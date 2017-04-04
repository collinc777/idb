# Run with command: 'python -m app.scripts.fill_database'

from app import database
from app.models import Book
from app.views import load_listing

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
trimmed_book_list = load_listing('data/trimmed_books.json')
for book in trimmed_book_list:
	book_model = Book(book['numberOfPages'], book['isbn'], book['name'],
		book['publisher'], book['country'], book['povCharacters'], book['author'], book['mediaType'], 
		book['released'], book['characters'])
	database.session.add(book_model)
	#print(book_model.toJSON())
database.session.commit()

print("Data loaded.")