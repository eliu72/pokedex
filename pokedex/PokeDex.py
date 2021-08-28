import requests
import PokeCard

class PokeDex:
    def __init__(self, poke_list=None):
        self.count = 100 # limit tp 100 because of rate-limiting
        self.poke_list = self.get_poke_list(poke_list)

    def get_poke_count(self):
        r = requests.get('https://pokeapi.glitch.me/v1/pokemon/counts')
        count = r.json()['total']
        return count

    def get_all_pokemon(self):
        poke_list = []
        for i in range(1, self.count):
            address = 'https://pokeapi.glitch.me/v1/pokemon/' + str(i)
            r = requests.get(address)
            print(r.json())
            poke_list.append(PokeCard.PokeCard(self.json_decode(r.json()[0])))
        return poke_list

    def get_poke_list(self, poke_list):
        if not poke_list:
            return self.get_all_pokemon()

        res_poke_list = []
        for pokemon in poke_list:
            address = 'https://pokeapi.glitch.me/v1/pokemon/' + pokemon
            r = requests.get(address)
            res_poke_list.append(PokeCard.PokeCard(self.json_decode(r.json()[0])))
        return res_poke_list

    def json_decode(self, json_obj, attributes=['name', 'species', 'abilities', 'sprite', 'description']):
        poke_details = {}
        for attribute in attributes:
            poke_details[attribute] = json_obj[attribute]
        return poke_details
