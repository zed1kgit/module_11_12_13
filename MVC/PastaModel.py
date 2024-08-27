class PastaModel:
    def __init__(self):
        self.menu = {
            "Карбонара": [0, 0, []],
            "Паста с креветками": [570, 1200,
                                   ["спагетти", "креветки", "помидоры черри", "чеснок", "оливковое масло", "петрушка"]],
            "Паста с курицей и грибами": [490, 1200,
                                          ["макароны", "куриная грудка", "шампиньоны", "лук репчатый", "сливки",
                                           "сыр пармезан"]],
        }

    def set_ingredients(self, position, ingredients: list):
        self.menu[position][2] = ingredients
        return self.menu[position]

    def set_price(self, position, price):
        self.menu[position][0] = price
        return self.menu[position]

    def set_weight(self, position, weight):
        self.menu[position][1] = weight
        return self.menu[position]
