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

import six
from sqlalchemy import Column, Integer, String, Table, ForeignKey

from app import database

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

# house_cadetBranches_association_table = Table(
#     'house_cadetBranches_association', database.metadata,
#     Column('founding_id', Integer, ForeignKey('house.id')),
#     Column('cadet_id', Integer, ForeignKey('house.id'))
# )

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
    'houses_alliances_association', database.metadata,
    Column('house_id', Integer, ForeignKey('house.id')),
    Column('alliance_id', Integer, ForeignKey('alliance.id'))
)

allegiances_houses_association_table = Table(
    'allegiances_houses_association', database.metadata,
    Column('character_id', Integer, ForeignKey('character.id')),
    Column('allegiances', Integer, ForeignKey('house.id'))
)


# -------
# Models
# -------


class Book(database.Model):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)

    # Many-to-Many Relationships
    povCharacter_ids = Column(database.ARRAY(Integer))
    # povCharacters = database.relationship(
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
    # povBook_ids = Column(database.ARRAY(Integer))
    # povBooks = database.relationship(
    #   "Book",
    #   secondary=books_povCharacters_association_table,
    #   back_populates="povCharacters")
    # Many-to-Many Relationships
    swornHouses_ids = Column(database.ARRAY(Integer))
    swornHouses = database.relationship(
        "House",
        secondary=house_swornMembers_association_table,
        back_populates="swornMembers")

    allegiances_ids = Column(database.ARRAY(Integer))
    allegiances = database.relationship("House",
                                        secondary=allegiances_houses_association_table)

    # Attributes
    culture = Column(String(80))
    titles = Column(database.ARRAY(String(300)))
    spouse_id = Column(Integer)
    died = Column(String(300))
    aliases = Column(database.ARRAY(String(300)))
    name = Column(String(80))
    born = Column(String(300))
    gender = Column(String(80))
    father_id = Column(Integer)
    playedBy = Column(database.ARRAY(String(80)))
    tvSeries = Column(database.ARRAY(String(300)))
    mother_id = Column(Integer)
    imageLink = Column(database.String(300))

    def __init__(self, id, culture, titles, spouse_id, died, aliases, name, born, gender, father_id,
                 allegiances_ids, povBook_ids, playedBy, book_ids, tvSeries, mother_id, imageLink):
        assert isinstance(culture, six.string_types)
        assert hasattr(titles, '__iter__')
        # assert isinstance(spouse_id, int)
        assert isinstance(died, six.string_types)
        assert hasattr(aliases, '__iter__')
        assert isinstance(died, six.string_types)
        assert isinstance(name, six.string_types)
        assert isinstance(born, six.string_types)
        assert isinstance(gender, six.string_types)
        # assert isinstance(father_id, int)
        # assert isinstance(mother_id, int)
        assert hasattr(allegiances_ids, '__iter__')
        assert hasattr(playedBy, '__iter__')
        assert hasattr(tvSeries, '__iter__')

        self.id = id
        self.culture = culture
        self.titles = titles
        self.spouse_id = spouse_id
        self.died = died
        self.aliases = aliases
        self.name = name
        self.born = born
        self.gender = gender
        self.father_id = father_id
        self.allegiances_ids = allegiances_ids
        self.povBook_ids = povBook_ids
        self.playedBy = playedBy
        self.book_ids = book_ids
        self.tvSeries = tvSeries
        self.mother_id = mother_id
        self.imageLink = imageLink


    @staticmethod
    def getSorts():
        return ["Name", "House", "Culture", "Gender"]

    @staticmethod
    def convertSort(sort):
        names = ["name", "swornHouses", "culture", "gender"]
        for i, s in enumerate(Book.getSorts()):
            if s == sort:
                return names[i]
        return None

    def toJSON(self):
        return json.dumps({c.name: getattr(self, c.name) for c in self.__table__.columns})


