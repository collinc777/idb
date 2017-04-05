#!/usr/bin/env python3

# See link: http://docs.sqlalchemy.org/en/latest/orm/join_conditions.html
# See link: http://flask-sqlalchemy.pocoo.org/2.1/models/

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

from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from app import database
import six

# -------------------
# Association Tables
# -------------------

books_characters_association_table = Table(
    'books_characters_association', database.metadata,
                                          Column(
                                              'book_id', Integer, ForeignKey('book.id')),
    Column('character_id', Integer, ForeignKey('character.id'))
)

books_povCharacters_association_table = Table(
    'books_povCharacters_association', database.metadata,
    Column('book_id', Integer, ForeignKey('book.id')),
    Column('povCharacter_id', Integer, ForeignKey('character.id'))
)

house_swornMembers_association_table = Table(
    'house_swornMembers_association', database.metadata,
    Column('house_id', Integer, ForeignKey('house.id')),
    Column('character_id', Integer, ForeignKey('character.id'))
)

alliance_members_association_table = Table(
    'alliance_members_association', database.metadata,
    Column('alliance_id', Integer, ForeignKey('alliance.id')),
    Column('character_id', Integer, ForeignKey('character.id'))
)

# -------
# Models
# -------


class Book(database.Model):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)

    # Many-to-Many Relationships
    povCharacter_ids = Column(database.ARRAY(Integer))
    #povCharacters = database.relationship(
    #    "Character",
    #   secondary=books_povCharacters_association_table,
    #   back_populates="povBooks")
    character_ids = Column(database.ARRAY(Integer))
    characters = database.relationship(
        "Character",
        secondary=books_characters_association_table,
        back_populates="books")

    # Attributes
    numberOfPages = Column(Integer)
    isbn = Column(String(14))
    name = Column(String(80))
    publisher = Column(String(80))
    country = Column(String(80))
    author = Column(String(80))
    mediaType = Column(String(80))
    released = Column(String(80))

    def __init__(self, numberOfPages, isbn, name, publisher, country, povCharacter_ids, author, mediaType, released, character_ids):
        assert numberOfPages > 0
        assert isinstance(isbn, six.string_types)
        assert isinstance(name, six.string_types)
        assert isinstance(publisher, six.string_types)
        assert isinstance(country, six.string_types)
        assert isinstance(author, six.string_types)
        assert isinstance(mediaType, six.string_types)
        assert hasattr(povCharacter_ids, '__iter__')
        assert hasattr(character_ids, '__iter__')

        self.numberOfPages = numberOfPages
        self.isbn = isbn
        self.name = name
        self.publisher = publisher
        self.country = country
        self.povCharacter_ids = povCharacter_ids
        self.author = author
        self.mediaType = mediaType
        self.released = released
        self.character_ids = character_ids

    @staticmethod
    def getSorts():
        return ["Name", "Author", "Publisher", "ISBN", "Number of Pages", "Release Date"]

    @staticmethod
    def convertSort(sort):
        names = ["name", "author", "publisher", "isbn", "numberOfPages", "released"]
        for i, s in enumerate(Book.getSorts()):
            if s == sort:
                return names[i]
        return None


    def toJSON(self):
        jsonString = '{'
        jsonString += '\"numberOfPages\":' + str(self.numberOfPages) + ','
        jsonString += '\"isbn\":\"' + self.isbn + '\",'
        jsonString += '\"name\":\"' + self.name + '\",'
        jsonString += '\"publisher\":\"' + self.publisher + '\",'
        jsonString += '\"country\":\"' + self.country + '\",'
        jsonString += '\"author\":\"' + self.author + '\",'
        jsonString += '\"mediaType\":\"' + self.mediaType + '\",'
        jsonString += '\"released\":\"' + self.released + '\",'

        if len(self.povCharacter_ids) > 0:
            jsonString += '\"povCharacters\":['
            for povCharacter_id in self.povCharacter_ids:
                jsonString += str(povCharacter_id) + ','
            jsonString = jsonString[0:-1] + ']'
        else:
            jsonString += '\"povCharacters\":[]'

        jsonString += ','
        if len(self.character_ids) > 0:
            jsonString += '\"characters\":['
            for character_id in self.character_ids:
                jsonString += str(character_id) + ','
            jsonString = jsonString[0:-1] + ']'
        else:
            jsonString += '\"characters\":[]'
        
        jsonString += '}'
        return jsonString

