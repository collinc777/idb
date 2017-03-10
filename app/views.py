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
character_list = [{"name": n[0], "house": n[1], "age": n[2], "status": n[3]} for n in zip(names, houses, ages, status)]

@application.route('/', methods=['GET', 'POST'])
def index():
    context = dict(navigation=navigation, nav_highlight=0)
    return render_template('index.html', **context)

@application.route('/characters', methods=['GET', 'POST'])
def characters():
    context = dict(navigation=navigation, nav_highlight=1, characters=character_list)
    return render_template('characters.html', **context)

@application.route('/houses', methods=['GET', 'POST'])
def houses():
    context = dict(navigation=navigation, nav_highlight=2, characters=character_list)
    return render_template('characters.html', **context)

@application.route('/regions', methods=['GET', 'POST'])
def regions():
    context = dict(navigation=navigation, nav_highlight=3, characters=character_list)
    return render_template('characters.html', **context)

@application.route('/books', methods=['GET', 'POST'])
def books():
    context = dict(navigation=navigation, nav_highlight=4, characters=character_list)
    return render_template('characters.html', **context)
