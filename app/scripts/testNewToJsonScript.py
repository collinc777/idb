from app.views import load_listing
from app.models import Character

trimmed_character_list = load_listing('data/trimmed_characters.json')
for char in trimmed_character_list:
    # char.pop('id')
    char_model = Character(**char)
    break