class Character(database.Model):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)

    # Many-to-Many Relationships
    book_ids = Column(database.ARRAY(Integer))
    books = database.relationship(
        "Book",
        secondary=books_characters_association_table,
        back_populates="characters")
    # TODO: Greg 4/4/2017 Re-add povBook ids when issue #52 is resolved
    #povBook_ids = Column(database.ARRAY(Integer))
    #povBooks = database.relationship(
    #   "Book",
    #   secondary=books_povCharacters_association_table,
    #   back_populates="povCharacters")
    # Many-to-Many Relationships
    swornHouses_ids = Column(database.ARRAY(Integer))
    swornHouses = database.relationship(
        "House",
        secondary=house_swornMembers_association_table,
        back_populates="swornMembers")
    alliance_ids = Column(database.ARRAY(Integer))
    alliances = database.relationship(
        "Alliance",
        secondary=alliance_members_association_table,
        back_populates="members")

    # Attributes
    house = Column(String(80))
    culture = Column(String(80))
    titles = Column(database.ARRAY(String))
    spouse = Column(String(80))
    died = Column(String(80))
    aliases = Column(database.ARRAY(String))
    dateOfDeath = Column(database.Boolean)
    name = Column(String(80))
    born = Column(String(80))
    gender = Column(String(80))
    father = Column(String(80))
    allegiances = Column(database.ARRAY(String(80)))
    playedBy = Column(database.ARRAY(String(80)))
    tvSeries = Column(database.ARRAY(String(80)))
    mother = Column(String(80))
    male = Column(database.Boolean)
    povBooks = Column(database.ARRAY(String(80)))

    def __init__(self, house, culture, titles, spouse, died, aliases, dateOfDeath, name, born, gender, father, allegiances, alliance_ids, povBooks, playedBy, book_ids, tvSeries, mother, male):
        assert isinstance(house, six.string_types)
        assert isinstance(culture, six.string_types)
        assert hasattr(titles, '__iter__')
        assert isinstance(spouse, six.string_types)
        assert isinstance(died, six.string_types)
        assert hasattr(aliases, '__iter__')
        assert isinstance(died, six.string_types)
        assert isinstance(name, six.string_types)
        assert isinstance(born, six.string_types)
        assert isinstance(gender, six.string_types)
        assert isinstance(father, six.string_types)
        assert isinstance(mother, six.string_types)
        assert hasattr(allegiances, '__iter__')
        assert hasattr(playedBy, '__iter__')
        assert hasattr(tvSeries, '__iter__')
        assert isinstance(male, bool)

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
        self.alliance_ids = alliance_ids
        self.povBooks = povBooks
        self.playedBy = playedBy
        self.book_ids = book_ids
        self.tvSeries = tvSeries
        self.mother = mother
        self.male = male

    def toJSON(self):
        jsonString = '{'
        jsonString += '\"name\":\"' + self.name + '\",'
        jsonString += '}'
        return jsonString


