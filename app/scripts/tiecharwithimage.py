from flask import json

from app.views import loadListing

char_list = loadListing('data/api_got_show/characters.json')
trimmed_char_list = loadListing('data/trimmed_characters.json')

namedToImageDict = dict()


def getFileName(imageURl):
    fileName = imageURl.split('/')[4]
    return fileName


for char in char_list:
    if 'imageLink' in char.keys():
        # print("the characters name is: " + char['name'])
        baseURl = 'https://api.got.show'
        imageURl = char['imageLink']
        name = char['name']
        fileName = 'app/static/img/chars/' + getFileName(imageURl)
        namedToImageDict[name] = fileName


for char in trimmed_char_list:
    char_name = char['name']
    if char_name in namedToImageDict:
        char['img'] = namedToImageDict[char_name]

with open("data/trimmed_characters.json", 'w') as data_file:
    json.dump(trimmed_char_list, data_file)

print(trimmed_char_list)