import json

from app.views import load_listing

trimmed_character_list = load_listing('data/trimmed_characters.json')
for char in trimmed_character_list:
    if char['povBooks'] is not []:
        result = []
        for book in char['povBooks']:
            val = int(book.split('/')[5])
            result.append(val)
        char['povBooks'] = result
    if char['allegiances'] is not []:
        result = []
        for allegiance in char['allegiances']:
            val = int(allegiance.split('/')[5])
            result.append(val)
        char['allegiances'] = result

print(str(json.dumps(trimmed_character_list)))
