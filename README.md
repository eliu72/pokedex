# Pokédex
### Gotta catch 'em all!

Want to access all your favourite Pokémon in one place? Look no further!
This repo pulls Pokémon info from the https://pokeapi.glitch.me API and displays it onto a Notion database
for easy and aestetically pleasing viewing.

## Getting Started
If you don't already use poetry for python package maangement:
`pip install poetry`

Install Dependencies:
`poetry install`

Populate your Notion Database
1. Create a secrets.py file and write `KEY="<your-notion-integration-key>"`
2. On the next line, write `DATABASE_ID="<database_id>"`
3. In the root of your repository, run the command `poetry run python pokedex/NotionSync.py`

Watch your database populate!

## Customizing your Database
To customize your database, you can pass in a list of Pokémon names or ids to the Pokedex() function in NotionSync.py.

Please note that you can only make 500 API calls at once so this program has limited the default to retrieving 100 Pokemon. You can retrieve additional Pokemon by changing the parameters in the range() function in the get_all_pokemon function.

* This is only meant to be a fun project so it is not optimized for commmercial, or user-friendly use