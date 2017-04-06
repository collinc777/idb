# Run with command: 'python -m app.scripts.print_database'

from app import database
from app.models import Book

# Get all class, model, and table names.
classes = []
models = []
tables = []
for c in database.Model._decl_class_registry.values():
    try:
        tables.append(c.__tablename__)
        classes.append(c)
    except:
        pass
for table in database.metadata.tables.items():
    if table[0] in tables:
        models.append(classes[tables.index(table[0])])

# Print all database characteristics.
# String to place at start of a title line.
fronter = ' ----- '
# String to place at end of a title line.
ender = fronter

# Print all classes.
print(fronter + 'Class(es)' + ender)
for c in classes:
    print(c)
print('')
# Print all models.
print(fronter + 'Model(s)' + ender)
for model in models:
    print(model)
print('')
# Print all tables.
print(fronter + 'Table(s)' + ender)
for tableName in tables:
    print(tableName)
print('')

# Print all model instances.
for model in models:
    print(fronter + str(model) + ' Instances' + ender)
    modelInstances = model.query.all()
    for instance in modelInstances:
        print(instance.toDict())
    print('')

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
