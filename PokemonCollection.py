#!/usr/bin/env python3

from PokemonAPI import PokemonAPI
from PokemonDB import PokemonDB
import random

class PokemonCollection:

    def __init__(self):
        self.db = PokemonDB('pokemon_db.json')

    def draw_from_db(self):
        pokemon_list = PokemonAPI.get_pokemon_list()
        if not pokemon_list:
            print("Drawing Failed!")
            return
        pokemon_name = random.choice(pokemon_list)
        pokemon = self.db.get_pokemon(pokemon_name)
        if pokemon is None:
            print("Drawing a pokemon...")
            pokemon = PokemonAPI.get_pokemon_details(pokemon_name)
            if pokemon:
                self.db.save_pokemon(pokemon)
        if pokemon:
            self.display_pokemon(pokemon)
        else:
            print("Drawing Failed!")

    @staticmethod
    def display_pokemon(pokemon):
        print(f"Name: {pokemon['name'].title()}")
        print(f"HP: {pokemon['hp']}")
        print(f"Attack: {pokemon['attack']}")
        print(f"Defense: {pokemon['defense']}")
        print(f"Speed: {pokemon['speed']}")


def main():
    collector = PokemonCollection()
    print("Welcome to Pokemon!")
    try:
        while True:
            user_input = str(input("Would you like to draw a Pokemon? [yes/no]: ").strip().lower())
            if user_input == 'yes' or user_input == 'y':
                collector.draw_from_db()
            elif user_input == 'no' or user_input == 'n':
                print("Thank you! Closing Pokemon...")
                break 
            else:
                print("Invalid Option! Please choose yes/y or no/n")
    except KeyboardInterrupt:
        print("\nPokemon is being cancelled! Closing Pokemon...")


if __name__ == "__main__":
    main()