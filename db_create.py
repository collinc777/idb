from app import database
from app import models

# Drop old database, then make a new one.
print('Clearing current database...')
database.drop_all()
print('Creating new database...')
database.create_all()
database.session.commit()
print("Database created.")

print("Loading data from JSON...")

# Test add.
b = models.Book(
            694, "978-0553103540", "A Game of Thrones", "Bantam Books",
                        "United States", [148, 208, 232], "George R.R. Martin", "Hardcover", "1996", [2, 12, 13])
database.session.add(b)

database.session.commit()

print("Data loaded.")

