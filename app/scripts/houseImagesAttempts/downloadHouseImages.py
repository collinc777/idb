import json
from requests_futures.sessions import FuturesSession
import os
import pdb
# from requests.packages.urllib3.exceptions import InsecureRequestWarning
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Joins the two API data sources to find matches
def getHouseImagesMap():
	modelFile = open("houses.txt", "r")
	houses = json.load(open("houses.json", "r"))
	models = list()
	for line in modelFile.readlines():
		modelID, modelName = line.split(",")
		modelName = modelName.replace('\n', '')
		models.append([modelID, modelName])

	houseLinks = dict()
	for house in houses:
		name = str(house["name"].lower())
		for modelID, modelName in models:
			occ = 0
			for word in modelName.split(" "):
				if word in name:
					occ += 1

			if occ:
				if modelID not in houseLinks:
					houseLinks[modelID] = [occ, modelName, house.get("imageLink")]
				else:
					if occ > houseLinks[modelID][0]:
						houseLinks[modelID] = [occ, modelName, house.get("imageLink")]

	json.dump(houseLinks, open("houseImageLinks.json","w"))


# Asynchronous saving of image file
def saveImage(sess, resp):
	picFilePath = "None set!"
	if resp.content is not None:
		picName = resp.url.rsplit("/", 1)[-1]
		with open("app/static/img/newHouses/" + picName, "wb") as picFile:
			picFile.write(resp.content)
			picFilePath = picFile.name
	else:
		print("Response data is empty for session: ", sess)
	return picFilePath

# Download the house images asynchronously
def downloadHouseImages():
	session = FuturesSession(max_workers=10)

	houseImages = json.load(open("houseImageLinks.json", "r"))
	linkedIDs = sorted(houseImages.keys(), key=lambda k: int(str(k)))
	
	asyncRequests = list()
	for houseID in linkedIDs:
		occ, name, imageLink = houseImages[houseID]
		if imageLink is not None:
			future = session.get("http://api.got.show" + imageLink, background_callback=saveImage, verify=False)
			print("Creating session for: ", imageLink)
			asyncRequests.append(future)

	results = [f.result() for f in asyncRequests]

# Rename all the downloaded images according to our getImageLinksMap()
def renameHouseImages():
	houseImages = json.load(open("houseImageLinks.json", "r"))

	for imageFilename in os.listdir("app/static/img/newHouses/"):
		with open("app/static/img/newHouses/" + imageFilename, "rb") as imageFile:
			imageData = imageFile.read()
			for modelID, houseImage in houseImages.items():
				_, name, imageLink = houseImage
				if imageLink is not None:
					if imageLink.endswith(imageFilename):
						with open("app/static/img/houses/" + str(modelID) + ".png", "wb") as newImageFile:
							newImageFile.write(imageData)

def fillInHouseImageGaps():
	# Unknown image
	baseDir = "app/static/img/houses/"
	with open(baseDir + "3.png", "rb") as imageFile:
		imageData = imageFile.read()
		existingHouses = os.listdir(baseDir)
		for i in range(1, 444):
			fillImageFileName = str(i) + ".png"
			if not any([fillImageFileName in existingHouses]):
				print("Filled in image: ", i)
				with open("app/static/img/houses/" + fillImageFileName, "wb") as fillImageFile:
					fillImageFile.write(imageData)


# getHouseImagesMap()		
# downloadHouseImages()
# renameHouseImages()
fillInHouseImageGaps()