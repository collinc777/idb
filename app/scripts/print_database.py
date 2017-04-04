# Run with command: 'python -m app.scripts.print_database'

from app.models import Book

# Print all books
allBooks = Book.query.all()
for book in allBooks:
    print(book.toJSON())
