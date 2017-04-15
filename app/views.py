# We'll define all of our views in this file. 

from flask import render_template, request, render_template_string
from app import application
from app.decorators import returns_json, takes_api_params, takes_search_params
from app.models import Book, Character, Alliance, House, getPropertyMatches
from sqlalchemy import desc
import json
from random import randint
import pdb
from operator import attrgetter
from subprocess import PIPE, check_output, STDOUT
import pickle

navigation = [{"url": "/", "name": "Home"}, {"url": "/characters", "name": "Characters"},
              {"url": "/houses", "name": "Houses"}, {"url": "/alliances", "name": "Alliances"},
              {"url": "/books", "name": "Books"}, {"url": "/devnotes", "name": "Dev Notes"},
              {"url": "/about", "name": "About"}]

HL_CHARACTERS = 1
HL_HOUSES = 2
HL_ALLIANCES = 3
HL_BOOKS = 4
HL_DEVNOTES = 5
HL_ABOUT = 6

def load_listing(filename):
    with open(filename) as data_file:
        return json.load(data_file)

allHouses = pickle.load(open("data/allHouses.pickle", "rb")) # House.query.all()
allCharacters = pickle.load(open("data/allCharacters.pickle", "rb")) # Character.query.all()
allBooks = pickle.load(open("data/allBooks.pickle", "rb")) # Book.query.all()
allAlliances = pickle.load(open("data/allAlliances.pickle", "rb")) # Alliance.query.all()

def buildInstanceLinks(models):
    modelLinks = dict()
    for model in models:
        modelDict = model.toDict()
        modelLinks[modelDict["id"]] = {"url": "/" + modelDict["modelType"] + "s/" + str(modelDict["id"]), "name": modelDict["name"]}
    return modelLinks


house_links_list = buildInstanceLinks(allHouses)
character_links_list = buildInstanceLinks(allCharacters)
book_links_list = buildInstanceLinks(allBooks)
alliance_links_list = buildInstanceLinks(allAlliances)


@application.context_processor
def house_links():
    return dict(house_links=house_links_list)

@application.context_processor
def character_links():
    return dict(character_links=character_links_list)

@application.context_processor
def book_links():
    return dict(book_links=book_links_list)

@application.context_processor
def alliance_links():
    return dict(alliance_links=alliance_links_list)

# @application.context_processor
# def getIdList(links_list):
#     def getIdListInner(links_list):
#         for link in links_list:
#             return link["id"]
#     return dict(getIdList=getIdListInner())

# Each Listing requires a "title" and a "properties" array
# properties are simply 2-element arrays of a human readable name and a dictionary key
# e.g. ["Image", "imageLink"] -> Image (for table header) and house["imageLink"] when accessed

# character_links, house_links and book_links are used to provide human readable
# they ARE duplicated data... but they make our lives much easier
# links between resources. E.g. in the books/2 page we want to have links to the 
# POV (point-of-view) characters that are in it. So we pass it the character_links array

character_listing = dict(model=Character, title="Characters", url="/characters", sorts=Character.getHumanReadableSortableProperties())
house_listing = dict(model=House, title="Houses", url="/houses", sorts=House.getHumanReadableSortableProperties())
book_listing = dict(model=Book, title="Books", url="/books", sorts=Book.getHumanReadableSortableProperties())
alliance_listing = dict(model=Alliance, title="Alliances", url="/alliances", sorts=Alliance.getHumanReadableSortableProperties())


book_images = {1: "agameofthrones.jpg", 2: "aclashofkings.jpg", 3: "astormofswords.jpg", 4: "thehedgeknight.jpg",
               5: "afeastforcrows.jpg", 6: "theswornsword.jpg", 7: "themysteryknight.jpg", 8: "adancewithdragons.jpg",
               9: "theprincessandthequeen.jpg", 10: "therogueprince.jpg", 11: "theworldoficeandfire.png",
               12: "aknightofthesevenkingdoms.jpg"}
# book_images is a total hack right now. Ideally this would be a field inside the book data/model
# but for now we'll just do this. Theres only 12 books so it'll be easy to add it in manually later


# Build a base "context" dictionary for passing to any given template
def create_context(nav_highlight=-1, **kwargs):
    # nav_highlight tells which navigation item to highlight
    # nocache provides a way to stop the browser from caching our scripts and css files
    # kwargs provides a way to add additional info to the context, per-page
    return dict(navigation=navigation, nav_highlight=nav_highlight, nocache=randint(1,1000000), **kwargs)

@application.route('/tests', methods=['GET'])
def runTestsForAboutPage():
    command = ['python', '-m', 'app.tests']
    env = os.environ.copy()
    env['PYTHONPATH'] = ':'.join(sys.path)
    result = Popen(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, env=env)
    (stdout, stderr) = result.communicate()
    print(stderr)
    return stderr

### Begin Landing Page ###

@application.route('/', methods=['GET'])
def index():
    context = create_context(0)
    return render_template('index.html', **context)

