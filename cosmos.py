import requests
import json

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    for planet in planets:
        if planet['isPlanet']:
            name = planet["name"]
            mass = planet["mass"]["massValue"]
            orbit_period = planet["sideralOrbit"]
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")

def find_heaviest_planet():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']
    mass_list = {}

    for planet in planets:
        if planet['isPlanet']:
            mass = planet["mass"]["massValue"]
            name = planet["name"]
            mass_list[name]= mass
    Keymax = max(mass_list, key= lambda x: mass_list[x])
    weight = mass_list[Keymax]
    print(f"Heaviest planet is {Keymax} with a weight of {weight}")
            
    
fetch_planet_data()
find_heaviest_planet()