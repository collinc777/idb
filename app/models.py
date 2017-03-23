from app import database

# Foreign key relationships are alternative for povCharacter and characters (need consult for IDB2)
# povCharacters = database.relationship('Character')
# See link: http://docs.sqlalchemy.org/en/latest/orm/join_conditions.html
class Book(database.Model):
	id = database.Column(database.Integer, primary_key=True)
	numberOfPages = database.Column(database.Integer)
	isbn = database.Column(database.String(13))
	name = database.Column(database.String(80))
	publisher = database.Column(database.String(80))
	country = database.Column(database.String(80))
	povCharacters = database.Column(database.ARRAY(database.Integer))
	author = database.Column(database.String(80))
	mediaType = database.Column(database.String(80))
	released = database.Column(database.String(80))
	characters = database.Column(database.ARRAY(database.Integer))

	def __init__(self, numberOfPages, isbn, name, publisher, country, povCharacters, author, mediaType, released, characters):
		self.numberOfPages = numberOfPages
		self.isbn = isbn
		self.name = name
		self.publisher = publisher
		self.country = country
		self.povCharacters = povCharacters
		self.author = author
		self.mediaType = mediaType
		self.released = released
		self.characters = characters

# Foreign key relationships are alternative for povBooks, playedBy, books, tvSeries (need consult for IDB2)
class Character(database.Model):
	id = database.Column(database.Integer, primary_key=True)
	house = database.Column(database.String(80))
	culture = database.Column(database.String(80))
	titles = database.Column(database.ARRAY(database.String))
	spouse = database.Column(database.String(80))
	died = database.Column(database.String(80))
	aliases = database.Column(database.ARRAY(database.String))
	dateOfDeath = database.Column(database.Boolean)
	name = database.Column(database.String(80))
	born = database.Column(database.String(80))
	gender = database.Column(database.String(80))
	father = database.Column(database.String(80))
	allegiances = database.Column(database.ARRAY(database.String))
	povBooks = database.Column(database.ARRAY(database.Integer))
	playedBy = database.Column(database.ARRAY(database.Integer))
	books = database.Column(database.ARRAY(database.Integer))
	tvSeries = database.Column(database.ARRAY(database.Integer))
	mother = database.Column(database.String(80))
	male = database.Column(database.Boolean)

	def __init__(self, house, culture, titles, spouse, died, aliases, dateOfDeath, name, born, gender, father, allegiances, povBooks, playedBy, books, tvSeries, mother, male):
		self.house = house
		self.culture= culture
		self.titles = titles
		self.spouse = spouse
		self.died = died
		self.aliases = aliases
		self.dateOfDeath = dateOfDeath
		self.name = name
		self.born = born
		self.gender = gender
		self.father = father
		self.allegiances = allegiances
		self.povBooks = povBooks
		self.playedBy = playedBy
		self.books = books
		self.tvSeries = tvSeries
		self.mother = mother
		self.male = male
