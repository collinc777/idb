# Run with command: 'python -m app.scripts.fill_database'

from app import database
from app.models import Book, Character, House, Alliance
from app.views import load_listing

print("Loading model instance(s) from JSON...")

# Load all books from JSON.
trimmed_book_list = load_listing('data/trimmed_books.json')
for book in trimmed_book_list:
	# TODO: Greg 4/4/2016 - Implement id changes once Issue #51 is closed
	book_model = Book(book['numberOfPages'], book['isbn'], book['name'],
		book['publisher'], book['country'], book['povCharacters'], book['author'], book['mediaType'], 
		book['released'], book['characters'])
	database.session.add(book_model)
print("Book model instance(s) loaded.")

# Load all characters from JSON.
trimmed_character_list = load_listing('data/trimmed_characters.json')
for character in trimmed_character_list:
	# TODO: Greg 4/4/2016 - Implement id changes once Issue #51 is closed
	# TODO: Greg 4/4/2016 - make change to dateOfDeath once Issue #50 is closed
	# TODO: Greg 4/4/2016 - make change to povBooks and povBook_ids once Issue #52 is closed
	character_model = Character(house=character['house'], culture=character['culture'],
		titles=character['titles'], spouse=character['spouse'], died=character['died'],
		aliases=character['aliases'], dateOfDeath=False, 
		name=character['name'], born=character['born'], gender=character['gender'],
		father=character['father'], allegiances=character['allegiances'], 
		alliance_ids=[1,2,3], povBooks=character['povBooks'],
		playedBy=character['playedBy'], book_ids=character['books'], tvSeries=character['tvSeries'],
		mother=character['mother'], male=character['male'])
	database.session.add(character_model)
print("Character model instance(s) loaded.")

# Load all houses from JSON.
trimmed_house_list = load_listing('data/trimmed_houses.json')
for house in trimmed_house_list:
	house_model = House(currentLord_id=house['currentLord'], founder=house['founder'], 
		heir_id=house['heir'], cadetBranches=house['cadetBranches'], founded=house['founded'], diedOut=house['diedOut'], titles=house['titles'],
		coatOfArms=house['coatOfArms'], words=house['words'], seats=house['seats'], 
		overlord_id=house['overlord'], name=house['name'], swornMember_ids=house['swornMembers'],
		region=house['region'], ancestralWeapons=house['ancestralWeapons'])
	database.session.add(house_model)
print("House model instance(s) loaded.")


database.session.commit()
print("All instances commited to database.")