import json

def filterEntities(entity_name, necessary_fields, output_defaults):
    output_fields = necessary_fields + list(output_defaults.keys())

    data = None
    with open(entity_name + '.json') as data_file:    
        data = json.load(data_file)

    if data is not None:
        i = 0
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
                trimmed_entity["id"] = i
                trimmed_entity["link"] = "/" + entity_name + "/" + str(i)
                trimmed.append(trimmed_entity)
                i += 1

        print(entity_name, " has ", len(trimmed), " data points")
        with open("trimmed_" + entity_name + ".json", 'w') as data_file:
            json.dump(trimmed, data_file)

def filterHouses():
    necessary_fields = ["imageLink", "name", "ancestralWeapon", "currentLord", "region", "coatOfArms"]
    output_defaults = {"overlord": "No overlord", "isExtinct": False, "founded": "???", "words": "No words"}

    filterEntities("houses", necessary_fields, output_defaults)

def filterCharacters():
    necessary_fields = ["male", "name", "books", "titles", "culture", "house"]
    output_defaults = {"dateOfDeath": False}

    data = None
    with open('characters.json') as data_file:    
        data = json.load(data_file)

    filterEntities("characters", necessary_fields, output_defaults)

filterHouses()
filterCharacters()