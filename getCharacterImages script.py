import urllib.request

from app.views import loadListing

char_list = loadListing('data/api_got_show/characters.json')


def getFileName(imageURl):
    fileName = imageURl.split('/')[4]
    return fileName


for char in char_list:
    if 'imageLink' in char.keys():
        # print("the characters name is: " + char['name'])
        baseURl = 'https://api.got.show'
        imageURl = char['imageLink']
        fileName = getFileName(imageURl)
        url = baseURl + imageURl
        print("the url is : " + url)
        urllib.request.urlretrieve(url, 'app/static/img/chars/' + fileName)
