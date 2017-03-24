#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = too-many-public-methods
# pylint: disable = line-too-long
# pylint: disable = bad-continuation

# -------
# imports
# -------
import unittest
from unittest import main, TestCase
from app import database
from app import models
from app import views

# -----------
# TestModels
# -----------


class TestModels (TestCase):

    def setUp(self):
        # Perform database setup, nothing to do for Idatabase1
        pass

        # Taken from: http://kronosapiens.github.io/blog/2014/07/29/setting-up-unit-tests-with-flask.html
        # app.config.from_object('webapp.config.Testing')
        # database.session.close()
        # 3database.drop_all()
        # database.create_all()

    # -----
    # Book
    # -----

    def test_Book_numberOfPages(self):
        b = models.Book(
            694, "978-0553103540", "A Game of Thrones", "Bantam Books",
                        "United States", [148, 208, 232], "George R.R. Martin", "Hardcover", "1996", [2, 12, 13])
        self.assertEqual(b.numberOfPages, 694)

    def test_Book_isbn(self):
        b = models.Book(
            694, "978-0553103540", "A Game of Thrones", "Bantam Books",
                       "United States", [148, 208, 232], "George R.R. Martin", "Hardcover", "1996", [2, 12, 13])
        self.assertEqual(b.isbn, "978-0553103540")

    def test_Book_name(self):
        b = models.Book(
            694, "978-0553103540", "A Game of Thrones", "Bantam Books",
            "United States", [148, 208, 232], "George R.R. Martin", "Hardcover", "1996", [2, 12, 13])
        self.assertEqual(b.name, "A Game of Thrones")

    def test_Book_publisher(self):
        b = models.Book(
            694, "978-0553103540", "A Game of Thrones", "Bantam Books",
            "United States", [148, 208, 232], "George R.R. Martin", "Hardcover", "1996", [2, 12, 13])
        self.assertEqual(b.publisher, "Bantam Books")

    @unittest.skip("testing skipping")
    def test_Book_add(self):
        exampleBook = models.Book(
            694, "978-0553103540", "A Game of Thrones", "Bantam Books",
                        "United States", [148, 208, 232], "George R.R. Martin", "Hardcover", "1996", [2, 12, 13])

        database.session.add(exampleBook)
        database.session.commit()

        book = database.session.query(models.Book).filter_by(name="A Game of Thrones").first()
        self.assertEqual(book.numberOfPages, 694)
        self.assertEqual(book.isbn, "978-0553103540")

        database.session.delete(exampleBook)
        database.session.commit()

    # ----------
    # Character
    # ----------

    def test_Character_house(self):
        c = models.Character("Night's Watch", "", [], "", "", ["Sam"], False,
                             "Samwell Tarly", "", "Male", "", [], [], [], [], [], [], "", True)
        self.assertEqual(c.house, "Night's Watch")

    def test_Character_name(self):
        c = models.Character("Night's Watch", "", [], "", "", ["Sam"], False,
                             "Samwell Tarly", "", "Male", "", [], [], [], [], [], [], "", True)
        self.assertEqual(c.name, "Samwell Tarly")

    def test_Character_aliases(self):
        c = models.Character("Night's Watch", "", [], "", "", ["Sam"], False,
                             "Samwell Tarly", "", "Male", "", [], [], [], [], [], [], "", True)
        self.assertEqual(c.aliases, ["Sam"])

    def test_Character_titles_empty(self):
        c = models.Character("Night's Watch", "", [], "", "", ["Sam"], False,
                             "Samwell Tarly", "", "Male", "", [], [], [], [], [], [], "", True)
        self.assertEqual(c.titles, [])

    @unittest.skip("testing skipping")
    def test_Character_add(self):
        exampleCharacter = models.Character("Night's Watch", "", [], "", "", ["Sam"], False,
                             "Samwell Tarly", "", "Male", "", [], [], [], [], [], [], "", True)

        database.session.add(exampleCharacter)
        database.session.commit()

        character = database.session.query(models.Character).filter_by(name="Samwell Tarly").first()
        self.assertEqual(character.house, "Night's Watch")

        database.session.delete(exampleCharacter)
        database.session.commit()

    # -----
    # House
    # -----

    def test_House_currentLord_id(self):
        h = models.House(848, "", "", [], "", "", [],
                         "Three brass buckles, on a blue field(Azure, three buckles or)", "",
                         ["Bronzegate"], 17, "House Buckler of Bronzegate", [234, 848], "The Stormlands", [])
        self.assertEqual(h.currentLord_id, 848)

    def test_House_founder_id(self):
        h = models.House("", 1272, "", [], "", "", ["Ser"],
                         "Three dogs on a yellow field(Or, three dogs courant in pale sable)",
                         "", ["Clegane's Keep"], 229, "House Clegane",
                         [955, 1270, 1272, 1350, 1356, 1442, 1568, 1814, 1852, 1994, 2012], "The Westerlands", [])
        self.assertEqual(h.founder_id, 1272)

    def test_House_name(self):
        h = models.House("", 1272, "", [], "", "", ["Ser"],
                         "Three dogs on a yellow field(Or, three dogs courant in pale sable)",
                         "", ["Clegane's Keep"], 229, "House Clegane",
                         [955, 1270, 1272, 1350, 1356, 1442, 1568, 1814, 1852, 1994, 2012], "The Westerlands", [])
        self.assertEqual(h.name, "House Clegane")

    def test_House_swornMember_ids(self):
        h = models.House("", 1272, "", [], "", "", ["Ser"],
                         "Three dogs on a yellow field(Or, three dogs courant in pale sable)",
                         "", ["Clegane's Keep"], 229, "House Clegane",
                         [955, 1270, 1272, 1350, 1356, 1442, 1568, 1814, 1852, 1994, 2012], "The Westerlands", [])
        self.assertEqual(
            h.swornMember_ids, [955, 1270, 1272, 1350, 1356, 1442, 1568, 1814, 1852, 1994, 2012])

    @unittest.skip("RestAPI not implemented")
    def test_House_add(self):
        # exampleHouse = models.House(1, 2, 3, ["cadetBranches"], "founded", "diedOut", ["title"], "coatOfArms", "words", ["seats"], 4, "name", [5, 6], "region", ["ancestralWeapons"])
        exampleHouse = models.House("", 1272, "", [], "", "", ["Ser"],
                         "Three dogs on a yellow field(Or, three dogs courant in pale sable)",
                         "", ["Clegane's Keep"], 229, "House Clegane",
                         [955, 1270, 1272, 1350, 1356, 1442, 1568, 1814, 1852, 1994, 2012], "The Westerlands", [])

        database.session.add(exampleHouse)
        database.session.commit()

        house = database.session.query(models.House).filter_by(name="House Clegane").first()
        self.assertEqual(house.region, "The Westerlands")

        database.session.delete(exampleHouse)
        database.session.commit()

    # ---------
    # Alliance
    # ---------
    @unittest.skip("RestAPI not implemented")
    def test_Alliance_add(self):
        exampleAlliance = models.Alliance(1, [2, 3], ["weapons"], ["seats"], ["regions"], ["cultures"])
        
        database.session.add(exampleAlliance)
        database.session.commit()

        house = database.session.query(models.Alliance).filter_by(headLeader_id=1).first()
        self.assertEqual(house.weapons, ["weapons"])

        database.session.delete(exampleAlliance)
        database.session.commit()

# ----
# main
# ----

if __name__ == "__main__":
    main()
