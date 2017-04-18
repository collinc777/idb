# We'll define all of our views in this file. 

import json
import os
from random import randint
from subprocess import PIPE, Popen

import sys
from flask import render_template
from sqlalchemy import desc

from app import application
from app.decorators import returns_json, takes_api_params, takes_search_params
from app.models import Book, Character, Alliance, House, getPropertyMatches, combinePropertyMatches

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
HL_BASKETBALL = 7


def load_listing(filename):
    with open(filename) as data_file:
        return json.load(data_file)


# allHouses = pickle.load(open("data/allHouses.pickle", "rb")) # House.query.all()
# allCharacters = pickle.load(open("data/allCharacters.pickle", "rb")) # Character.query.all()
# allBooks = pickle.load(open("data/allBooks.pickle", "rb")) # Book.query.all()
# allAlliances = pickle.load(open("data/allAlliances.pickle", "rb")) # Alliance.query.all()

allHouses = House.query.all()
allCharacters = Character.query.all()
allBooks = Book.query.all()
allAlliances = Alliance.query.all()


# pickle.dump(allHouses, open("data/allHouses.pickle", "wb"))
# pickle.dump(allCharacters, open("data/allCharacters.pickle", "wb"))
# pickle.dump(allBooks, open("data/allBooks.pickle", "wb"))
# pickle.dump(allAlliances, open("data/allAlliances.pickle", "wb"))


def buildInstanceLinks(models):
    modelLinks = dict()
    for model in models:
        modelDict = model.toDict()
        modelLinks[modelDict["id"]] = {"url": "/" + modelDict["modelType"] + "s/" + str(modelDict["id"]),
                                       "name": modelDict["name"]}
    return modelLinks


house_links_list = buildInstanceLinks(allHouses)
character_links_list = buildInstanceLinks(allCharacters)
book_links_list = buildInstanceLinks(allBooks)
alliance_links_list = buildInstanceLinks(allAlliances)


# character_links, house_links and book_links are used to provide human readable
# they ARE duplicated data... but they make our lives much easier
# links between resources. E.g. in the books/2 page we want to have links to the 
# POV (point-of-view) characters that are in it. So we pass it the character_links array
# Luckily, jinja2 templates allow us to inject these into every page ! 
### This makes all links available on all pages ###

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


character_listing = dict(model=Character, title="Characters", url="/characters",
                         sorts=Character.getHumanReadableSortableProperties())
house_listing = dict(model=House, title="Houses", url="/houses",
                     sorts=House.getHumanReadableSortableProperties())
book_listing = dict(model=Book, title="Books", url="/books",
                    sorts=Book.getHumanReadableSortableProperties())
alliance_listing = dict(model=Alliance, title="Alliances", url="/alliances",
                        sorts=Alliance.getHumanReadableSortableProperties())


# Build a base "context" dictionary for passing to any given template
def create_context(nav_highlight=-1, **kwargs):
    # nav_highlight tells which navigation item to highlight
    # nocache provides a way to stop the browser from caching our scripts and css files
    # kwargs provides a way to add additional info to the context, per-page
    return dict(navigation=navigation, nav_highlight=nav_highlight, nocache=randint(1, 1000000), **kwargs)


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
                wordResults.append(dict(resultID=modelDict["id"], resultModelName=modelDict["name"],
                                        resultModelType=modelDict["modelType"], resultPropertyMatches=propertyMatches))
        fullQueryResults.append(wordResults)

    # print("Total query results: ", sum([len(wordResults) for wordResults in fullQueryResults]))

    # dictionary with added properties, for sorting based on relevance AND/OR basically
    # so ties can be broken in this order: weight, resultPropertMatchesLength

    weightedQueryResults = dict()
    for wordResults in fullQueryResults:
        for wordResult in wordResults:
            rid = wordResult["resultID"]
            rmn = wordResult["resultModelType"]
            k = (rid, rmn)
            if k in weightedQueryResults:
                weightedQueryResults[k]["weight"] += 1
                cpm = combinePropertyMatches(weightedQueryResults[k]["resultPropertyMatches"],
                                             wordResult["resultPropertyMatches"])
                weightedQueryResults[k]["resultPropertyMatches"] = cpm
            else:
                weightedQueryResults[k] = wordResult
                weightedQueryResults[k]["weight"] = 1
            weightedQueryResults[k]["resultPropertyMatchesLength"] = len(
                weightedQueryResults[k]["resultPropertyMatches"])

    # Sort by a key that is just the integer made by combining the digits of these
    # so a model that was matched twice has more relevance than a model that was
    # matched by 9 different properties but by only one of the words in the query
    def andOrKey(r):
        return int(str(r["weight"]) + str(r["resultPropertyMatchesLength"]))

    results = list(weightedQueryResults.values())
    results = sorted(results, key=andOrKey, reverse=True)

    for w in results[:10]:
        print("[ID: ", w["resultID"], "] [", w["resultModelName"], "]  [SearchRank:",
              andOrKey(w), "]")

    return results


