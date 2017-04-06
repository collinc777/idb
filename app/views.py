# We'll define all of our views in this file. 

from flask import render_template, request
from app import application
from app.decorators import returns_json, takes_query_params
from app.models import Book, Character, Alliance, House
from sqlalchemy import desc
import json
from random import randint
import pdb

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


# Each Listing requires a "title" and a "properties" array
# properties are simply 2-element arrays of a human readable name and a dictionary key
# e.g. ["Image", "imageLink"] -> Image (for table header) and house["imageLink"] when accessed

# character_links, house_links and book_links are used to provide human readable
# they ARE duplicated data... but they make our lives much easier
# links between resources. E.g. in the books/2 page we want to have links to the 
# POV (point-of-view) characters that are in it. So we pass it the character_links array

character_listing = dict(model=Character, title="Characters", url="/characters", sorts=Character.getSorts())
character_listing["data"] = load_listing("data/trimmed_characters.json") #this needs to be a db call?
character_links = dict()
for character in character_listing["data"]:
    character_links[character["id"]] = {"name": character["name"], "link": "/characters/" + str(character["id"])}

house_listing = dict(model=House, title="Houses", url="/houses", sorts=House.getSorts())
house_listing["data"] = load_listing("data/trimmed_houses_alliances.json")
house_links = dict()
for house in house_listing["data"]:
    house_links[house["id"]] = {"name": house["name"], "link": "/houses/" + str(house["id"])}

book_listing = dict(model=Book, title="Books", url="/books", sorts=Book.getSorts())
book_listing["data"] = load_listing("data/trimmed_books.json")
book_links = dict()
for book in book_listing["data"]:
    book_links[book["id"]] = {"name": book["name"], "link": "/books/" + str(book["id"])}
book_images = {1: "agameofthrones.jpg", 2: "aclashofkings.jpg", 3: "astormofswords.jpg", 4: "thehedgeknight.jpg",
               5: "afeastforcrows.jpg", 6: "theswornsword.jpg", 7: "themysteryknight.jpg", 8: "adancewithdragons.jpg",
               9: "theprincessandthequeen.jpg", 10: "therogueprince.jpg", 11: "theworldoficeandfire.png",
               12: "aknightofthesevenkingdoms.jpg"}
# book_images is a total hack right now. Ideally this would be a field inside the book data/model
# but for now we'll just do this. Theres only 12 books so it'll be easy to add it in manually later

alliance_listing = dict(model=Alliance, title="Alliances", url="/alliances", sorts=Alliance.getSorts())
alliance_listing["data"] = load_listing("data/trimmed_alliances.json")
alliance_links = dict()
for alliance in alliance_listing["data"]:
    alliance_links[alliance["id"]] = {"name": alliance["name"], "link": "/alliances/" + str(alliance["id"])}


# Build a base "context" dictionary for passing to any given template
def create_context(nav_highlight=-1, **kwargs):
    # nav_highlight tells which navigation item to highlight
    # nocache provides a way to stop the browser from caching our scripts and css files
    # kwargs provides a way to add additional info to the context, per-page
    return dict(navigation=navigation, nav_highlight=nav_highlight, nocache=randint(1,1000000), **kwargs)


### Begin Landing Page ###

@application.route('/', methods=['GET', 'POST'])
def index():
    context = create_context(0)
    return render_template('index.html', **context)

### End Landing Page ###

#model.convertSort("Name") returns "name"
#model.convertSort("Number of pages") returns numberOfPages etc
#also, I added a "model" key to each listing dictionary
# book_listing = dict(model=Book, title="Books", url="/books", sorts=Book.getSorts())
# like this^^
def getDataList(listing, params=None):
    if params is None:
        return [] #should not happen due to decorator
    cardURL = listing["url"]
    print("Params: ", params)
    dataListing = list()
    model = listing["model"]
    page = params["page"]
    dataQuery = model.query

    if "sortParam" in params:
        if "sortAscending" in params and params["sortAscending"] == 0:
            dataQuery = model.query.order_by(desc(getattr(model, model.convertSort(params["sortParam"]))))
        else:
            dataQuery = model.query.order_by(getattr(model, model.convertSort(params["sortParam"])))
        print("Books sorted by paramter: ", params["sortParam"])
    modelInstances = []
    if "filter" in params:
        #only does exact match on name for now
        modelInstances = dataQuery.filter(model.name.match(params["filter"])).slice((page-1)*20, 20).all()
    else:
        modelInstances = dataQuery.slice((page-1)*20, page*20).all() #only display up to 20 results
    jsonResults = [json.loads(c.toJSON()) for c in modelInstances]
    print([result["name"] for result in jsonResults])
    listing_list = [dict(cardURL=cardURL, cardID=i, cardName=res["name"]) for i, res in enumerate(jsonResults)]
    #modelInstances = dataQuery.slice((page-1)*20, page*20).all()
    #jsonResults = [modelInstances[i].toJSON() for i in range((page-1)*20, min(len(modelInstances), page*20))]

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
@takes_query_params
def get_characters(**kwargs):
    json_out = getDataList(character_listing, kwargs)
    return json.dumps(json_out)


