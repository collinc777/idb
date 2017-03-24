# We'll define all of our views in this file. 

from flask import render_template, flash, redirect
from app import application
import json

navigation = [{"url": "/", "name": "Home"}, {"url": "/characters", "name": "Characters"}, {"url": "/houses", "name": "Houses"}, {"url": "/regions", "name": "Regions"}, {"url": "/books", "name": "Books"}, {"url":"/devnotes","name":"Dev Notes"}, {"url":"/about","name":"About"}]

HL_CHARACTERS = 1
HL_HOUSES = 2
HL_REGIONS = 3
HL_BOOKS = 4
HL_DEVNOTES = 5
HL_ABOUT = 6

def loadListing(filename):
    with open(filename) as data_file:
        return json.load(data_file)

# Each Listing requires a "title" and a "properties" array
# properties are simply 2-element arrays of a human readable name and a dictionary key
# e.g. ["Image", "imageLink"] -> Image (for table header) and house["imageLink"] when accessed

# character_links, house_links and book_links are used to provide human readable
# they ARE duplicated data... but they make our lives much easier
# links between resources. E.g. in the books/2 page we want to have links to the 
# POV (point-of-view) characters that are in it. So we pass it the character_links array

character_listing = {"title": "Characters", "url": "/characters", "properties": [["Name", "name"], ["Gender", "male"], ["Culture", "culture"], ["House", "house"]]}
character_listing["data"] = loadListing("data/trimmed_characters_houses.json")
character_links = {character["id"]: {"name": character["name"], "link": "/characters/" + str(character["id"])} for character in character_listing["data"]}

house_listing = {"title": "Houses", "url": "/houses", "properties": [["Name", 'name'], ["Current Lord", 'currentLord'], ["Region", 'region'], ["Coat of Arms", 'coatOfArms'], ["Founded", 'founded'], ["Overlord", 'overlord'], ["Extinct?", 'isExtinct'], ["Words", 'words']]}
house_listing["data"] = loadListing("data/trimmed_houses.json")
house_links = {house["id"]: {"name": house["name"], "link": "/houses/" + str(house["id"])} for house in house_listing["data"]}

book_listing = {"title": "Books", "url": "/books", "properties": [["Name", "name"], ["Publisher", "publisher"], ["Country", "country"], ["Release Date", "released"], ["Media Type", "mediaType"]]}
book_listing["data"] = loadListing("data/api_ice_and_fire/trimmed_books.json")
book_links = {book["id"]: {"name": book["name"], "link": "/books/" + str(book["id"])} for book in book_listing["data"]}
book_images = {1: "agameofthrones.jpg", 2: "aclashofkings.jpg", 3: "astormofswords.jpg", 4: "thehedgeknight.jpg", 5: "afeastforcrows.jpg", 6: "theswornsword.jpg", 7: "themysteryknight.jpg", 8: "adancewithdragons.jpg", 9: "theprincessandthequeen.jpg", 10: "therogueprince.jpg", 11: "theworldoficeandfire.png", 12: "aknightofthesevenkingdoms.jpg"}
# book_images is a total hack right now. Ideally this would be a field inside the book data/model
# but for now we'll just do this. Theres only 12 books so it'll be easy to add it in manually later

# Build a base "context" dictionary for passing to any given template
def createContext(nav_highlight=-1, **kwargs):
    return dict(navigation=navigation, nav_highlight=nav_highlight, **kwargs)

@application.route('/', methods=['GET', 'POST'])
def index():
    context = createContext(0)
    return render_template('index.html', **context)

@application.route("/characters/<charid>")
def character(charid):
    try:
        charid = int(charid)
    except:
        # Could not even convert to an integer, return empty page for now
        return render_template('notfound.html', **createContext(1, entity="Character", entity_id=charid))
    
    character = None
    for c in character_listing["data"]:
        if c["id"] == charid:
            character = c
    if character is None:
        context = createContext(HL_CHARACTERS, entity="Character", entity_id=charid)
        return render_template('notfound.html', **context)
    else:
        context = createContext(HL_CHARACTERS, character=character, book_links=book_links, house_links=house_links)
        return render_template('character.html', **context)

@application.route("/houses/<houseid>")
def house(houseid):
    try:
        houseid = int(houseid)
    except:
        # Could not even convert to an integer, return empty page for now
        return render_template('notfound.html', **createContext(1, entity="House", entity_id=houseid))
    
    house = None
    for h in house_listing["data"]:
        if h["id"] == houseid:
            house = h
    if house is None:
        context = createContext(HL_HOUSES, entity="House", entity_id=houseid)
        return render_template('notfound.html', **context)
    else:
        context = createContext(HL_HOUSES, house=house, character_links=character_links, house_links=house_links)
        return render_template('house.html', **context)

@application.route("/books/<bookid>")
def book(bookid):
    try:
        bookid = int(bookid)
    except:
        # Could not even convert to an integer, return empty page for now
        return render_template('notfound.html', **createContext(1, entity="Book", entity_id=bookid))
    
    book = None
    for b in book_listing["data"]:
        if b["id"] == bookid:
            book = b
    if book is None:
        context = createContext(HL_BOOKS, entity="Book", entity_id=bookid)
        return render_template('notfound.html', **context)
    else:
        context = createContext(HL_BOOKS, book=book, character_links=character_links, book_images=book_images)
        return render_template('book.html', **context)

@application.route('/characters', methods=['GET', 'POST'])
def characters():
    context = createContext(HL_CHARACTERS, listing=character_listing)
    return render_template('listing.html', **context)

@application.route('/houses', methods=['GET', 'POST'])
def houses():
    context = createContext(HL_HOUSES, listing=house_listing)
    return render_template('listing.html', **context)

@application.route('/regions', methods=['GET', 'POST'])
def regions():
    context = createContext(HL_REGIONS, listing=character_listing)
    return render_template('listing.html', **context)

@application.route('/books', methods=['GET', 'POST'])
def books():
    context = createContext(HL_BOOKS, listing=book_listing)
    return render_template('listing.html', **context)

@application.route('/devnotes', methods=['GET', 'POST'])
def devnotes():
    context = createContext(HL_DEVNOTES)
    return render_template('devnotes.html', **context)

@application.route('/about', methods=['GET'])
def about():
    context = createContext(HL_ABOUT)
    return render_template('about.html', **context)