### End Landing Page ###


### Begin Search Page and API ###

def getSearchResultData(query):
    global allHouses
    global allCharacters
    global allBooks
    global allAlliances

    allModels = allHouses + allCharacters + allBooks + allAlliances

    # list of lists of dictionaries
    fullQueryResults = list()
    for word in query.split(" "):
        wordResults = list()
        for model in allModels:
            propertyMatches = getPropertyMatches(model, word)
            if propertyMatches is not None and len(propertyMatches):
                modelDict = model.toDict()
                wordResults.append(dict(resultID=modelDict["id"], resultModelName=modelDict["name"], resultModelType=modelDict["modelType"], resultPropertyMatches=propertyMatches))
        fullQueryResults.append(wordResults)

    print("Total query results: ", sum([len(wordResults) for wordResults in fullQueryResults]))

    # dictionary with added properties, 
    # so ties can be broken in this order: weight, resultPropertMatchesLength

    weightedQueryResults = dict()
    for wordResults in fullQueryResults:
        for wordResult in wordResults:
            rid = wordResult["resultID"]
            if rid in weightedQueryResults:
                weightedQueryResults[rid]["weight"] += 1
                weightedQueryResults[rid]["resultPropertyMatches"].extend(wordResult["resultPropertyMatches"])
            else:
                weightedQueryResults[rid] = wordResult
                weightedQueryResults[rid]["weight"] = 1
            weightedQueryResults[rid]["resultPropertyMatchesLength"] = len(weightedQueryResults[rid]["resultPropertyMatches"])
        
    results = list(weightedQueryResults.values())
    print(json.dumps(results))
    """trimmed_results = list()
    for r in results:
        trimmed_results.append({k:v} for k,v in r if k in ["weight", "resultModelName"]]
        
        
    json.dump(trimmed_results, open("data/fuck.json", "w"))
    """

    #results = sorted(results, key=attrgetter("weight"))

    return results

