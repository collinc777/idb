# Run with command: 'python -m app.scripts.create_database'

from app import database

# Drop old database, then make a new one.
print('Clearing current database...')
database.drop_all()
print('Creating new database...')
database.create_all()
database.session.commit()
print("Database created.")
