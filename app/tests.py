#!/usr/bin/env python3

# How to run: from main directory (idb) run 'python -m app.tests'
# How to coverage: coverage run -m app.tests (need to fix ImportError)

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
from app import database
from app import models

# -----------
# TestModels
# -----------


class TestModels(TestCase):
    def setUp(self):
        # Perform database setup
        database.session.close()

        self.bookParameters = {
            "numberOfPages": 694,
            "character_ids": [2, 12, 13, 16, 20, 27, 31, 38, 39, 40, 41, 42, 46, 54, 56, 57, 60, 61, 62, 66, 67, 69, 79,
                              89, 107, 115, 116, 120, 125, 128, 129, 130, 135, 137, 142, 147, 149, 150, 151, 160, 164,
                              168, 171, 181, 190, 194, 198, 202, 203, 206, 209, 211, 213, 217, 220, 223, 225, 235, 238,
                              245, 259, 264, 273, 274, 291, 292, 293, 294, 303, 306, 313, 315, 325, 326, 327, 338, 346,
                              347, 348, 361, 368, 377, 379, 380, 384, 385, 393, 394, 397, 400, 401, 405, 408, 413, 415,
                              418, 421, 427, 435, 439, 458, 461, 463, 466, 467, 475, 476, 484, 487, 490, 494, 496, 498,
                              501, 503, 506, 508, 519, 521, 526, 527, 529, 531, 532, 533, 535, 536, 539, 547, 557, 558,
                              562, 565, 572, 584, 585, 586, 588, 595, 600, 604, 605, 613, 615, 622, 631, 632, 635, 640,
                              649, 650, 651, 672, 677, 688, 691, 692, 694, 695, 701, 709, 714, 718, 721, 724, 725, 731,
                              734, 749, 751, 752, 754, 755, 759, 766, 768, 775, 778, 779, 782, 784, 786, 797, 805, 806,
                              814, 815, 820, 823, 827, 828, 829, 832, 837, 844, 850, 852, 860, 862, 867, 869, 876, 884,
                              886, 887, 891, 892, 894, 901, 903, 909, 912, 913, 916, 933, 945, 955, 969, 972, 975, 983,
                              984, 994, 1010, 1017, 1022, 1023, 1025, 1029, 1033, 1034, 1043, 1044, 1049, 1051, 1055,
                              1063, 1068, 1069, 1072, 1074, 1076, 1077, 1079, 1080, 1089, 1090, 1091, 1093, 1096, 1104,
                              1106, 1107, 1110, 1113, 1114, 1116, 1120, 1122, 1124, 1131, 1132, 1140, 1142, 1147, 1152,
                              1158, 1165, 1166, 1178, 1188, 1193, 1214, 1219, 1228, 1245, 1247, 1253, 1260, 1262, 1265,
                              1266, 1267, 1268, 1269, 1275, 1277, 1278, 1280, 1282, 1284, 1289, 1296, 1299, 1304, 1317,
                              1326, 1333, 1335, 1336, 1340, 1346, 1352, 1355, 1373, 1383, 1389, 1396, 1409, 1410, 1418,
                              1430, 1434, 1442, 1444, 1453, 1455, 1456, 1463, 1466, 1468, 1470, 1488, 1499, 1502, 1515,
                              1520, 1523, 1526, 1529, 1530, 1531, 1540, 1547, 1548, 1549, 1551, 1559, 1560, 1565, 1566,
                              1568, 1570, 1573, 1585, 1596, 1602, 1620, 1624, 1627, 1631, 1649, 1650, 1660, 1662, 1665,
                              1666, 1670, 1674, 1675, 1677, 1682, 1697, 1706, 1708, 1710, 1713, 1715, 1717, 1721, 1724,
                              1725, 1727, 1741, 1742, 1749, 1755, 1770, 1772, 1787, 1790, 1802, 1815, 1816, 1826, 1837,
                              1838, 1840, 1843, 1855, 1856, 1861, 1873, 1874, 1875, 1880, 1882, 1900, 1909, 1911, 1916,
                              1935, 1938, 1939, 1942, 1963, 1968, 1976, 1979, 1997, 2002, 2008, 2009, 2013, 2014, 2020,
                              2025, 2029, 2044, 2045, 2047, 2051, 2059, 2067, 2068, 2069, 2071, 2073, 2076, 2089, 2114,
                              2119, 2121],
            "povCharacter_ids": [148, 208, 232, 339, 583, 957, 1052, 1109, 1303],
            "publisher": "Bantam Books",
            "mediaType": "Hardcover",
            "released": "1996-08-01T00:00:00",
            "isbn": "978-0553103540",
            "country": "United States",
            "author": "George R. R. Martin",
            "id": 1,
            "name": "A Game of Thrones"
        }

        self.characterParameters = {
            "aliases": ["The Hound", "Dog"],
            "allegiances_ids": [72, 229],
            "book_ids": [1, 2, 3, 5, 8],
            "born": "In 270 AC or 271 AC",
            "culture": "",
            "died": "In 300 AC (supposedly)",
            "father_id": None,
            "gender": "Male",
            "id": 955,
            "imageLink": "Sandor_Clegane.jpeg",
            "mother_id": None,
            "name": "Sandor Clegane",
            "playedBy": ["Rory McCann"],
            "povBook_ids": [],
            "spouse_id": None,
            "titles": [],
            "tvSeries": ["Season 1", "Season 2", "Season 3", "Season 4", "Season 6"]
        }

        self.houseParameters = {
            "titles": ["King of Mountain and Vale (formerly)", "Lord of the Eyrie", "Defender of the Vale",
                       "Warden of the East"],
            "founded": "Coming of the Andals",
            "seats": ["The Eyrie (summer)", "Gates of the Moon (winter)"],
            "region": "The Vale",
            "ancestralWeapons": [],
            "coatOfArms": "A sky-blue falcon soaring against a white moon, on a sky-blue field(Bleu celeste, upon a plate a falcon volant of the field)",
            "id": 7,
            "heir_id": 477,
            "founder_id": 144,
            "currentLord_id": 894,
            "swornMember_ids": [49, 92, 93, 107, 223, 265, 300, 356, 477, 508, 540, 548, 558, 572, 688, 894, 1068, 1193,
                                1280, 1443, 1655, 1693, 1715, 1884],
            "diedOut": "",
            "words": "As High as Honor",
            "alliance_id": None,
            "name": "House Arryn of the Eyrie",
            "overlord_id": 16
        }

        self.allianceParameters = {
            "name": "The Wardens of the North",
            "ancestralWeapons" : ["Long Claw", "Ice"],
            "seats" : ["Winterfell"],
            "cultures" : ["Northman"],
            "regions" : ["North"],
            "id" : 1,
            "headHouse_id": 362,
            "currentLord_id" : 583,
            "swornHouse_ids" : [362, 216, 318, 395, 401, 271, 282, 150, 236, 435, 61],
            "imageLink": "alliancebanners/North.png"
        }

    # -----
    # Book
    # -----

    def test_Book_numberOfPages(self):
        b = models.Book(**self.bookParameters)
        self.assertEqual(b.numberOfPages, 694)

    def test_Book_isbn(self):
        b = models.Book(**self.bookParameters)
        self.assertEqual(b.isbn, self.bookParameters['isbn'])

    def test_Book_name(self):
        b = models.Book(**self.bookParameters)
        self.assertEqual(b.name, "A Game of Thrones")

    def test_Book_publisher(self):
        b = models.Book(**self.bookParameters)
        self.assertEqual(b.publisher, "Bantam Books")

    def test_Book_toDict(self):
        instance = models.Book(**self.bookParameters)
        self.assertGreater(len(instance.toDict()), 0)

    def test_Book_database_query(self):
        # Assumes existence of at least one element in model table.
        queryResult = database.session.query(models.Book).first()
        self.assertNotEqual(queryResult.name, None)

        database.session.rollback()

    def test_Book_database_add(self):
        # Note: Test will fail if a instance already exists with the given id
        testId = 999999
        testName = 'test_Book_database_add'
        self.bookParameters['name'] = testName
        self.bookParameters['id'] = testId
        model = models.Book
        instance = model(**self.bookParameters)

        database.session.add(instance)
        queryResult = database.session.query(model).filter_by(name=testName).first()
        self.assertEqual(queryResult.name, testName)

        database.session.rollback()

    # ----------
    # Character
    # ----------

    def test_Character_house(self):
        c = models.Character(**self.characterParameters)
        self.assertEqual(c.aliases[0], "The Hound")

    def test_Character_name(self):
        c = models.Character(**self.characterParameters)
        self.assertEqual(c.name, "Sandor Clegane")

    def test_Character_aliases(self):
        c = models.Character(**self.characterParameters)
        self.assertEqual(c.aliases[1], "Dog")

    def test_Character_titles(self):
        c = models.Character(**self.characterParameters)
        self.assertEqual(c.titles, [])

    def test_Character_toDict(self):
        instance = models.Character(**self.characterParameters)
        self.assertGreater(len(instance.toDict()), 0)

    def test_Character_database_add(self):
        # Note: Test will fail if a instance already exists with the given id
        testId = 999999
        testName = 'test_Character_database_add'
        self.characterParameters['name'] = testName
        self.characterParameters['id'] = testId
        model = models.Character
        instance = model(**self.characterParameters)

        database.session.add(instance)
        queryResult = database.session.query(model).filter_by(name=testName).first()
        self.assertEqual(queryResult.name, testName)

        database.session.rollback()

    # -----
    # House
    # -----

    def test_House_currentLord_id(self):
        h = models.House(**self.houseParameters)
        self.assertEqual(h.currentLord_id, 894)

    def test_House_founder_id(self):
        h = models.House(**self.houseParameters)
        self.assertEqual(h.founder_id, 144)

    def test_House_name(self):
        h = models.House(**self.houseParameters)
        self.assertEqual(h.name, "House Arryn of the Eyrie")

    def test_House_swornMember_ids(self):
        h = models.House(**self.houseParameters)
        self.assertEqual(
            h.swornMember_ids, [49, 92, 93, 107, 223, 265, 300, 356, 477, 508, 540, 548, 558, 572, 688, 894, 1068, 1193,
                                1280, 1443, 1655, 1693, 1715, 1884])

    def test_House_toDict(self):
        instance = models.House(**self.houseParameters)
        self.assertGreater(len(instance.toDict()), 0)

    def test_House_database_add(self):
        # Note: Test will fail if a instance already exists with the given id
        testId = 999999
        testName = 'test_House_database_add'
        self.houseParameters['name'] = testName
        self.houseParameters['id'] = testId
        model = models.House
        instance = model(**self.houseParameters)

        database.session.add(instance)
        queryResult = database.session.query(model).filter_by(name=testName).first()
        self.assertEqual(queryResult.name, testName)

        database.session.rollback()

    # ---------
    # Alliance
    # ---------

    def test_Alliance_id(self):
        a = models.Alliance(**self.allianceParameters)
        self.assertEqual(a.id, 1)

    def test_Alliance_name(self):
        a = models.Alliance(**self.allianceParameters)
        self.assertEqual(a.name, 'The Wardens of the North')

    def test_Alliance_seats(self):
        a = models.Alliance(**self.allianceParameters)
        self.assertEqual(a.seats, ["Winterfell"])

    def test_Alliance_toDict(self):
        instance = models.Alliance(**self.allianceParameters)
        self.assertGreater(len(instance.toDict()), 0)

    def test_Alliance_database_add(self):
        # Note: Test will fail if a instance already exists with the given id
        testId = 999999
        testName = 'test_Alliance_database_add'
        self.allianceParameters['name'] = testName
        self.allianceParameters['id'] = testId
        model = models.Alliance
        instance = model(**self.allianceParameters)

        database.session.add(instance)
        queryResult = database.session.query(model).filter_by(name=testName).first()
        self.assertEqual(queryResult.name, testName)

        database.session.rollback()

    def test_Alliance_database_delete(self):
        # Note: Test will fail if a instance already exists with the given id
        testId = 999999
        testName = 'test_Alliance_database_delete'
        self.allianceParameters['name'] = testName
        self.allianceParameters['id'] = testId
        model = models.Alliance
        instance = model(**self.allianceParameters)

        database.session.add(instance)
        queryResult = database.session.query(model).filter_by(name=testName).first()
        self.assertNotEqual(queryResult, None)

        database.session.delete(queryResult)
        queryResult = database.session.query(model).filter_by(name=testName).first()
        self.assertEqual(queryResult, None)

        database.session.rollback()

# ----
# main
# ----

if __name__ == "__main__":
    main()
