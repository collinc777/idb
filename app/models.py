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
import json

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
alliance_houses_assocation_table = Table(
    'alliance_houses_assocation', database.metadata,
    Column('alliance_id', Integer, ForeignKey('alliance.id')),
    Column('house_id', Integer, ForeignKey('house.id'))
)

houses_characters_association_table = Table(
    'houses_characters_association', database.metadata,
    Column('house_id', Integer, ForeignKey('house.id')),
    Column('character_id', Integer, ForeignKey('character.id'))
)

houses_alliances_association_table = Table(
    'houses_alliances_association_table', database.metadata,
    Column('house_id', Integer, ForeignKey('house.id')),
    Column('alliance_id', Integer, ForeignKey('alliance.id'))
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

    def __init__(self, id, numberOfPages, isbn, name, publisher, country, povCharacter_ids, author, mediaType, released,
                 character_ids):
        assert isinstance(id, int)
        assert isinstance(numberOfPages, int)
        assert numberOfPages > 0
        assert isinstance(isbn, six.string_types)
        assert isinstance(name, six.string_types)
        assert isinstance(publisher, six.string_types)
        assert isinstance(country, six.string_types)
        assert isinstance(author, six.string_types)
        assert isinstance(mediaType, six.string_types)
        assert hasattr(povCharacter_ids, '__iter__')
        assert hasattr(character_ids, '__iter__')

        self.id = id
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
        return json.dumps({c.name: getattr(self, c.name) for c in self.__table__.columns})


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

    house_id = Column(Integer)
    house = database.relationship(
        "House",
        secondary=houses_characters_association_table,
        back_populates="swornMembers")

    # Attributes
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
    imageLink = Column(database.String(160))

    def __init__(self, id, house_id, culture, titles, spouse, died, aliases, dateOfDeath, name, born, gender, father,
                 allegiances, alliance_ids, povBooks, playedBy, book_ids, tvSeries, mother, male, imageLink):
        assert isinstance(house_id, int)
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

        self.id = id
        self.house_id = house_id
        self.culture = culture
        self.titles = titles
        self.spouse = spouse
        self.died = died
        self.aliases = aliases
        if (dateOfDeath != False):
            self.dateOfDeath = True
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
        self.imageLink = imageLink

    def toJSON(self):
        return json.dumps({c.name: getattr(self, c.name) for c in self.__table__.columns})


class House(database.Model):
    __tablename__ = 'house'
    id = Column(Integer, primary_key=True)

    # Many-to-One Relationships
    # TODO: Greg 4/4/2017 Re-make ids as ForeignKeys once all keys are present in characters table
    #currentLord_id = Column(Integer, ForeignKey('character.id'), nullable=True)
    #currentLord_id = Column(Integer, nullable=True)
    #currentLord = database.relationship("Character", foreign_keys=[currentLord_id])
    #founder_id = Column(Integer, ForeignKey('character.id'))
    #founder = database.relationship("Character", foreign_keys=[founder_id])
    #heir_id = Column(Integer, ForeignKey('character.id'), nullable=True)
    #heir_id = Column(Integer, nullable=True)
    #heir = database.relationship("Character", foreign_keys=[heir_id])
    #overlord_id = Column(Integer, ForeignKey('character.id'), nullable=True)
    #overlord_id = Column(Integer, nullable=True)
    #overlord = database.relationship("Character", foreign_keys=[overlord_id])

    currentLord_id = Column(Integer, ForeignKey('character.id'))
    currentLord = database.relationship("Character",
                                        foreign_keys=[currentLord_id])

    heir_id = Column(Integer, ForeignKey('character.id'))
    heir = database.relationship("Character", foreign_keys=[heir_id])

    overlord_id = Column(Integer, ForeignKey('character.id'))
    overlord = database.relationship("Character", foreign_keys=[overlord_id])

    # Many-to-Many Relationships
    swornMember_ids = Column(database.ARRAY(Integer))
    swornMembers = database.relationship(
        "Character",
        secondary=house_swornMembers_association_table,
        back_populates="swornHouses")

    alliance_id = Column(Integer)
    alliance = database.relationship(
        "Alliance",
        secondary=houses_alliances_association_table,
        back_populates="swornHouses"
    )

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
    imageLink = Column(String(160))
    ancestralWeapons = Column(database.ARRAY(String(80)))

    def __init__(self, id, currentLord_id, heir_id, cadetBranches, founded, diedOut, titles, coatOfArms, words,
                 seats, overlord_id, name, swornMember_ids, alliance_id, region, ancestralWeapons, imageLink):
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

        self.id = id
        self.currentLord_id = currentLord_id
        self.heir_id = heir_id
        self.cadetBranches = cadetBranches
        self.founded = founded
        self.diedOut = diedOut
        self.titles = titles
        self.coatOfArms = coatOfArms
        self.words = words
        self.seats = seats
        self.overlord_id = overlord_id
        self.alliance_id = alliance_id
        self.name = name
        self.swornMember_ids = swornMember_ids
        self.region = region
        self.ancestralWeapons = ancestralWeapons
        self.imageLink = imageLink

    def toJSON(self):
        return json.dumps({c.name: getattr(self, c.name) for c in self.__table__.columns})


class Alliance(database.Model):
    __tablename__ = 'alliance'
    id = Column(Integer, primary_key=True)

    # Many-to-One Relationships
    headLeader_id = Column(Integer, ForeignKey('character.id'))
    headLeader = database.relationship("Character",
                                       foreign_keys=[headLeader_id])
    headHouse_id = Column(Integer, ForeignKey('house.id'))
    headHouse = database.relation("House", foreign_keys=[headHouse_id])

    # One-to-Many Relationships
    member_ids = Column(database.ARRAY(Integer))
    members = database.relationship(
        "Character",
        secondary=alliance_members_association_table,
        back_populates="alliances")

    swornHouse_ids = Column(database.ARRAY(Integer))
    swornHouses = database.relationship(
        "House",
        secondary=alliance_houses_assocation_table
    )

    # Attributes
    weapons = Column(database.ARRAY(String(80)))
    seats = Column(database.ARRAY(String(80)))
    regions = Column(database.ARRAY(String(80)))
    cultures = Column(database.ARRAY(String(80)))
    name = Column(database.String(80))
    imageLink = Column(database.String(160))

    def __init__(self, id, headLeader_id, member_ids, weapons, seats, regions, cultures, headHouse_id, imageLink, name):
        assert hasattr(member_ids, "__iter__")
        assert hasattr(weapons, "__iter__")
        assert hasattr(seats, "__iter__")
        assert hasattr(regions, "__iter__")
        assert hasattr(cultures, "__iter__")
        assert isinstance(id, int)

        self.id = id
        self.headLeader_id = headLeader_id
        self.member_ids = member_ids
        self.weapons = weapons
        self.seats = seats
        self.regions = regions
        self.cultures = cultures
        self.headHouse_id = headHouse_id
        self.name = name
        self.imageLink = imageLink

    def toJSON(self):
        return json.dumps({c.name: getattr(self, c.name) for c in self.__table__.columns})
