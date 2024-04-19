#!/usr/bin/env python3

import requests

class PokemonAPI:
    URL = "https://pokeapi.co/api/v2/pokemon/"

    def get_pokemon_list():
        response = requests.get(f"{PokemonAPI.URL}")
        if response.status_code == 200:
            pokemon_data = response.json()
            return [pokemon['name'] for pokemon in pokemon_data['results']]
        else:
            return []
        
    def get_pokemon_details(name):
        response = requests.get(f"{PokemonAPI.URL}{name}")
        if response.status_code == 200:
            data = response.json()
            stats = {stat['stat']['name']: stat['base_stat'] for stat in data['stats']}
            return {
                'name': data['name'],
                'hp': stats.get('hp', 0),
                'attack': stats.get('attack', 0),
                'defense': stats.get('defense', 0),
                'speed': stats.get('speed', 0)
            }
        return None