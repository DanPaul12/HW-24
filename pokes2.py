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
    try:
        weights = []
        for name in pokemon_list:
            api_url = f"https://pokeapi.co/api/v2/pokemon/{name}"
            response = requests.get(api_url)
            json_data = response.text
            poke_data = json.loads(json_data)
            weight = poke_data["weight"]
            weights.append(weight)
        average = sum(weights)/3
        print(f"The average weight is {average}")
    except:
        pass

calculate_average_weight(pokemon_names)