@application.route('/search', methods=['GET'])
@takes_search_params
def search(query):
    searchResults = getSearchResultData(query)

    pagedSearchResults = searchResults[:10]
    page_data = {"currentPage": 1, "numberPages": max(len(searchResults) // 10, 1)}

    context = create_context(0, query=query, numberOfResults=len(searchResults), searchResults=pagedSearchResults,
                             pageData=page_data)
    return render_template('search.html', **context)


@application.route('/api/search', methods=['GET'])
@returns_json
@takes_search_params
def get_search(**kwargs):
    query = kwargs.get("query")
    page = kwargs.get("page")
    page = max(1, page)

    pageStart = (page - 1) * 10
    pageEnd = page * 10

    searchResults = getSearchResultData(query)
    pagedSearchResults = searchResults[pageStart:pageEnd]

    page_data = {"currentPage": page, "numberPages": max(len(searchResults) // 10, 1)}
    return json.dumps({"resultsData": pagedSearchResults, "pageData": page_data})


### End Landing Page ###

def getDataList(listing, params):
    cardURL = listing["url"]
    dataListing = list()
    model = listing["model"]
    page = params["page"]
    page = max(1, page)  # make sure we don't go negative
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
                filteredModelInstances.append(m)
        if len(filteredModelInstances) > 0:
            modelInstances = filteredModelInstances

    numberOfResults = len(modelInstances)
    page_data = {"currentPage": page, "numberPages": max(numberOfResults // 21, 1)}

    modelInstances = modelInstances[(page - 1) * 21:page * 21]

    dictResults = [c.toDict() for c in modelInstances]

    listing_list = dict(pageData=page_data, modelData=dictResults)
    return listing_list


def loadBasketballData(dataName):
    print("in load basketball data")
    with open('data/basketballmania/' + dataName + '.json') as data_file:
        return json.load(data_file)


def getBasketBallData():
    games = loadBasketballData('games')
    players = loadBasketballData('players')
    teams = loadBasketballData('teams')
    venues = loadBasketballData('venues')
    return dict(games=games, players=players, teams=teams, venues=venues)


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
    context = create_context(HL_CHARACTERS, listing=character_listing,
                             data=getDataList(character_listing, default_params))
    return render_template('listing.html', **context)


@application.route('/houses', methods=['GET'])
def houses():
    context = create_context(HL_HOUSES, listing=house_listing, data=getDataList(house_listing, default_params))
    return render_template('listing.html', **context)


@application.route('/alliances', methods=['GET'])
def alliances():
    context = create_context(HL_ALLIANCES, listing=alliance_listing, data=getDataList(alliance_listing, default_params))
    return render_template('listing.html', **context)


@application.route('/books', methods=['GET'])
def books():
    context = create_context(HL_BOOKS, listing=book_listing, data=getDataList(book_listing, default_params))
    return render_template('listing.html', **context)


### End "Listing" Pages ###

### Start "Details page data builder" ###
def createDetailsWithQuery(model, instance, query=None):
    lookup = model.getHumanReadableProperties()
    instance = instance.toDict()
    modelLinks = model.getModelLinks()

    # copied from DetailsCard.jsx
    # propertyType possible values: 
    # "linkarray": combines the next two, value will be array of ids, modelLinks will have links to the models
    # "link": link to another model, value will be ID, modelLinks will have links to the models
    # "array": array of elements, value will be array
    # "default": just display readable name and then the value in text

    properties = list()
    for name, readable in lookup.items():
        prop = dict(readableName=readable, propertyName=name)
        value = instance.get(name, "")

        shouldDisplay = False
        if "_ids" in name:
            # linkarray
            prop["propertyType"] = "linkarray"
            prop["propertyValue"] = value
            prop["propertyModelLinks"] = modelLinks[name]
            if value and len(value):
                shouldDisplay = True
        elif "_id" in name:
            # link
            prop["propertyType"] = "link"
            prop["propertyValue"] = value
            prop["propertyModelLinks"] = modelLinks[name]
            if value and len(str(value)):
                shouldDisplay = True
        elif isinstance(value, list):
            # array
            prop["propertyType"] = "array"
            prop["propertyValue"] = value
            if value and len(value):
                shouldDisplay = True
        else:
            # default
            prop["propertyType"] = "default"
            prop["propertyValue"] = value
            if value and len(str(value)):
                shouldDisplay = True
        if shouldDisplay:
            properties.append(prop)
    return properties


### End "Details page data builder" ###


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
        context = create_context(HL_CHARACTERS, details_name=character.name,
                                 details_image_link="/static/img/chars/" + str(character.id) + ".jpg",
                                 details_data=createDetailsWithQuery(Character, character))
        return render_template('details.html', **context)


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
        context = create_context(HL_HOUSES, details_name=house.name,
                                 details_image_link="/static/img/houses/" + str(house.id) + ".png",
                                 details_data=createDetailsWithQuery(House, house))
        return render_template('details.html', **context)


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
        context = create_context(HL_BOOKS, details_name=book.name,
                                 details_image_link="/static/img/books/" + str(book.id) + ".jpg",
                                 details_data=createDetailsWithQuery(Book, book))
        return render_template('details.html', **context)


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
        context = create_context(HL_ALLIANCES, details_name=alliance.name,
                                 details_image_link="/static/img/alliances/" + str(alliance.id) + ".png",
                                 details_data=createDetailsWithQuery(Alliance, alliance))
        return render_template('details.html', **context)


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

### Start basketball mania page ###


@application.route('/basketballmania')
def basketballMania():
    context = create_context(HL_BASKETBALL, data=getBasketBallData())
    return render_template('basketballmania.html', **context)

    ### End basketball mania page ###
