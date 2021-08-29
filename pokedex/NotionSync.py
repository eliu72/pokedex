import json
import requests

import secrets
import PokeDex
from PokeCard import PokeCard as card

class NotionSync:
    def __init__(self):
        self.base_url = "https://api.notion.com/v1/pages/"
        self.header = {
            "Authorization": secrets.KEY,
            "Content-Type": "application/json",
            "Notion-Version": "2021-08-16"
        }
        self.pokedex = PokeDex.PokeDex()
        self.poke_list = self.pokedex.poke_list

    
    def populate_properties(self, pokemon) -> dict:
        properties = {}
        properties["Name"] = {
            "title": [
                {
                    "text": {
                        "content": pokemon.name
                    }
                }
            ]
        }

        select_attr = card.select_attr()
        for attr in select_attr:
            properties[attr.capitalize()] = {
                "select": {
                    "name": pokemon.attributes[attr]
                }
            }

        check_box_attr = card.check_box_attr()
        for attr in check_box_attr:
            properties[attr.capitalize()] = {
                "checkbox": bool(pokemon.attributes[attr])
            }

        int_attr = card.int_attr()
        for attr in int_attr:
            properties[attr.capitalize()] = {
                "number": int(pokemon.attributes[attr])
            }
        
        rich_text_attr = card.rich_text_attr()
        for attr in rich_text_attr:
            properties[attr.capitalize()] = {
                "rich_text": [{
                    "text": {
                        "content": pokemon.attributes[attr]
                    }
                }]
            }
        
        multi_select_attr = card.multi_select_attr()
        for attr in multi_select_attr:
            multi_select = []
            for name in pokemon.attributes[attr]:
                multi_select.append({"name":name})
            properties[attr.capitalize()] = {
                "multi_select": multi_select
            }
        return properties


    def populate_db(self):
        responses = []
        default_data = {
            "parent": { "database_id": secrets.DATABASE_ID },
            "properties": {}
        }
        for pokemon in self.poke_list:
            data = default_data
            data["properties"] = self.populate_properties(pokemon)
            data["cover"] = {
                "type": "external",
                "external": {
                    "url": pokemon.sprite
                }
            }
            data = json.dumps(data)
            r = requests.post(self.base_url, data=data, headers=self.header)
            responses.append(r.status_code)
        if set(responses) == set([200]):
            return 200
        else:
            return 400


if __name__ == '__main__':
    notion = NotionSync()
    print(notion.populate_db())