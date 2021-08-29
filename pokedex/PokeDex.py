import json
import requests
import PokeCard

class PokeDex:
    def __init__(self, poke_list=None):
        self.count = self.get_poke_count() # limit tp 100 because of rate-limiting
        self.poke_list = self.get_poke_list(poke_list)

    def get_poke_count(self):
        r = requests.get('https://pokeapi.glitch.me/v1/pokemon/counts')
        print(r.json())
        count = r.json()['total']
        return count

    def get_all_pokemon(self):
        poke_list = []
        for i in range(700, self.count):
            address = 'https://pokeapi.glitch.me/v1/pokemon/' + str(i)
            r = requests.get(address)
            poke_list.append(PokeCard.PokeCard(r.json()[0]))
        return poke_list

    def get_poke_list(self, poke_list):
        if not poke_list:
            return self.get_all_pokemon()

        res_poke_list = []
        for pokemon in poke_list:
            address = 'https://pokeapi.glitch.me/v1/pokemon/' + pokemon
            r = requests.get(address)
            res_poke_list.append(PokeCard.PokeCard(r.json()[0]))
        return res_poke_list

    def json_decode(self, json_obj):
        return json.loads(json_obj[0])