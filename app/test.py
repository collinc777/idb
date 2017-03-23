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

from unittest import main, TestCase
from app import models

# -----------
# TestModels
# -----------

class TestModels (TestCase):

    def setUp(self):
        # Perform database setup, nothing to do for IDB1
        pass

        # Taken from: http://kronosapiens.github.io/blog/2014/07/29/setting-up-unit-tests-with-flask.html
        # app.config.from_object('webapp.config.Testing')
        # db.session.close()
        # 3db.drop_all()
        # db.create_all()

    # -----
    # Book 
    # -----

    def test_Book_numberOfPages(self):
        b = models.Book(694, "978-0553103540", "A Game of Thrones", "Bantam Books", \
            "United States", [148, 208, 232], "George R.R. Martin", "Hardcover", "1996", [2, 12, 13])
        self.assertEqual(b.numberOfPages, 694)

    def test_Book_isbn(self):
        b = models.Book(694, "978-0553103540", "A Game of Thrones", "Bantam Books", \
            "United States", [148, 208, 232], "George R.R. Martin", "Hardcover", "1996", [2, 12, 13])
        self.assertEqual(b.isbn, "978-0553103540")

    def test_Book_name(self):
        b = models.Book(694, "978-0553103540", "A Game of Thrones", "Bantam Books", \
            "United States", [148, 208, 232], "George R.R. Martin", "Hardcover", "1996", [2, 12, 13])
        self.assertEqual(b.name, "A Game of Thrones")

    def test_Book_publisher(self):
        b = models.Book(694, "978-0553103540", "A Game of Thrones", "Bantam Books", \
            "United States", [148, 208, 232], "George R.R. Martin", "Hardcover", "1996", [2, 12, 13])
        self.assertEqual(b.publisher, "Bantam Books")

    # ----------
    # Character 
    # ----------

    def test_Character_house(self):
        c = models.Character("Night's Watch", "", [], "", "", ["Sam"], False, \
            "Samwell Tarly", "", "Male", "", [], [], [], [], [], "", True)
        self.assertEqual(c.house, "Night's Watch")

    def test_Character_name(self):
        c = models.Character("Night's Watch", "", [], "", "", ["Sam"], False, \
            "Samwell Tarly", "", "Male", "", [], [], [], [], [], "", True)
        self.assertEqual(c.name, "Samwell Tarly")

    def test_Character_aliases(self):
        c = models.Character("Night's Watch", "", [], "", "", ["Sam"], False, \
            "Samwell Tarly", "", "Male", "", [], [], [], [], [], "", True)
        self.assertEqual(c.aliases, ["Sam"])

    def test_Character_titles_empty(self):
        c = models.Character("Night's Watch", "", [], "", "", ["Sam"], False, \
            "Samwell Tarly", "", "Male", "", [], [], [], [], [], "", True)
        self.assertEqual(c.titles, [])

    # -----
    # House 
    # -----

    def test_House_currentLord(self):
        h = models.House(848, "", "", [], "", "", [], \
            "Three brass buckles, on a blue field(Azure, three buckles or)", "", \
            ["Bronzegate"], 17, "House Buckler of Bronzegate", [234, 848], "The Stormlands", [])
        self.assertEqual(h.currentLord, 848)

    def test_House_founder(self):
        h = models.House("", 1272, "", [], "", "", ["Ser"], \
            "Three dogs on a yellow field(Or, three dogs courant in pale sable)", \
            "", ["Clegane's Keep"], 229, "House Clegane", \
            [955, 1270, 1272, 1350, 1356, 1442, 1568, 1814, 1852, 1994, 2012], "The Westerlands", [])
        self.assertEqual(h.founder, 1272)

    def test_House_name(self):
        h = models.House("", 1272, "", [], "", "", ["Ser"], \
            "Three dogs on a yellow field(Or, three dogs courant in pale sable)", \
            "", ["Clegane's Keep"], 229, "House Clegane", \
            [955, 1270, 1272, 1350, 1356, 1442, 1568, 1814, 1852, 1994, 2012], "The Westerlands", [])
        self.assertEqual(h.name, "House Clegane")

    def test_House_swornMembers(self):
        h = models.House("", 1272, "", [], "", "", ["Ser"], \
            "Three dogs on a yellow field(Or, three dogs courant in pale sable)", \
            "", ["Clegane's Keep"], 229, "House Clegane", \
            [955, 1270, 1272, 1350, 1356, 1442, 1568, 1814, 1852, 1994, 2012], "The Westerlands", [])
        self.assertEqual(h.swornMembers, [955, 1270, 1272, 1350, 1356, 1442, 1568, 1814, 1852, 1994, 2012])

# ----
# main
# ----

if __name__ == "__main__":
    main()
