# We'll define all of our views in this file. 

from flask import render_template, flash, redirect
from app import application

navigation = [{"url": "/", "name": "Home"}, {"url": "/characters", "name": "Characters"}, {"url": "/houses", "name": "Houses"}, {"url": "/regions", "name": "Regions"}, {"url": "/books", "name": "Books"}]
names = ["Catelyn Tully", "Tyrion Lannister", "Eddard Stark"]
houses = ["House Tully", "House Lannister", "House Stark"]
ages = [16, 45, 60]
status = [True, True, False]

# Build some fake data for our table for now
# demonstrating how to pass information to a rendered template
character_listing = {"title": "Characters", "properties": [["Name", "name"], ["House", "house"], ["Age", "age"], ["Alive?", "status"]]}
character_listing["data"] = [{"id": i, "name": n[0], "house": n[1], "age": n[2], "status": n[3]} for i, n in enumerate(zip(names, houses, ages, status))]

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
        print(c)
        if c["id"] == charid:
            character = c
    if character is None:
        context = createContext(1, entity="Character", entity_id=charid)
        return render_template('notfound.html', **context)
    else:
        context = createContext(1, character=character)
        return render_template('character.html', **context)

@application.route('/characters', methods=['GET', 'POST'])
def characters():
    context = createContext(1, listing=character_listing)
    return render_template('listing.html', **context)

@application.route('/houses', methods=['GET', 'POST'])
def houses():
    context = createContext(2, listing=character_listing)
    return render_template('listing.html', **context)

@application.route('/regions', methods=['GET', 'POST'])
def regions():
    context = createContext(3, listing=character_listing)
    return render_template('listing.html', **context)

@application.route('/books', methods=['GET', 'POST'])
def books():
    context = createContext(4, listing=character_listing)
    return render_template('listing.html', **context)