@application.route('/search', methods=['GET'])
@takes_search_params
def search(query):
    searchResults = getSearchResultData(query)

    pagedSearchResults = searchResults[:5]
    page_data = {"currentPage": 1, "numberPages": max(len(searchResults) // 5, 1)}

    context = create_context(0, query=query, numberOfResults=len(searchResults), searchResults=pagedSearchResults, pageData=page_data)
    return render_template('search.html', **context)


@application.route('/api/search', methods=['GET'])
@returns_json
@takes_search_params
def get_search(**kwargs):
    query = kwargs.get("query")
    page = kwargs.get("page")
    page = max(1, page)

    pageStart = (page - 1) * 5
    pageEnd = page * 5

    array = ["a","b","C","d"]
    array[2] = "C"

    searchResults = getSearchResultData(query)
    pagedSearchResults = searchResults[pageStart:pageEnd]

    page_data = {"currentPage": page, "numberPages": max(len(searchResults) // 5, 1)}
    return json.dumps({"resultsData": pagedSearchResults, "pageData": page_data})

### End Landing Page ###

def getDataList(listing, params, modelLinks):
    cardURL = listing["url"]
    dataListing = list()
    model = listing["model"]
    page = params["page"]
    page = max(1, page) # make sure we don't go negative
    dataQuery = model.query

    if "sortParam" in params:
        try:
            if "sortAscending" in params and params["sortAscending"] == 0:
                dataQuery = dataQuery.order_by(desc(getattr(model, params["sortParam"])))
            else:
                dataQuery = dataQuery.order_by(getattr(model, params["sortParam"]))
        except:
            print("Sort Parameter: ", params["sortParam"], " is incorrect")
            return None

    modelInstances = dataQuery.all()

    if "filterText" in params:
        # use property match Search API for filtering now
        filteredModelInstances = []
        query = params["filterText"]
        for m in modelInstances:
            matches = getPropertyMatches(m, query)
            if len(matches) > 0:
                modelInstances.append(m)
        if len(filteredModelInstances) > 0:
            modelInstances = filteredModelInstances

    numberOfResults = len(modelInstances)
    page_data = {"currentPage": page, "numberPages": max(numberOfResults // 21, 1)}

    modelInstances = modelInstances[(page-1)*21:page*21]

    dictResults = [c.toDict() for c in modelInstances]
    
    listing_list = dict(pageData=page_data, modelData=dictResults, modelLinks=modelLinks)
    return listing_list

### Begin "API" Pages ###
### Note: These also accept POST requests, behavior will be as follows: 
### GET /api/modeltype?page=[int]
### The following are OPTIONAL parameters
### GET /api/modeltype?page=[int]&offset=[int]&sortParam=[string]&sortAscending=[bool]&filter=[string]

### POST /api/modeltype
### request body contains JSON of model data to ADD to database

@application.route('/api/characters', methods=['GET', 'POST'])
@returns_json
@takes_api_params
def get_characters(**kwargs):
    json_out = getDataList(character_listing, kwargs)
    return json.dumps(json_out)


@application.route('/api/houses', methods=['GET', 'POST'])
@returns_json
@takes_api_params
def get_houses(**kwargs):
    json_out = getDataList(house_listing, kwargs)
    return json.dumps(json_out)


@application.route('/api/alliances', methods=['GET', 'POST'])
@returns_json
@takes_api_params
def get_alliances(**kwargs):
    json_out = getDataList(alliance_listing, kwargs)
    return json.dumps(json_out)


@application.route('/api/books', methods=['GET', 'POST'])
@returns_json
@takes_api_params
def get_books(**kwargs):
    json_out = getDataList(book_listing, kwargs)
    return json.dumps(json_out)

### End "API" Pages ###



### Begin "Listing" Pages ###

default_params = dict(page=1, sortParam="name", sortAscending=1)

@application.route('/characters', methods=['GET'])
def characters():
    character_data = get_characters()
    # characters link to other characters, houses, books
    model_links = dict(characters=character_links, houses=house_links, books=book_links)

    context = create_context(HL_CHARACTERS, listing=character_listing, data=getDataList(character_listing, default_params, model_links))
    return render_template('listing.html', **context)


@application.route('/houses', methods=['GET'])
def houses():
    model_links = dict(characters=character_links, houses=house_links, alliances=alliance_links)

    context = create_context(HL_HOUSES, listing=house_listing, data=getDataList(house_listing, default_params, model_links))
    return render_template('listing.html', **context)


@application.route('/alliances', methods=['GET'])
def alliances():
    model_links = dict(characters=character_links, houses=house_links)
    context = create_context(HL_ALLIANCES, listing=alliance_listing, data=getDataList(alliance_listing, default_params, model_links))
    return render_template('listing.html', **context)


@application.route('/books', methods=['GET'])
def books():
    model_links = dict(characters=character_links)
    context = create_context(HL_BOOKS, listing=book_listing, data=getDataList(book_listing, default_params, model_links))
    return render_template('listing.html', **context)


### End "Listing" Pages ###


### Begin "Detail" Pages ###
@application.route("/characters/<charid>")
def character(charid):
    global allCharacters
    try:
        charid = int(charid)
    except ValueError:
        # Could not even convert to an integer, return empty page for now
        return render_template('notfound.html', **create_context(1, entity="Character", entity_id=charid))


    character = None
    for c in allCharacters:
        if c.id == charid:
            character = c
    if character is None:
        context = create_context(HL_CHARACTERS, entity="Character", entity_id=charid)
        return render_template('notfound.html', **context)
    else:
        context = create_context(HL_CHARACTERS, character=character)
        return render_template('character.html', **context)


@application.route("/houses/<houseid>")
def house(houseid):
    global allHouses
    try:
        houseid = int(houseid)
    except ValueError:
        # Could not even convert to an integer, return empty page for now
        return render_template('notfound.html', **create_context(1, entity="House", entity_id=houseid))

    house = None
    for h in allHouses:
        if h.id == houseid:
            house = h

    if house is None:
        context = create_context(HL_HOUSES, entity="House", entity_id=houseid)
        return render_template('notfound.html', **context)
    else:
        context = create_context(HL_HOUSES, house=house)#, character_links=character_links, house_links=house_links,alliance_links=alliance_links)
        return render_template('house.html', **context)


@application.route("/books/<bookid>")
def book(bookid):
    global allBooks
    try:
        bookid = int(bookid)
    except ValueError:
        # Could not even convert to an integer, return empty page for now
        return render_template('notfound.html', **create_context(1, entity="Book", entity_id=bookid))

    book = None
    for b in allBooks:
        if b.id == bookid:
            book = b

    if book is None:
        context = create_context(HL_BOOKS, entity="Book", entity_id=bookid)
        return render_template('notfound.html', **context)
    else:
        context = create_context(HL_BOOKS, book=book, book_images=book_images)
        return render_template('book.html', **context)


@application.route("/alliances/<allianceid>")
def alliance(allianceid):
    global allAlliances
    try:
        allianceid = int(allianceid)
    except ValueError:
        # Could not even convert to an integer, return empty page for now
        return render_template('notfound.html', **create_context(1, entity="Alliance", entity_id=allianceid))

    alliance = None
    for a in allAlliances:
        if a.id == allianceid:
            alliance = a

    if alliance is None:
        context = create_context(HL_ALLIANCES, entity="Alliance", entity_id=allianceid)
        return render_template('notfound.html', **context)
    else:
        context = create_context(HL_ALLIANCES, alliance=alliance)
        return render_template('alliance.html', **context)

### End "Detail" Pages ###


### Begin "Miscellaneous" Pages ###


@application.route('/devnotes', methods=['GET'])
def devnotes():
    context = create_context(HL_DEVNOTES)
    return render_template('devnotes.html', **context)


@application.route('/about', methods=['GET'])
def about():
    context = create_context(HL_ABOUT)
    return render_template('about.html', **context)


### End "Miscellaneous" Pages ###

