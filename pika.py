import requests
import json

api_url = "https://pokeapi.co/api/v2/pokemon/pikachu"
response = requests.get(api_url)
json_data = response.text
pika_data = json.loads(json_data)
print(pika_data["name"],pika_data["abilities"])