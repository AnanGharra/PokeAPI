#!/usr/bin/env python3

import json

class PokemonDB:
    def __init__(self, filename):
        self.filename = filename
        self.data = self.load_data()

    def load_data(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}
        
    def save_data(self):
        with open(self.filename, 'w') as file:
            json.dump(self.data, file, indent=4)

    def get_pokemon(self, name):
        return self.data.get(name)
    
    def save_pokemon(self, pokemon):
        self.data[pokemon['name']] = pokemon
        self.save_data()
    