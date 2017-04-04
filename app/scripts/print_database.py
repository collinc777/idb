# Run with command: 'python -m app.scripts.print_database'

from app import database
from app.models import Book

# Print all tables.
fronter = ' ----- '
ender = fronter
print(fronter + 'Table(s)' + ender)
tableKeys = database.metadata.tables.keys()
for tableKey in tableKeys:
	print(tableKey)
print('')

# Print all Book model instances.
allBooks = Book.query.all()
for book in allBooks:
    print(book.toJSON())

"""
source: http://stackoverflow.com/questions/6473925/sql-alchemy-getting-a-list-of-tables
classes, models, table_names = [], [], []
for clazz in db.Model._decl_class_registry.values():
    try:
        table_names.append(clazz.__tablename__)
        classes.append(clazz)
    except:
        pass
for table in db.metadata.tables.items():
    if table[0] in table_names:
        models.append(classes[table_names.index(table[0])])

"""