class House(database.Model):
    __tablename__ = 'house'
    id = Column(Integer, primary_key=True)

    # Many-to-One Relationships
    # TODO: Greg 4/4/2017 Re-make ids as ForeignKeys once all keys are present in characters table
    #currentLord_id = Column(Integer, ForeignKey('character.id'), nullable=True)
    currentLord_id = Column(Integer, nullable=True)
    #currentLord = database.relationship("Character", foreign_keys=[currentLord_id])
    #founder_id = Column(Integer, ForeignKey('character.id'))
    #founder = database.relationship("Character", foreign_keys=[founder_id])
    #heir_id = Column(Integer, ForeignKey('character.id'), nullable=True)
    heir_id = Column(Integer, nullable=True)
    #heir = database.relationship("Character", foreign_keys=[heir_id])
    #overlord_id = Column(Integer, ForeignKey('character.id'), nullable=True)
    overlord_id = Column(Integer, nullable=True)
    #overlord = database.relationship("Character", foreign_keys=[overlord_id])

    # Many-to-Many Relationships
    swornMember_ids = Column(database.ARRAY(Integer))
    swornMembers = database.relationship(
        "Character",
        secondary=house_swornMembers_association_table,
        back_populates="swornHouses")

    # Attributes
    founder = Column(String(80))
    cadetBranches = Column(database.ARRAY(String(80)))
    founded = Column(String(80))
    diedOut = Column(String(80))
    titles = Column(database.ARRAY(String(80)))
    coatOfArms = Column(String(512))
    words = Column(String(80))
    seats = Column(database.ARRAY(String(80)))
    name = Column(String(80))
    region = Column(String(80))
    ancestralWeapons = Column(database.ARRAY(String(80)))

    def __init__(self, currentLord_id, founder, heir_id, cadetBranches, founded, diedOut, titles, coatOfArms, words, seats, overlord_id, name, swornMember_ids, region, ancestralWeapons):
        assert hasattr(cadetBranches, '__iter__')
        assert isinstance(founded, six.string_types)
        assert isinstance(diedOut, six.string_types)
        assert hasattr(titles, '__iter__')
        assert isinstance(coatOfArms, six.string_types)
        assert isinstance(words, six.string_types)
        assert hasattr(seats, '__iter__')
        assert isinstance(name, six.string_types)
        assert isinstance(region, six.string_types)
        assert hasattr(swornMember_ids, '__iter__')
        assert hasattr(ancestralWeapons, '__iter__')

        self.currentLord_id = currentLord_id if not isinstance(currentLord_id, six.string_types) else None
        self.founder = founder
        self.heir_id = heir_id if not isinstance(heir_id, six.string_types) else None
        self.cadetBranches = cadetBranches
        self.founded = founded
        self.diedOut = diedOut
        self.titles = titles
        self.coatOfArms = coatOfArms
        self.words = words
        self.seats = seats
        self.overlord_id = overlord_id if not isinstance(overlord_id, six.string_types) else None
        self.name = name
        self.swornMember_ids = swornMember_ids
        self.region = region
        self.ancestralWeapons = ancestralWeapons


class Alliance(database.Model):
    __tablename__ = 'alliance'
    id = Column(Integer, primary_key=True)

    # Many-to-One Relationships
    headLeader_id = Column(Integer, ForeignKey('character.id'))
    headLeader = database.relationship("Character",
                                       foreign_keys=[headLeader_id])

    # One-to-Many Relationships
    member_ids = Column(database.ARRAY(Integer))
    members = database.relationship(
        "Character",
        secondary=alliance_members_association_table,
        back_populates="alliances")

    # Attributes
    weapons = Column(database.ARRAY(String(80)))
    seats = Column(database.ARRAY(String(80)))
    regions = Column(database.ARRAY(String(80)))
    cultures = Column(database.ARRAY(String(80)))

    def __init__(self, headLeader_id, member_ids, weapons, seats, regions, cultures):
        assert hasattr(member_ids, "__iter__")
        assert hasattr(weapons, "__iter__")
        assert hasattr(seats, "__iter__")
        assert hasattr(regions, "__iter__")
        assert hasattr(cultures, "__iter__")

        self.headLeader_id = headLeader_id
        self.member_ids = member_ids
        self.weapons = weapons
        self.seats = seats
        self.regions = regions
        self.cultures = cultures
