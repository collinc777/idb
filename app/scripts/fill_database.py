# Run with command: 'python -m app.scripts.fill_database'

from sqlalchemy.engine import reflection
from sqlalchemy.schema import (
        MetaData,
        Table,
        DropTable,
        ForeignKeyConstraint,
        DropConstraint,
        )

from app import database
from app.models import Book, Character, House, Alliance
from app.views import load_listing

def drop_everything(db):
    # From http://www.sqlalchemy.org/trac/wiki/UsageRecipes/DropEverything

    conn=db.engine.connect()
    # the transaction only applies if the DB supports
    # transactional DDL, i.e. Postgresql, MS SQL Server
    trans = conn.begin()

    inspector = reflection.Inspector.from_engine(db.engine)
    # gather all data first before dropping anything.
    # some DBs lock after things have been dropped in 
    # a transaction.
    metadata = MetaData()

    tbs = []
    all_fks = []
    for table_name in inspector.get_table_names():
        fks = []
        for fk in inspector.get_foreign_keys(table_name):
            if not fk['name']:
                continue
            fks.append(
                ForeignKeyConstraint((),(),name=fk['name'])
                )
        t = Table(table_name,metadata,*fks)
        tbs.append(t)
        all_fks.extend(fks)

    for fkc in all_fks:
        conn.execute(DropConstraint(fkc))

    for table in tbs:
        conn.execute(DropTable(table))

    trans.commit()

# Drop old database, then make a new one.
print('Clearing current database...')
drop_everything(database)
print('Creating new database...')
database.create_all()
database.session.commit()
print("Database created.")

requiredCharacterIds = set()

# Load all books from JSON.
# TODO: Greg 4/4/2016 - Implement id changes once Issue #51 is closed
trimmed_book_list = load_listing('data/trimmed_books.json')
for book in trimmed_book_list:
    # book.pop('id')
    book.pop('houses')
    book['character_ids'] = book.pop('characters')
    book['povCharacter_ids'] = book.pop('povCharacters')
    book_model = Book(**book)
    database.session.add(book_model)
database.session.commit()

print("Book model instance(s) loaded.")

# Load all characters from JSON.
# TODO: Greg 4/4/2016 - Implement id changes once Issue #51 is closed
# TODO: Greg 4/4/2016 - make change to dateOfDeath once Issue #50 is closed
# TODO: Greg 4/4/2016 - make change to povBooks and povBook_ids once Issue #52 is closed
trimmed_character_list = load_listing('data/trimmed_characters_houses.json')
char_id_set = set()
for char in trimmed_character_list:
    char_id_set.add(char['id'])
    # char.pop('id')
    char['book_ids'] = char.pop('books')
    char['house_id'] = char.pop('house')
    #char['povBook_ids'] = char.pop('povBooks')
    char['alliance_ids'] = []
    if 'img' in char:
        char.pop('img')
    char_model = Character(**char)
    # print(str(char_model.toJSON()))
    database.session.add(char_model)
database.session.commit()
print("Character model instance(s) loaded.")

# Load all houses from JSON.
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
        requiredCharacterIds.add(house['overlord_id'])
        requiredCharacterIds.add(house['currentLord_id'])

database.session.commit()
print("House model instance(s) loaded.")

# Load all alliances from JSON.
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
print("Alliance model instance(s) loaded.")

print("Required character id(s): ")
print()
print(str(requiredCharacterIds))
