#!/usr/bin/env python3

# How to run: 'python -m app.tests'
# How to coverage: 'coverage run --source=app -m app.tests'

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
            "ancestralWeapons": ["Long Claw", "Ice"],
            "seats": ["Winterfell"],
            "cultures": ["Northman"],
            "regions": ["North"],
            "id": 1,
            "headHouse_id": 362,
            "currentLord_id": 583,
            "swornHouse_ids": [362, 216, 318, 395, 401, 271, 282, 150, 236, 435, 61],
            "imageLink": "alliancebanners/North.png"
        }

        self.bookParameters2 = {
            "country": "United States", 
            "character_ids": [2, 3, 7, 12, 13, 16, 20, 21, 27, 31, 35, 36, 37, 38, 39, 40, 41, 42, 46, 50, 51, 52, 53, 54, 
                    56, 58, 60, 62, 64, 67, 68, 69, 70, 71, 72, 73, 77, 78, 79, 80, 81, 82, 84, 85, 86, 87, 89, 94, 95, 96, 100, 105, 
                    108, 111, 112, 114, 115, 116, 117, 118, 120, 122, 123, 124, 125, 127, 130, 138, 141, 142, 145, 146, 147, 149, 151, 
                    153, 158, 159, 160, 161, 162, 164, 168, 169, 173, 175, 177, 179, 180, 181, 187, 188, 189, 190, 193, 194, 199, 200, 
                    202, 203, 204, 206, 214, 216, 217, 219, 222, 223, 225, 227, 228, 230, 234, 235, 237, 238, 245, 247, 250, 251, 252, 
                    254, 262, 263, 264, 267, 273, 274, 279, 280, 282, 285, 286, 288, 290, 291, 292, 294, 295, 296, 297, 298, 299, 300, 
                    303, 306, 308, 309, 310, 311, 312, 315, 320, 321, 322, 323, 325, 326, 327, 329, 330, 331, 332, 336, 337, 338, 339, 
                    341, 346, 347, 348, 352, 357, 360, 361, 362, 364, 365, 368, 369, 370, 372, 374, 375, 377, 379, 380, 381, 382, 383, 
                    385, 392, 393, 394, 397, 401, 404, 405, 406, 408, 411, 413, 415, 416, 417, 418, 421, 423, 424, 426, 434, 438, 439, 
                    442, 443, 448, 453, 458, 461, 462, 465, 470, 475, 476, 485, 486, 487, 490, 496, 498, 499, 500, 501, 502, 503, 504, 
                    506, 507, 511, 519, 521, 522, 523, 524, 526, 527, 530, 531, 532, 533, 534, 535, 536, 537, 539, 547, 549, 550, 553, 
                    555, 557, 559, 560, 561, 562, 563, 565, 571, 572, 574, 575, 576, 580, 585, 586, 587, 588, 590, 592, 595, 597, 599, 
                    600, 602, 603, 604, 605, 606, 607, 609, 613, 616, 617, 621, 622, 623, 624, 625, 626, 628, 629, 630, 631, 632, 635, 
                    636, 638, 639, 640, 647, 649, 650, 651, 657, 658, 659, 660, 662, 663, 664, 665, 666, 669, 670, 673, 674, 676, 677, 
                    678, 682, 683, 686, 688, 689, 690, 691, 692, 693, 694, 697, 699, 700, 701, 704, 708, 710, 711, 712, 713, 717, 718, 
                    720, 721, 722, 723, 725, 727, 730, 731, 735, 736, 738, 740, 741, 742, 743, 745, 746, 747, 748, 750, 752, 754, 755, 
                    756, 757, 761, 762, 764, 765, 766, 767, 768, 769, 770, 771, 772, 774, 775, 776, 778, 780, 781, 783, 784, 785, 786, 
                    788, 796, 799, 800, 801, 802, 803, 804, 805, 806, 808, 809, 811, 812, 814, 815, 817, 818, 819, 820, 822, 823, 824, 
                    825, 826, 827, 828, 829, 831, 832, 834, 837, 838, 844, 848, 849, 850, 851, 852, 854, 855, 856, 858, 860, 862, 863, 
                    866, 867, 869, 874, 876, 877, 882, 884, 887, 889, 890, 891, 892, 894, 896, 897, 899, 900, 901, 902, 903, 905, 909, 
                    912, 913, 914, 922, 923, 925, 927, 929, 930, 931, 932, 933, 937, 938, 940, 941, 944, 945, 946, 947, 948, 949, 950, 
                    952, 953, 955, 956, 959, 960, 961, 965, 966, 968, 972, 973, 974, 975, 976, 983, 984, 986, 989, 991, 992, 994, 995, 
                    996, 997, 998, 1000, 1004, 1006, 1008, 1009, 1010, 1011, 1013, 1014, 1017, 1019, 1020, 1022, 1024, 1025, 1027, 1029, 
                    1033, 1034, 1036, 1037, 1038, 1040, 1043, 1045, 1046, 1049, 1051, 1053, 1054, 1055, 1056, 1057, 1058, 1061, 1063, 
                    1068, 1072, 1073, 1074, 1075, 1077, 1079, 1080, 1081, 1082, 1083, 1084, 1085, 1086, 1087, 1088, 1089, 1090, 1091, 
                    1092, 1093, 1094, 1095, 1096, 1097, 1099, 1100, 1102, 1104, 1105, 1106, 1107, 1113, 1114, 1115, 1116, 1118, 1122, 
                    1124, 1125, 1127, 1131, 1132, 1134, 1135, 1136, 1137, 1139, 1142, 1144, 1145, 1146, 1147, 1151, 1155, 1157, 1158, 
                    1161, 1164, 1165, 1166, 1172, 1173, 1174, 1177, 1179, 1181, 1182, 1184, 1186, 1192, 1194, 1195, 1196, 1199, 1200, 
                    1201, 1205, 1213, 1216, 1217, 1220, 1221, 1222, 1223, 1224, 1227, 1231, 1233, 1234, 1237, 1240, 1244, 1246, 1250, 
                    1252, 1253, 1257, 1262, 1265, 1266, 1270, 1274, 1275, 1277, 1279, 1280, 1281, 1283, 1289, 1293, 1295, 1296, 1298, 
                    1301, 1305, 1310, 1311, 1314, 1315, 1316, 1317, 1320, 1321, 1323, 1325, 1331, 1334, 1335, 1337, 1341, 1342, 1346, 
                    1347, 1348, 1350, 1351, 1352, 1353, 1355, 1358, 1362, 1363, 1364, 1367, 1369, 1374, 1375, 1376, 1377, 1383, 1384, 
                    1385, 1390, 1393, 1396, 1401, 1404, 1409, 1410, 1411, 1412, 1413, 1417, 1418, 1419, 1420, 1425, 1426, 1427, 1428, 
                    1429, 1434, 1435, 1436, 1437, 1438, 1442, 1445, 1447, 1448, 1450, 1451, 1453, 1455, 1465, 1466, 1467, 1468, 1471, 
                    1472, 1474, 1475, 1479, 1481, 1487, 1488, 1494, 1495, 1497, 1502, 1507, 1508, 1515, 1518, 1519, 1520, 1522, 1523, 
                    1525, 1526, 1531, 1532, 1533, 1535, 1536, 1539, 1540, 1544, 1547, 1548, 1549, 1559, 1560, 1561, 1569, 1570, 1571, 
                    1574, 1575, 1576, 1577, 1578, 1580, 1581, 1584, 1587, 1594, 1599, 1603, 1604, 1606, 1607, 1612, 1613, 1615, 1616, 
                    1617, 1618, 1619, 1621, 1623, 1625, 1626, 1627, 1629, 1630, 1632, 1634, 1640, 1645, 1647, 1649, 1650, 1654, 1656, 
                    1657, 1658, 1659, 1660, 1666, 1667, 1669, 1670, 1674, 1675, 1676, 1678, 1681, 1682, 1683, 1684, 1685, 1688, 1692, 
                    1695, 1696, 1697, 1700, 1701, 1703, 1704, 1706, 1708, 1709, 1713, 1715, 1727, 1729, 1730, 1732, 1733, 1735, 1740, 
                    1741, 1742, 1747, 1749, 1754, 1755, 1759, 1761, 1762, 1764, 1766, 1768, 1769, 1770, 1774, 1776, 1777, 1778, 1781, 
                    1782, 1783, 1784, 1785, 1787, 1789, 1791, 1794, 1795, 1797, 1799, 1800, 1804, 1805, 1806, 1807, 1808, 1809, 1810, 
                    1811, 1814, 1815, 1821, 1824, 1825, 1826, 1827, 1828, 1830, 1839, 1843, 1847, 1848, 1852, 1854, 1856, 1860, 1861, 
                    1862, 1864, 1873, 1880, 1882, 1885, 1896, 1900, 1902, 1903, 1904, 1911, 1916, 1917, 1918, 1920, 1921, 1922, 1925, 
                    1926, 1930, 1931, 1932, 1933, 1934, 1935, 1938, 1939, 1940, 1941, 1943, 1947, 1951, 1952, 1954, 1955, 1957, 1959, 
                    1963, 1964, 1967, 1969, 1971, 1972, 1976, 1977, 1979, 1984, 1988, 1990, 1993, 1994, 1996, 2002, 2003, 2005, 2006, 
                    2007, 2009, 2010, 2013, 2014, 2016, 2017, 2018, 2020, 2022, 2024, 2027, 2031, 2032, 2035, 2038, 2041, 2044, 2045, 
                    2049, 2050, 2052, 2060, 2063, 2065, 2066, 2067, 2069, 2070, 2071, 2072, 2073, 2074, 2077, 2085, 2087, 2088, 2091, 
                    2092, 2093, 2097, 2098, 2099, 2100, 2109, 2120, 2121, 2122, 2126, 2131, 2134, 2137], 
            "povCharacter_ids": [148, 208, 232, 529, 583, 751, 957, 1052, 1267, 1303, 1319], 
            "author": "George R. R. Martin", 
            "name": "A Storm of Swords", 
            "released": "2000-10-31T00:00:00", 
            "id": 3, 
            "numberOfPages": 992, 
            "isbn": "978-0553106633", 
            "publisher": "Bantam Books", 
            "mediaType": "Hardcover"}

        self.bookParameters3 = {
            "country": "United Status", 
            "character_ids": [1, 2, 4, 5, 6, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 21, 22, 24, 25, 26, 27, 28, 31, 34, 36, 37, 38, 
                    39, 42, 46, 47, 52, 53, 54, 56, 62, 63, 66, 67, 68, 69, 70, 71, 73, 74, 77, 79, 81, 82, 84, 85, 86, 87, 88, 89, 
                    91, 92, 94, 95, 96, 99, 100, 102, 103, 106, 108, 111, 112, 114, 115, 116, 117, 118, 122, 123, 124, 125, 131, 
                    134, 135, 138, 141, 142, 145, 146, 147, 153, 158, 159, 160, 162, 163, 164, 166, 168, 169, 172, 173, 174, 175, 
                    176, 177, 179, 180, 181, 184, 185, 187, 188, 189, 190, 191, 194, 196, 199, 200, 201, 202, 203, 204, 205, 208, 
                    209, 214, 215, 217, 219, 221, 222, 223, 225, 227, 228, 232, 233, 235, 237, 241, 243, 244, 245, 246, 247, 250, 
                    251, 252, 260, 261, 262, 263, 264, 270, 273, 274, 276, 277, 278, 279, 280, 281, 282, 285, 286, 287, 288, 289, 
                    291, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 311, 312, 313, 314, 315, 
                    316, 318, 319, 320, 321, 323, 325, 326, 327, 329, 330, 331, 332, 336, 337, 338, 339, 341, 343, 344, 345, 346, 
                    348, 352, 355, 356, 357, 358, 359, 360, 361, 362, 364, 365, 367, 368, 369, 370, 372, 373, 375, 377, 378, 380, 
                    381, 382, 383, 385, 387, 390, 392, 393, 394, 396, 397, 398, 401, 402, 403, 404, 405, 406, 407, 408, 409, 411, 
                    413, 415, 416, 417, 418, 419, 420, 424, 426, 429, 430, 432, 433, 434, 436, 438, 439, 440, 441, 444, 445, 447, 
                    450, 451, 453, 454, 455, 456, 458, 459, 461, 462, 463, 466, 468, 469, 470, 472, 473, 474, 475, 476, 477, 482, 
                    483, 485, 486, 487, 490, 491, 493, 496, 498, 499, 500, 501, 502, 503, 504, 505, 506, 509, 510, 511, 512, 515, 
                    516, 517, 518, 519, 520, 521, 522, 523, 524, 526, 528, 530, 531, 532, 533, 535, 539, 540, 541, 542, 545, 547, 
                    549, 550, 551, 552, 553, 555, 557, 561, 562, 563, 564, 565, 571, 572, 573, 574, 575, 576, 578, 579, 580, 582, 
                    583, 585, 586, 587, 588, 590, 592, 594, 597, 600, 601, 602, 604, 605, 606, 609, 612, 613, 616, 617, 619, 620, 
                    621, 622, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 645, 647, 649, 
                    651, 652, 653, 654, 658, 659, 660, 661, 662, 663, 665, 666, 667, 669, 670, 673, 674, 676, 677, 678, 681, 682, 
                    686, 687, 688, 689, 690, 691, 692, 693, 700, 705, 706, 707, 708, 709, 710, 711, 712, 713, 715, 718, 719, 720, 
                    721, 723, 725, 726, 727, 730, 731, 735, 736, 738, 739, 740, 741, 742, 743, 745, 746, 747, 748, 750, 751, 752, 
                    753, 754, 757, 760, 762, 763, 764, 765, 766, 768, 769, 770, 771, 774, 775, 776, 778, 780, 781, 782, 783, 784, 
                    785, 786, 787, 788, 789, 790, 793, 796, 798, 799, 800, 801, 802, 803, 804, 806, 810, 811, 814, 815, 817, 818, 
                    819, 820, 822, 823, 824, 826, 827, 828, 829, 831, 832, 835, 836, 837, 838, 839, 840, 844, 845, 846, 847, 849, 
                    850, 851, 852, 854, 855, 856, 857, 860, 861, 862, 863, 866, 867, 869, 870, 872, 874, 876, 877, 879, 880, 881, 
                    884, 885, 889, 890, 892, 894, 897, 898, 899, 900, 901, 903, 904, 906, 907, 909, 912, 913, 914, 915, 919, 922, 
                    923, 924, 925, 927, 929, 932, 933, 934, 935, 936, 937, 938, 939, 942, 943, 944, 945, 946, 947, 948, 949, 950, 
                    952, 953, 955, 956, 958, 959, 960, 961, 963, 965, 966, 967, 968, 970, 972, 973, 974, 975, 976, 978, 979, 980, 
                    983, 984, 985, 989, 990, 991, 992, 994, 995, 996, 997, 998, 999, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 
                    1007, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1018, 1019, 1020, 1021, 1022, 1025, 1027, 1028, 1029, 
                    1030, 1031, 1033, 1035, 1036, 1039, 1042, 1043, 1045, 1046, 1047, 1049, 1051, 1052, 1053, 1054, 1055, 1056, 
                    1057, 1058, 1059, 1061, 1062, 1063, 1064, 1071, 1072, 1073, 1075, 1079, 1080, 1081, 1082, 1083, 1084, 1085, 
                    1086, 1088, 1089, 1090, 1091, 1092, 1093, 1094, 1095, 1096, 1097, 1098, 1100, 1102, 1103, 1104, 1105, 1106, 
                    1107, 1110, 1112, 1113, 1115, 1116, 1118, 1120, 1122, 1123, 1124, 1125, 1126, 1127, 1128, 1130, 1131, 1132, 
                    1133, 1134, 1135, 1136, 1137, 1142, 1143, 1144, 1145, 1146, 1147, 1150, 1154, 1155, 1156, 1157, 1163, 1164, 
                    1165, 1168, 1172, 1173, 1176, 1177, 1179, 1184, 1185, 1191, 1192, 1196, 1197, 1201, 1202, 1203, 1204, 1205, 
                    1206, 1207, 1209, 1210, 1211, 1215, 1217, 1221, 1222, 1223, 1226, 1227, 1230, 1231, 1232, 1233, 1238, 1242, 
                    1244, 1249, 1253, 1256, 1257, 1258, 1261, 1262, 1264, 1271, 1273, 1274, 1275, 1277, 1279, 1280, 1283, 1285, 
                    1288, 1289, 1290, 1292, 1293, 1295, 1296, 1298, 1300, 1301, 1303, 1305, 1306, 1307, 1309, 1310, 1311, 1315, 
                    1317, 1319, 1320, 1321, 1322, 1324, 1325, 1330, 1331, 1334, 1335, 1338, 1339, 1341, 1347, 1350, 1351, 1352, 
                    1354, 1355, 1358, 1359, 1362, 1363, 1364, 1366, 1367, 1368, 1369, 1372, 1376, 1377, 1379, 1380, 1382, 1385, 
                    1386, 1391, 1393, 1395, 1398, 1399, 1403, 1405, 1406, 1408, 1409, 1410, 1412, 1414, 1418, 1421, 1426, 1427, 
                    1428, 1429, 1432, 1433, 1434, 1442, 1443, 1445, 1446, 1447, 1450, 1451, 1453, 1454, 1457, 1459, 1460, 1465, 
                    1468, 1471, 1472, 1475, 1480, 1481, 1482, 1485, 1486, 1488, 1492, 1493, 1494, 1495, 1497, 1500, 1502, 1504, 
                    1507, 1508, 1518, 1520, 1523, 1525, 1526, 1531, 1532, 1533, 1534, 1539, 1540, 1541, 1543, 1544, 1547, 1548, 
                    1549, 1551, 1553, 1554, 1555, 1556, 1557, 1558, 1559, 1560, 1563, 1564, 1567, 1568, 1570, 1571, 1572, 1574, 
                    1575, 1576, 1577, 1578, 1579, 1580, 1582, 1584, 1590, 1592, 1602, 1603, 1604, 1605, 1607, 1612, 1613, 1615, 
                    1617, 1618, 1619, 1621, 1623, 1626, 1627, 1628, 1630, 1632, 1633, 1637, 1639, 1640, 1642, 1643, 1644, 1645, 
                    1647, 1649, 1654, 1655, 1658, 1659, 1660, 1666, 1667, 1669, 1670, 1674, 1675, 1676, 1682, 1683, 1684, 1685, 
                    1688, 1689, 1693, 1696, 1697, 1698, 1701, 1702, 1704, 1706, 1708, 1709, 1711, 1712, 1713, 1714, 1715, 1716, 
                    1719, 1721, 1723, 1725, 1727, 1729, 1732, 1733, 1735, 1738, 1740, 1741, 1743, 1749, 1750, 1751, 1754, 1755, 
                    1758, 1760, 1761, 1762, 1763, 1764, 1765, 1766, 1767, 1768, 1769, 1770, 1771, 1773, 1775, 1776, 1777, 1778, 
                    1779, 1781, 1782, 1784, 1785, 1787, 1788, 1792, 1793, 1794, 1796, 1797, 1798, 1799, 1807, 1808, 1810, 1811, 
                    1814, 1815, 1817, 1822, 1825, 1826, 1827, 1828, 1829, 1830, 1831, 1835, 1839, 1841, 1842, 1843, 1844, 1845, 
                    1846, 1848, 1852, 1853, 1854, 1856, 1857, 1858, 1859, 1863, 1865, 1868, 1870, 1873, 1875, 1876, 1877, 1878, 
                    1880, 1881, 1882, 1883, 1886, 1887, 1888, 1890, 1892, 1895, 1898, 1900, 1901, 1902, 1903, 1906, 1910, 1911, 
                    1913, 1915, 1916, 1917, 1922, 1923, 1925, 1929, 1930, 1931, 1935, 1936, 1938, 1939, 1940, 1941, 1945, 1946, 
                    1952, 1953, 1954, 1957, 1963, 1964, 1967, 1970, 1972, 1975, 1976, 1979, 1980, 1982, 1984, 1985, 1987, 1990, 
                    1991, 1992, 1993, 1994, 1996, 1998, 1999, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2011, 2013, 2016, 2017, 
                    2018, 2022, 2024, 2026, 2027, 2030, 2032, 2033, 2037, 2041, 2043, 2045, 2049, 2050, 2053, 2055, 2056, 2060, 
                    2064, 2065, 2067, 2069, 2071, 2072, 2073, 2074, 2075, 2077, 2080, 2081, 2082, 2085, 2088, 2091, 2092, 2093, 
                    2097, 2101, 2104, 2106, 2107, 2109, 2110, 2113, 2117, 2122, 2123, 2126, 2127, 2129, 2133, 2137, 2138], 
            "povCharacter_ids": [60, 130, 148, 149, 150, 216, 238, 529, 957, 1074, 1166], 
            "author": "George R. R. Martin", 
            "name": "A Feast for Crows", 
            "released": "2005-11-08T00:00:00", 
            "id": 5, 
            "numberOfPages": 784, 
            "isbn": "978-0553801507", 
            "publisher": "Bantam Books",  
            "mediaType": "Hardcover"}

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
        self.assertEqual(len(instance.toDict()), 12)

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
        queryResult = database.session.query(
            model).filter_by(name=testName).first()
        self.assertEqual(queryResult.name, testName)

        database.session.rollback()

    def test_Book_release(self):
        b = models.Book(**self.bookParameters)
        self.assertEqual(b.released, "1996-08-01T00:00:00")

    def test_Book_media(self):
        b = models.Book(**self.bookParameters)
        self.assertEqual(b.mediaType, "Hardcover")

    def test_Book_numberOfPages2(self):
        b = models.Book(**self.bookParameters2)
        self.assertEqual(b.numberOfPages, 992)

    def test_Book_isbn2(self):
        b = models.Book(**self.bookParameters2)
        self.assertEqual(b.isbn, self.bookParameters2['isbn'])

    def test_Book_name2(self):
        b = models.Book(**self.bookParameters2)
        self.assertEqual(b.name, "A Storm of Swords")

    def test_Book_publisher2(self):
        b = models.Book(**self.bookParameters2)
        self.assertEqual(b.publisher, "Bantam Books")

    def test_Book_toDict2(self):
        instance = models.Book(**self.bookParameters2)
        self.assertEqual(len(instance.toDict()), 12)

    def test_Book_database_query2(self):
        # Assumes existence of at least one element in model table.
        queryResult = database.session.query(models.Book).first()
        self.assertNotEqual(queryResult.name, None)

        database.session.rollback()

    def test_Book_database_add2(self):
        # Note: Test will fail if a instance already exists with the given id
        testId = 999999
        testName = 'test_Book_database_add'
        self.bookParameters2['name'] = testName
        self.bookParameters2['id'] = testId
        model = models.Book
        instance = model(**self.bookParameters2)

        database.session.add(instance)
        queryResult = database.session.query(
            model).filter_by(name=testName).first()
        self.assertEqual(queryResult.name, testName)

        database.session.rollback()

    def test_Book_release2(self):
        b = models.Book(**self.bookParameters2)
        self.assertEqual(b.released, "2000-10-31T00:00:00")

    def test_Book_media2(self):
        b = models.Book(**self.bookParameters2)
        self.assertEqual(b.mediaType, "Hardcover")

    def test_Book_numberOfPages3(self):
        b = models.Book(**self.bookParameters3)
        self.assertEqual(b.numberOfPages, 784)

    def test_Book_isbn3(self):
        b = models.Book(**self.bookParameters3)
        self.assertEqual(b.isbn, self.bookParameters3['isbn'])

    def test_Book_name3(self):
        b = models.Book(**self.bookParameters3)
        self.assertEqual(b.name, "A Feast for Crows")

    def test_Book_publisher3(self):
        b = models.Book(**self.bookParameters3)
        self.assertEqual(b.publisher, "Bantam Books")

    def test_Book_toDict3(self):
        instance = models.Book(**self.bookParameters3)
        self.assertEqual(len(instance.toDict()), 12)

    def test_Book_database_query3(self):
        # Assumes existence of at least one element in model table.
        queryResult = database.session.query(models.Book).first()
        self.assertNotEqual(queryResult.name, None)

        database.session.rollback()

    def test_Book_database_add3(self):
        # Note: Test will fail if a instance already exists with the given id
        testId = 999999
        testName = 'test_Book_database_add'
        self.bookParameters3['name'] = testName
        self.bookParameters3['id'] = testId
        model = models.Book
        instance = model(**self.bookParameters3)

        database.session.add(instance)
        queryResult = database.session.query(
            model).filter_by(name=testName).first()
        self.assertEqual(queryResult.name, testName)

        database.session.rollback()

    def test_Book_release3(self):
        b = models.Book(**self.bookParameters3)
        self.assertEqual(b.released, "2005-11-08T00:00:00")

    def test_Book_media3(self):
        b = models.Book(**self.bookParameters3)
        self.assertEqual(b.mediaType, "Hardcover")

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
        self.assertEqual(len(instance.toDict()), 19)

    def test_Character_database_add(self):
        # Note: Test will fail if a instance already exists with the given id
        testId = 999999
        testName = 'test_Character_database_add'
        self.characterParameters['name'] = testName
        self.characterParameters['id'] = testId
        model = models.Character
        instance = model(**self.characterParameters)

        database.session.add(instance)
        queryResult = database.session.query(
            model).filter_by(name=testName).first()
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
            h.swornMember_ids, [
                49, 92, 93, 107, 223, 265, 300, 356, 477, 508, 540, 548, 558, 572, 688, 894, 1068, 1193,
                                1280, 1443, 1655, 1693, 1715, 1884])

    def test_House_toDict(self):
        instance = models.House(**self.houseParameters)
        self.assertEqual(len(instance.toDict()), 17)

    def test_House_database_add(self):
        # Note: Test will fail if a instance already exists with the given id
        testId = 999999
        testName = 'test_House_database_add'
        self.houseParameters['name'] = testName
        self.houseParameters['id'] = testId
        model = models.House
        instance = model(**self.houseParameters)

        database.session.add(instance)
        queryResult = database.session.query(
            model).filter_by(name=testName).first()
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
        self.assertEqual(len(instance.toDict()), 11)

    def test_Alliance_database_add(self):
        # Note: Test will fail if a instance already exists with the given id
        testId = 999999
        testName = 'test_Alliance_database_add'
        self.allianceParameters['name'] = testName
        self.allianceParameters['id'] = testId
        model = models.Alliance
        instance = model(**self.allianceParameters)

        database.session.add(instance)
        queryResult = database.session.query(
            model).filter_by(name=testName).first()
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
        queryResult = database.session.query(
            model).filter_by(name=testName).first()
        self.assertNotEqual(queryResult, None)

        database.session.delete(queryResult)
        queryResult = database.session.query(
            model).filter_by(name=testName).first()
        self.assertEqual(queryResult, None)

        database.session.rollback()

# ----
# main
# ----

if __name__ == "__main__":
    main()