class House(database.Model):
    __tablename__ = 'house'
    id = Column(Integer, primary_key=True)

    # Many-to-One Relationships
    # TODO: Greg 4/4/2017 Re-make ids as ForeignKeys once all keys are present in characters table
    # currentLord_id = Column(Integer, ForeignKey('character.id'), nullable=True)
    # currentLord_id = Column(Integer, nullable=True)
    # currentLord = database.relationship("Character", foreign_keys=[currentLord_id])
    # founder_id = Column(Integer, ForeignKey('character.id'))
    # founder = database.relationship("Character", foreign_keys=[founder_id])
    # heir_id = Column(Integer, ForeignKey('character.id'), nullable=True)
    # heir_id = Column(Integer, nullable=True)
    # heir = database.relationship("Character", foreign_keys=[heir_id])
    # overlord_id = Column(Integer, ForeignKey('character.id'), nullable=True)
    # overlord_id = Column(Integer, nullable=True)
    # overlord = database.relationship("Character", foreign_keys=[overlord_id])

    currentLord_id = Column(Integer, ForeignKey('character.id'))
    currentLord = database.relationship("Character",
                                        foreign_keys=[currentLord_id])

    heir_id = Column(Integer, ForeignKey('character.id'))
    heir = database.relationship("Character", foreign_keys=[heir_id])

    overlord_id = Column(Integer)

    # Many-to-Many Relationships
    swornMember_ids = Column(database.ARRAY(Integer))
    swornMembers = database.relationship(
        "Character",
        secondary=house_swornMembers_association_table,
        back_populates="swornHouses")

    founder_id = Column(Integer, ForeignKey('character.id'))
    founder = database.relationship("Character", foreign_keys=[founder_id])

    alliance_id = Column(Integer)
    alliance = database.relationship(
        "Alliance",
        secondary=houses_alliances_association_table,
        back_populates="swornHouses"
    )

    # Attributes
    founded = Column(String(80))
    diedOut = Column(String(80))
    titles = Column(database.ARRAY(String(80)))
    coatOfArms = Column(String(500))
    words = Column(String(80))
    seats = Column(database.ARRAY(String(80)))
    name = Column(String(80))
    region = Column(String(80))
    ancestralWeapons = Column(database.ARRAY(String(80)))

    def __init__(self, id, currentLord_id, heir_id, founded, founder_id, diedOut, titles, coatOfArms,
                 words,
                 seats, overlord_id, name, swornMember_ids, alliance_id, region, ancestralWeapons):
        # assert isinstance(founder_id, Integer)
        assert isinstance(diedOut, six.string_types)
        assert isinstance(founded, six.string_types)
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
        self.founder_id = founder_id
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

    @staticmethod
    def getSorts():
        return ["Name", "Region", "Coat of Arms", "Words"]

    @staticmethod
    def convertSort(sort):
        names = ["name", "region", "coatOfArms", "words"]
        for i, s in enumerate(Book.getSorts()):
            if s == sort:
                return names[i]
        return None

    def toJSON(self):
        return json.dumps({c.name: getattr(self, c.name) for c in self.__table__.columns})


class Alliance(database.Model):
    __tablename__ = 'alliance'
    id = Column(Integer, primary_key=True)

    # Many-to-One Relationships
    currentLord_id = Column(Integer, ForeignKey('character.id'))
    currentLord = database.relationship("Character",
                                        foreign_keys=[currentLord_id])
    headHouse_id = Column(Integer, ForeignKey('house.id'))
    headHouse = database.relation("House", foreign_keys=[headHouse_id])

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
    imageLink = Column(database.String(300))

    def __init__(self, id, currentLord_id, ancestralWeapons, seats, swornHouse_ids, regions, cultures, headHouse_id,
                 name,
                 imageLink):
        assert hasattr(ancestralWeapons, "__iter__")
        assert hasattr(seats, "__iter__")
        assert hasattr(regions, "__iter__")
        assert hasattr(cultures, "__iter__")
        assert hasattr(swornHouse_ids, "__iter__")
        assert isinstance(imageLink, six.string_types)
        assert isinstance(id, int)

        self.id = id
        self.currentLord_id = currentLord_id
        self.ancestralWeapons = ancestralWeapons
        self.seats = seats
        self.regions = regions
        self.cultures = cultures
        self.headHouse_id = headHouse_id
        self.name = name
        self.swornHouse_ids = swornHouse_ids
        self.imageLink = imageLink

    @staticmethod
    def getSorts():
        return ["Name", "Current Head House", "Number of Members"]

    @staticmethod
    def convertSort(sort):
        names = ["name", "headHouse_id", "cultures", "seats"]
        for i, s in enumerate(Book.getSorts()):
            if s == sort:
                return names[i]
        return None

    def toJSON(self):
        return json.dumps({c.name: getattr(self, c.name) for c in self.__table__.columns})
