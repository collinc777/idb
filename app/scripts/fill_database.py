# Run with command: 'python -m app.scripts.fill_database'

from app import database
from app.models import Book, Character, House, Alliance
from app.views import load_listing

# Drop old database, then make a new one.
print('Clearing current database...')
database.drop_all()
print('Creating new database...')
database.create_all()
database.session.commit()
print("Database created.")

print("Loading data from JSON...")

# Test add.
"""
b = Book(
            694, "978-0553103540", "A Game of Thrones", "Bantam Books",
                        "United States", [148, 208, 232], "George R.R. Martin", "Hardcover", "1996", [2, 12, 13])
database.session.add(b)
database.session.commit()
"""

neededCharSet = set()

# Load all books from JSON.
trimmed_book_list = load_listing('data/trimmed_books.json')
for book in trimmed_book_list:
    # book.pop('id')
    book.pop('houses')
    book['character_ids'] = book.pop('characters')
    book['povCharacter_ids'] = book.pop('povCharacters')
    book_model = Book(**book)
    database.session.add(book_model)
database.session.commit()

print("Book Data loaded.")

trimmed_character_list = load_listing('data/trimmed_characters_houses.json')
char_id_set = set()
for char in trimmed_character_list:
    char_id_set.add(char['id'])
    # char.pop('id')
    char['book_ids'] = char.pop('books')
    char['house_id'] = char.pop('house')
    char['povBook_ids'] = char.pop('povBooks')
    char['alliance_ids'] = []
    if 'img' in char:
        char.pop('img')
    char_model = Character(**char)
    # print(str(char_model.toJSON()))
    database.session.add(char_model)
database.session.commit()
print("Character Data Loaded")

trimmed_house_list = load_listing('data/trimmed_houses_alliances.json')
houseId_set = set()
for house in trimmed_house_list:
    # house.pop('id')
    house['currentLord_id'] = house.pop('currentLord')
    house['founder_id'] = house.pop('founder')
    house['heir_id'] = house.pop('heir')
    house['overlord_id'] = house.pop('overlord')
    house['swornMember_ids'] = house.pop('swornMembers')
    house['alliance_id'] = house.pop('alliance')
    house.pop('founder_id')
    if house['overlord_id'] in char_id_set and house['currentLord_id'] in char_id_set:
        houseId_set.add(house['id'])
        house_model = House(**house)
        database.session.add(house_model)
    else:
        neededCharSet.add(house['overlord_id'])
        neededCharSet.add(house['currentLord_id'])

database.session.commit()
print("House data loaded")

trimmed_alliance_list = load_listing('data/trimmed_alliances.json')
for alliance in trimmed_alliance_list:
    # alliance.pop('id')
    alliance['headLeader_id'] = alliance.pop('currentLord')
    alliance['member_ids'] = alliance.pop('swornHouses')
    alliance['weapons'] = alliance.pop('ancestralWeapons')
    alliance['headHouse_id'] = alliance.pop('headHouse')
    if alliance['headHouse_id'] in houseId_set:
        alliance_model = Alliance(**alliance)

        database.session.add(alliance_model)
database.session.commit()
print("Alliance data loaded")

print("needed ids: ")
print()
print(str(neededCharSet))
