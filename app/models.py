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

Base = declarative_base()

# -------------------
# Association Tables
# -------------------

books_characters_association_table = Table(
    'books_characters_association', Base.metadata,
                                          Column(
                                              'book_id', Integer, ForeignKey('book.id')),
    Column('character_id', Integer, ForeignKey('character.id'))
)

books_povCharacters_association_table = Table(
    'books_povCharacters_association', Base.metadata,
    Column('book_id', Integer, ForeignKey('book.id')),
    Column('povCharacter_id', Integer, ForeignKey('character.id'))
)

house_swornMembers_association_table = Table(
    'house_swornMembers_association', Base.metadata,
    Column('house_id', Integer, ForeignKey('house.id')),
    Column('character_id', Integer, ForeignKey('character.id'))
)

alliance_members_association_table = Table(
    'alliance_members_association', Base.metadata,
    Column('alliance_id', Integer, ForeignKey('alliance.id')),
    Column('character_id', Integer, ForeignKey('character.id'))
)

# -------
# Models
# -------


class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)

    # Many-to-Many Relationships
    povCharacter_ids = Column(database.ARRAY(Integer))
    povCharacters = database.relationship(
        "Character",
        secondary=books_povCharacters_association_table,
        back_populates="povBooks")
    character_ids = Column(database.ARRAY(Integer))
    characters = database.relationship(
        "Character",
        secondary=books_characters_association_table,
        back_populates="books")

    # Attributes
    numberOfPages = Column(Integer)
    isbn = Column(String(13))
    name = Column(String(80))
    publisher = Column(String(80))
    country = Column(String(80))
    author = Column(String(80))
    mediaType = Column(String(80))
    released = Column(String(80))

    def __init__(self, numberOfPages, isbn, name, publisher, country, povCharacter_ids, author, mediaType, released, character_ids):
        assert numberOfPages > 0
        assert len(isbn) > 0
        assert len(name) > 0
        assert len(publisher) > 0
        assert len(country) > 0
        assert len(author) > 0
        assert len(mediaType) > 0
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


class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)

    # Many-to-Many Relationships
    book_ids = Column(database.ARRAY(Integer))
    books = database.relationship(
        "Book",
        secondary=books_characters_association_table,
        back_populates="characters")
    povBook_ids = Column(database.ARRAY(Integer))
    povBooks = database.relationship(
        "Book",
        secondary=books_povCharacters_association_table,
        back_populates="povCharacters")
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

    def __init__(self, house, culture, titles, spouse, died, aliases, dateOfDeath, name, born, gender, father, allegiances, alliance_ids, povBook_ids, playedBy, book_ids, tvSeries, mother, male):
        assert isinstance(house, basestring)
        assert isinstance(culture, basestring)
        assert hasattr(titles, '__iter__')
        assert isinstance(spouse, basestring)
        assert isinstance(died, basestring)
        assert hasattr(aliases, '__iter__')
        assert isinstance(died, basestring)
        assert isinstance(name, basestring)
        assert isinstance(born, basestring)
        assert isinstance(gender, basestring)
        assert isinstance(father, basestring)
        assert isinstance(mother, basestring)
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
        self.povBook_ids = povBook_ids
        self.playedBy = playedBy
        self.book_ids = book_ids
        self.tvSeries = tvSeries
        self.mother = mother
        self.male = male


class House(Base):
    __tablename__ = 'house'
    id = Column(Integer, primary_key=True)

    # Many-to-One Relationships
    currentLord_id = Column(Integer, ForeignKey('character.id'))
    currentLord = database.relationship("Character",
                                        foreign_keys=[currentLord_id])
    founder_id = Column(Integer, ForeignKey('character.id'))
    founder = database.relationship("Character", foreign_keys=[founder_id])
    heir_id = Column(Integer, ForeignKey('character.id'))
    heir = database.relationship("Character", foreign_keys=[heir_id])
    overlord_id = Column(Integer, ForeignKey('character.id'))
    overlord = database.relationship("Character", foreign_keys=[overlord_id])

    # One-to-Many Relationships
    swornMember_ids = Column(database.ARRAY(Integer))
    swornMembers = database.relationship(
        "Character",
        secondary=house_swornMembers_association_table)

    # Attributes
    cadetBranches = Column(database.ARRAY(String(80)))
    founded = Column(String(80))
    diedOut = Column(String(80))
    titles = Column(database.ARRAY(String(80)))
    coatOfArms = Column(String(80))
    words = Column(String(80))
    seats = Column(database.ARRAY(String(80)))
    overlord = Column(Integer)
    name = Column(String(80))
    region = Column(String(80))
    ancestralWeapons = Column(database.ARRAY(String(80)))

    def __init__(self, currentLord_id, founder_id, heir_id, cadetBranches, founded, diedOut, titles, coatOfArms, words, seats, overlord_id, name, swornMember_ids, region, ancestralWeapons):
        assert hasattr(cadetBranches, '__iter__')
        assert isinstance(founded, basestring)
        assert isinstance(diedOut, basestring)
        assert hasattr(titles, '__iter__')
        assert isinstance(coatOfArms, basestring)
        assert isinstance(words, basestring)
        assert hasattr(seats, '__iter__')
        assert isinstance(name, basestring)
        assert isinstance(region, basestring)
        assert hasattr(swornMember_ids, '__iter__')
        assert hasattr(ancestralWeapons, '__iter__')

        self.currentLord_id = currentLord_id
        self.founder_id = founder_id
        self.heir_id = heir_id
        self.cadetBranches = cadetBranches
        self.founded = founded
        self.diedOut = diedOut
        self.titles = titles
        self.coatOfArms = coatOfArms
        self.words = words
        self.seats = seats
        self.overlord_id = overlord_id
        self.name = name
        self.swornMember_ids = swornMember_ids
        self.region = region
        self.ancestralWeapons = ancestralWeapons


class Alliance(Base):
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
