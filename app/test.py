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
# TestCollatz
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
        b = models.Book(694, "978-0553103540", "A Game of Thrones", "Bantam Books", "United States", [148, 208, 232], "George R.R. Martin", "Hardcover", "1996", [2, 12, 13])
        self.assertEqual(b.numberOfPages, 694)

    # ----------
    # Character 
    # ----------

    def test_Character_house(self):
        c = models.Character("Night's Watch", "", [], "", "", ["Sam"], False, "Samwell Tarly", "", "Male", "", [], [], [], [], [], "", True)
        self.assertEqual(c.house, "Night's Watch")

# ----
# main
# ----

if __name__ == "__main__":
    main()
