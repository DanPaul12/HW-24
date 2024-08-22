import requests
import json

def fetch_pokemon_data(pokemon_name):
    try:
        api_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
        response = requests.get(api_url)
        json_data = response.text
        poke_data = json.loads(json_data)
        print(poke_data["name"],poke_data["abilities"])
    except:
        pass

pokemon_names = ["pikachu", "bulbasaur", "charmander"]

fetch_pokemon_data("bulbasaur")
fetch_pokemon_data("charmander")

def calculate_average_weight(pokemon_list):
    pass
