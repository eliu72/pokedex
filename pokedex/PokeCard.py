class PokeCard:
    def __init__(self, attributes):
        self.attributes = attributes
        self.name = attributes['name']
        self.attributes['abilities_normal'] = ", ".join(attributes['abilities']["normal"])
        self.attributes['abilities_hidden'] = ", ".join(attributes['abilities']['hidden'])
        self.sprite = attributes['sprite']
        self.attributes['egg_groups'] = attributes['eggGroups']
        self.attributes['family'] = " -> ".join(attributes['family']['evolutionLine'])

    @staticmethod
    def check_box_attr():
        return ['starter', 'legendary', 'mythical', 'ultraBeast', 'mega']
    
    @staticmethod
    def int_attr():
        return ['gen', 'number']
    
    @staticmethod
    def rich_text_attr():
        return ['description', 'height', 'weight', 'family', 'abilities_hidden', 'abilities_normal']
    
    @staticmethod
    def select_attr():
        return ['species']

    @staticmethod
    def multi_select_attr():
        return ['types', 'egg_groups']
