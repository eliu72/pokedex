import json
import requests

import secrets
import PokeDex

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
        properties['Species'] = {
            "select": {
                "name": pokemon.species
            }
        }
        properties['Description'] = {
            "rich_text": [{
                "text": {
                    "content": pokemon.description
                }
            }]
        }
        properties['Normal Abilities'] = {
            "rich_text": [{
                "text": {
                    "content": ", ".join(pokemon.abilities_normal)
                }
            }]
        }
        properties['Hidden Abilities'] = {
            "rich_text": [{
                "text": {
                    "content": ", ".join(pokemon.abilities_hidden)
                }
            }]
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