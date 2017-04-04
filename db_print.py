from app import models

Book = models.Book

# Print all books
allBooks = Book.query.all()
for book in allBooks:
    print(book.toJSON())
