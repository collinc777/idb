import json
import requests

### API GoT Show

def got_show_filter_entities(entity_name, necessary_fields, output_defaults):
    output_fields = necessary_fields + list(output_defaults.keys())

    data = None
    with open("api_got_show/" + entity_name + '.json') as data_file:    
        data = json.load(data_file)

    if data is not None:
        trimmed = list()
        for d in data:
            passes = True
            for field in necessary_fields:
                if field not in d:
                    passes = False
            if passes:
                trimmed_entity = dict()
                for field in output_fields:
                    if field in d:
                        trimmed_entity[field] = d[field]
                    else:
                        trimmed_entity[field] = output_defaults[field]
                trimmed.append(trimmed_entity)

        print(entity_name, " has ", len(trimmed), " data points")
        with open("api_got_show/trimmed_" + entity_name + ".json", 'w') as data_file:
            json.dump(trimmed, data_file)

def got_show_filter_houses():
    necessary_fields = ["imageLink", "name", "ancestralWeapon", "currentLord", "region", "coatOfArms"]
    output_defaults = {"overlord": "No overlord", "isExtinct": False, "founded": "???", "words": "No words"}

    got_show_filter_entities("houses", necessary_fields, output_defaults)

def got_show_filter_characters():
    necessary_fields = ["male", "name", "books", "titles", "culture", "house"]
    output_defaults = {"dateOfDeath": False}

    got_show_filter_entities("characters", necessary_fields, output_defaults)


### API of Ice and Fire

def ice_and_fire_get_entity(entity):
    entities = list()
    i = 1
    while True:
        print("Retrieving " + entity + " : " + str(i * 50))
        r = requests.get("http://www.anapioficeandfire.com/api/" + entity + "?page=" + str(i) + "&pageSize=50")
        try:
            adds = json.loads(r.text)
            if len(adds) == 0:
                break
            entities.extend(adds)
            i += 1
        except:
            print("Error parsing characters JSON on request ", i)
            break

    print("Number of " + entity + " retrieved: " + str(len(entities)))
    with open("api_ice_and_fire/" + entity + ".json", 'w') as data_file:
        json.dump(entities, data_file)

def ice_and_fire_trim_books():
    iaf_books = None
    with open("api_ice_and_fire/books.json") as iaf_books_file:
        iaf_books = json.load(iaf_books_file)

    trimmed_books = list()
    for book in iaf_books:
        trimmed = book.copy()
        trimmed["id"] = int(trimmed["url"].rsplit("/")[-1])
        trimmed.pop("url")
        trimmed["author"] = "George R. R. Martin"
        trimmed.pop("authors")

        chars = list()
        for character in trimmed["characters"]:
            chars.append(int(character.rsplit("/")[-1]))
        trimmed["characters"] = chars

        pov_chars = list()
        for character in trimmed["povCharacters"]:
            pov_chars.append(int(character.rsplit("/")[-1]))
        trimmed["povCharacters"] = pov_chars
        trimmed_books.append(trimmed)

    with open("api_ice_and_fire/trimmed_books.json", 'w') as trimmed_books_file:
        json.dump(trimmed_books, trimmed_books_file)

def ice_and_fire_trim_houses():
    iaf_houses = None
    with open("api_ice_and_fire/houses.json") as iaf_houses_file:
        iaf_houses = json.load(iaf_houses_file)

    trimmed_houses = list()
    for house in iaf_houses:
        trimmed = house.copy()
        trimmed["id"] = int(trimmed["url"].rsplit("/")[-1])
        trimmed.pop("url")
        if len(trimmed["overlord"]):
            trimmed["overlord"] = int(trimmed["overlord"].rsplit("/")[-1])
        if len(trimmed["currentLord"]):
            trimmed["currentLord"] = int(trimmed["currentLord"].rsplit("/")[-1])
        if len(trimmed["heir"]):
            trimmed["heir"] = int(trimmed["heir"].rsplit("/")[-1])
        if len(trimmed["founder"]):
            trimmed["founder"] = int(trimmed["founder"].rsplit("/")[-1])

        cadets = list()
        for cadet in trimmed["cadetBranches"]:
            cadets.append(int(cadet.rsplit("/")[-1]))
        trimmed["cadetBranches"] = cadets

        sworns = list()
        for sworn in trimmed["swornMembers"]:
            sworns.append(int(sworn.rsplit("/")[-1]))
        trimmed["swornMembers"] = sworns
        trimmed_houses.append(trimmed)

    with open("api_ice_and_fire/trimmed_houses.json", 'w') as trimmed_houses_file:
        json.dump(trimmed_houses, trimmed_houses_file)