@application.route('/api/houses', methods=['GET', 'POST'])
@returns_json
@takes_query_params
def get_houses(**kwargs):
    json_out = getDataList(house_listing, kwargs)
    return json.dumps(json_out)


@application.route('/api/alliances', methods=['GET', 'POST'])
@returns_json
@takes_query_params
def get_alliances(**kwargs):
    json_out = getDataList(alliance_listing, kwargs)
    return json.dumps(json_out)


@application.route('/api/books', methods=['GET', 'POST'])
@returns_json
@takes_query_params
def get_books(**kwargs):
    json_out = getDataList(book_listing, kwargs)
    return json.dumps(json_out)

### End "API" Pages ###



### Begin "Listing" Pages ###


@application.route('/characters', methods=['GET'])
def characters():
    character_data = get_characters()
    context = create_context(HL_CHARACTERS, listing=character_listing, data=getDataList(character_listing))
    return render_template('listing.html', **context)


@application.route('/houses', methods=['GET'])
def houses():
    context = create_context(HL_HOUSES, listing=house_listing, data=getDataList(house_listing))
    return render_template('listing.html', **context)


@application.route('/alliances', methods=['GET'])
def alliances():
    context = create_context(HL_ALLIANCES, listing=alliance_listing, data=getDataList(alliance_listing))
    return render_template('listing.html', **context)


@application.route('/books', methods=['GET'])
def books():
    context = create_context(HL_BOOKS, listing=book_listing, data=getDataList(book_listing))
    return render_template('listing.html', **context)


### End "Listing" Pages ###


### Begin "Detail" Pages ###

@application.route("/characters/<charid>")
def character(charid):
    try:
        charid = int(charid)
    except ValueError:
        # Could not even convert to an integer, return empty page for now
        return render_template('notfound.html', **create_context(1, entity="Character", entity_id=charid))

    character = None
    for c in character_listing["data"]:
        if c["id"] == charid:
            character = c
    if character is None:
        context = create_context(HL_CHARACTERS, entity="Character", entity_id=charid)
        return render_template('notfound.html', **context)
    else:
        context = create_context(HL_CHARACTERS, character=character, book_links=book_links, house_links=house_links)
        return render_template('character.html', **context)


@application.route("/houses/<houseid>")
def house(houseid):
    try:
        houseid = int(houseid)
    except ValueError:
        # Could not even convert to an integer, return empty page for now
        return render_template('notfound.html', **create_context(1, entity="House", entity_id=houseid))

    house = None
    for h in house_listing["data"]:
        if h["id"] == houseid:
            house = h
    if house is None:
        context = create_context(HL_HOUSES, entity="House", entity_id=houseid)
        return render_template('notfound.html', **context)
    else:
        context = create_context(HL_HOUSES, house=house, character_links=character_links, house_links=house_links,
                                 alliance_links=alliance_links)
        return render_template('house.html', **context)


@application.route("/books/<bookid>")
def book(bookid):
    try:
        bookid = int(bookid)
    except ValueError:
        # Could not even convert to an integer, return empty page for now
        return render_template('notfound.html', **create_context(1, entity="Book", entity_id=bookid))

    book = None
    for b in book_listing["data"]:
        if b["id"] == bookid:
            book = b
    if book is None:
        context = create_context(HL_BOOKS, entity="Book", entity_id=bookid)
        return render_template('notfound.html', **context)
    else:
        context = create_context(HL_BOOKS, book=book, character_links=character_links, house_links=house_links,
                                 book_images=book_images)
        return render_template('book.html', **context)


@application.route("/alliances/<allianceid>")
def alliance(allianceid):
    try:
        allianceid = int(allianceid)
    except ValueError:
        # Could not even convert to an integer, return empty page for now
        return render_template('notfound.html', **create_context(1, entity="Alliance", entity_id=allianceid))

    alliance = None
    for a in alliance_listing["data"]:
        if a["id"] == allianceid:
            alliance = a
    if alliance is None:
        context = create_context(HL_ALLIANCES, entity="Alliance", entity_id=allianceid)
        return render_template('notfound.html', **context)
    else:
        context = create_context(HL_ALLIANCES, alliance=alliance, character_links=character_links,
                                 house_links=house_links)
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

