# We'll define all of our views in this file. 

from flask import render_template, flash, redirect
from app import application
import json

navigation = [{"url": "/", "name": "Home"}, {"url": "/characters", "name": "Characters"}, {"url": "/houses", "name": "Houses"}, {"url": "/regions", "name": "Regions"}, {"url": "/books", "name": "Books"}, {"url":"/devnotes","name":"Dev Notes"}]
names = ["Catelyn Tully", "Tyrion Lannister", "Eddard Stark"]
houses = ["House Tully", "House Lannister", "House Stark"]
ages = [16, 45, 60]
status = [True, True, False]

HL_CHARACTERS = 1
HL_HOUSES = 2
HL_REGIONS = 3
HL_BOOKS = 4
HL_DEVNOTES = 5

def loadListing(filename):
    with open(filename) as data_file:
        return json.load(data_file)

# Each Listing requires a "title" and a "properties" array
# properties are simply 2-element arrays of a human readable name and a dictionary key
# e.g. ["Image", "imageLink"] -> Image (for table header) and house["imageLink"] when accessed


character_listing = {"title": "Characters", "properties": [["Name", "name"], ["Gender", "male"], ["Culture", "culture"], ["House", "house"]]}
character_listing["data"] = loadListing("data/trimmed_characters.json")

house_listing = {"title": "Houses", "properties": [["Name", 'name'], ["Image",'imageLink'], ["Current Lord", 'currentLord'], ["Region", 'region'], ["Coat of Arms", 'coatOfArms'], ["Founded", 'founded'], ["Overlord", 'overlord'], ["Extinct?", 'isExtinct'], ["Words", 'words']]}
house_listing["data"] = loadListing("data/trimmed_houses.json")

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
        return render_template('notfound.html', entity="Character", **createContext(1, entity="Character", entity_id=charid))
    
    character = None
    for c in character_listing["data"]:
        if c["id"] == charid:
            character = c
    if character is None:
        context = createContext(HL_CHARACTERS, entity="Character", entity_id=charid)
        return render_template('notfound.html', **context)
    else:
        context = createContext(HL_CHARACTERS, character=character)
        return render_template('character.html', **context)

@application.route("/houses/<houseid>")
def house(houseid):
    try:
        houseid = int(houseid)
    except:
        # Could not even convert to an integer, return empty page for now
        return render_template('notfound.html', entity="House", **createContext(1, entity="House", entity_id=houseid))
    
    house = None
    for h in house_listing["data"]:
        if h["id"] == houseid:
            house = h
    if house is None:
        context = createContext(HL_HOUSES, entity="House", entity_id=houseid)
        return render_template('notfound.html', **context)
    else:
        context = createContext(HL_HOUSES, house=house)
        return render_template('house.html', **context)

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
    context = createContext(HL_BOOKS, listing=character_listing)
    return render_template('listing.html', **context)

@application.route('/devnotes', methods=['GET', 'POST'])
def devnotes():
    context = createContext(HL_DEVNOTES)
    return render_template('devnotes.html', **context)