### Both

def find_intersecting_houses():
    # Find houses that appear in both and append the imageLink from got_show to ice_and_fire's house

    gs_houses = None
    with open("api_got_show/trimmed_houses.json") as gs_houses_file:
        gs_houses = json.load(gs_houses_file)

    iaf_houses = None
    with open("api_ice_and_fire/trimmed_houses.json") as iaf_houses_file:
        iaf_houses = json.load(iaf_houses_file)

    iaf_houses_by_name = dict()
    for house in iaf_houses:
        iaf_houses_by_name[house["name"]] = house

    trimmed_houses = list()
    for house in gs_houses:
        name = house["name"]

        # couldn't do a simple "if name in iaf_houses_by_name" because
        # there are houses like "House X of Y" where they appear as "House X"
        # in one dataset. So I check if the name is a substring of the other's name
        # by doing "if name in iaf_name"... "House Stark" IS in "House Stark of Winterfell"
        # this bumped the number of intersecting houses from 44 to 179.
        
        for iaf_name in iaf_houses_by_name.keys():
            if name in iaf_name:
                iaf_houses_by_name[iaf_name]["imageLink"] = house["imageLink"]
                trimmed_houses.append(iaf_houses_by_name[iaf_name])
                break

    print("Found ", len(trimmed_houses), " houses in common")
    with open("trimmed_houses.json", 'w') as trimmed_houses_file:
        json.dump(trimmed_houses, trimmed_houses_file)


# Only keep characters that appear in both APIs?
def find_intersecting_characters():
    gs_characters = None
    with open("api_got_show/trimmed_characters.json") as gs_characters_file:
        gs_characters = json.load(gs_characters_file)

    iaf_characters = None
    with open("api_ice_and_fire/characters.json") as iaf_characters_file:
        iaf_characters = json.load(iaf_characters_file)

    iaf_names = set()
    gs_names = set()

    for character in gs_characters:
        gs_names.add(character["name"])

    for character in iaf_characters:
        iaf_names.add(character["name"])

    intersecting_names = iaf_names.intersection(gs_names)

    characters = dict()
    for character in gs_characters:
        if character["name"] in intersecting_names:
            characters[character["name"]] = character

    for character in iaf_characters:
        name = character["name"]
        if name in intersecting_names:
            if name in characters:
                characters[name].update(character)
            else:
                characters[name] = character

    # Convert "url" parameter into an ID paramter
    # Also convert all book references from urls to book IDs
    # "1/2/3".rsplit("/") returns ["1", "2", "3"] and we only want the last part
    # hence the [-1] indexing (get last element)
    # pop removes the key from the dictionary

    trimmed_characters = list()
    for character in characters.values():
        trimmed = character.copy()
        trimmed["id"] = int(trimmed["url"].rsplit("/")[-1])
        trimmed.pop("url")
        books = list()
        for book in trimmed["books"]:
            books.append(int(book.rsplit("/")[-1]))
        trimmed["books"] = books
        trimmed_characters.append(trimmed)

    print("Number of total characters: ", len(characters))
    with open("trimmed_characters.json", 'w') as characters_file:
        json.dump(trimmed_characters, characters_file)

#  Alliances
# Head leader
# Military strength (by number of sworn characters)
# Military strength (by access to ancestral weapons)
# Military strength (by number of seats it has access to)
# Regions it encompasses
# Cultures it encompasses

# Characters in it
# Houses in it

def find_distinct_cultures():
    gs_characters = None
    with open("api_got_show/trimmed_characters.json") as gs_characters_file:
        gs_characters = json.load(gs_characters_file)

    iaf_characters = None
    with open("api_ice_and_fire/characters.json") as iaf_characters_file:
        iaf_characters = json.load(iaf_characters_file)

    gs_cultures = set()
    iaf_cultures = set()

    for character in gs_characters:
        gs_cultures.add(character["culture"].lower())

    for character in iaf_characters:
        iaf_cultures.add(character["culture"].lower())

    cultures = gs_cultures.union(iaf_cultures)
    print(cultures)

find_intersecting_houses()
#ice_and_fire_trim_houses()
#got_show_filter_characters()
#find_intersecting_characters()
#ice_and_fire_get_entity("books")
