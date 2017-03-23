#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = too-many-public-methods
# pylint: disable = line-too-long
# pylint: disable = bad-continuation
# pylint: disable = too-many-arguments
# pylint: disable = too-many-instance-attributes
# pylint: disable = too-few-public-methods
# pylint: disable = too-many-locals

# -------
# imports
# -------

from app import database

# -------
# Models
# -------

# Foreign key relationships are alternative for povCharacter and characters (need consult for IDB2)
# povCharacters = database.relationship('Character')
# See link: http://docs.sqlalchemy.org/en/latest/orm/join_conditions.html
# See link: http://flask-sqlalchemy.pocoo.org/2.1/models/


class Book(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    numberOfPages = database.Column(database.Integer)
    isbn = database.Column(database.String(13))
    name = database.Column(database.String(80))
    publisher = database.Column(database.String(80))
    country = database.Column(database.String(80))
    povCharacters = database.Column(database.ARRAY(database.Integer))
    author = database.Column(database.String(80))
    mediaType = database.Column(database.String(80))
    released = database.Column(database.String(80))
    characters = database.Column(database.ARRAY(database.Integer))

    def __init__(self, numberOfPages, isbn, name, publisher, country, povCharacters, author, mediaType, released, characters):
        self.numberOfPages = numberOfPages
        self.isbn = isbn
        self.name = name
        self.publisher = publisher
        self.country = country
        self.povCharacters = povCharacters
        self.author = author
        self.mediaType = mediaType
        self.released = released
        self.characters = characters

# Foreign key relationships are alternative for povBooks, playedBy, books,
# tvSeries (need consult for IDB2)


class Character(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    house = database.Column(database.String(80))
    culture = database.Column(database.String(80))
    titles = database.Column(database.ARRAY(database.String))
    spouse = database.Column(database.String(80))
    died = database.Column(database.String(80))
    aliases = database.Column(database.ARRAY(database.String))
    dateOfDeath = database.Column(database.Boolean)
    name = database.Column(database.String(80))
    born = database.Column(database.String(80))
    gender = database.Column(database.String(80))
    father = database.Column(database.String(80))
    allegiances = database.Column(database.ARRAY(database.String(80)))
    povBooks = database.Column(database.ARRAY(database.Integer))
    playedBy = database.Column(database.ARRAY(database.Integer))
    books = database.Column(database.ARRAY(database.Integer))
    tvSeries = database.Column(database.ARRAY(database.Integer))
    mother = database.Column(database.String(80))
    male = database.Column(database.Boolean)

    def __init__(self, house, culture, titles, spouse, died, aliases, dateOfDeath, name, born, gender, father, allegiances, povBooks, playedBy, books, tvSeries, mother, male):
        self.house = house
        self.culture = culture
        self.titles = titles
        self.spouse = spouse
        self.died = died
        self.aliases = aliases
        self.dateOfDeath = dateOfDeath
        self.name = name
        self.born = born
        self.gender = gender
        self.father = father
        self.allegiances = allegiances
        self.povBooks = povBooks
        self.playedBy = playedBy
        self.books = books
        self.tvSeries = tvSeries
        self.mother = mother
        self.male = male

# Foreign key relationships are alternative for currentLord, founder,
# heir, overlord, swornMembers (need consult for IDB2)


class House(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    currentLord = database.Column(database.Integer)
    founder = database.Column(database.Integer)
    heir = database.Column(database.Integer)
    cadetBranches = database.Column(database.ARRAY(database.String(80)))
    founded = database.Column(database.String(80))
    diedOut = database.Column(database.String(80))
    titles = database.Column(database.ARRAY(database.String(80)))
    coatOfArms = database.Column(database.String(80))
    words = database.Column(database.String(80))
    seats = database.Column(database.ARRAY(database.String(80)))
    overlord = database.Column(database.Integer)
    name = database.Column(database.String(80))
    swornMembers = database.Column(database.ARRAY(database.Integer))
    region = database.Column(database.String(80))
    ancestralWeapons = database.Column(database.ARRAY(database.String(80)))

    def __init__(self, currentLord, founder, heir, cadetBranches, founded, diedOut, titles, coatOfArms, words, seats, overlord, name, swornMembers, region, ancestralWeapons):
        self.currentLord = currentLord
        self.founder = founder
        self.heir = heir
        self.cadetBranches = cadetBranches
        self.founded = founded
        self.diedOut = diedOut
        self.titles = titles
        self.coatOfArms = coatOfArms
        self.words = words
        self.seats = seats
        self.overlord = overlord
        self.name = name
        self.swornMembers = swornMembers
        self.region = region
        self.ancestralWeapons = ancestralWeapons

# Foreign key relationships are alternative for headLeader, members, 
# weapons, seats (need consult for IDB2)


class Alliances(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    headLeader = database.Column(database.Integer)
    members = database.Column(database.ARRAY(database.Integer))
    weapons = database.Column(database.ARRAY(database.String(80)))
    seats = database.Column(database.ARRAY(database.String(80)))
    regions = database.Column(database.ARRAY(database.String(80)))
    cultures = database.Column(database.ARRAY(database.String(80)))

    def __init__(self, headLeader, members, weapons, seats, regions, cultures):
        self.headLeader = headLeader
        self.members = members
        self.weapons = weapons
        self.seats = seats
        self.regions = regions
        self.cultures = cultures