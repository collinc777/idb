from app.views import load_listing

trimmed_house_list = load_listing('data/trimmed_houses_alliances.json')
max_len = 0
for house in trimmed_house_list:
    max_len = max(len(house['coatOfArms']), max_len)

print("the max is: ", max_len)