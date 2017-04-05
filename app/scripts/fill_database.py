# Run with command: 'python -m app.scripts.fill_database'

from app import database
from app.models import Book, Character, House, Alliance
from app.views import load_listing


def create_new_db():
    # Drop old database, then make a new one.
    print('Clearing current database...')
    database.reflect()
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


# Load all books from JSON.
def commit_books():
    trimmed_book_list = load_listing('data/trimmed_books.json')
    for book in trimmed_book_list:
        # book.pop('id')
        book_model = Book(**book)
        database.session.add(book_model)
    database.session.commit()
    print("Book Data loaded.")


def commit_charactes():
    trimmed_character_list = load_listing('data/trimmed_characters.json')
    char_id_set = set()
    for char in trimmed_character_list:
        char_id_set.add(char['id'])
        # char.pop('id')
        char_model = Character(**char)
        # print(str(char_model.toJSON()))
        database.session.add(char_model)
    database.session.commit()
    print("Character Data Loaded")


def commit_houses():
    trimmed_house_list = load_listing('data/trimmed_houses_alliances.json')
    for house in trimmed_house_list:
        house_model = House(**house)
        database.session.add(house_model)
    database.session.commit()
    print("House data loaded")


def commit_alliances():
    trimmed_alliance_list = load_listing('data/trimmed_alliances.json')
    for alliance in trimmed_alliance_list:
        # alliance.pop('id')
        alliance_model = Alliance(**alliance)

        database.session.add(alliance_model)
    database.session.commit()
    print("Alliance data loaded")


create_new_db()
commit_books()
commit_charactes()
commit_houses()
commit_alliances()
