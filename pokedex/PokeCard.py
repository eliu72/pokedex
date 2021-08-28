class PokeCard:
    def __init__(self, attributes):
        self.name = attributes['name']
        self.species = attributes['species']
        self.abilities_normal = attributes['abilities']["normal"]
        self.abilities_hidden = attributes['abilities']['hidden']
        self.sprite = attributes['sprite']
        self.description = attributes['description']