from PastaModel import PastaModel


class PastaController:
    def __init__(self, model: PastaModel):
        self.model = model

    def set_ingredients(self, position, ingredients):
        if position in self.model.menu.keys():
            return self.model.set_ingredients(position, ingredients)
        else:
            return None

    def set_price(self, position, price):
        if position in self.model.menu.keys():
            return self.model.set_price(position, price)
        else:
            return None

    def set_weight(self, position, weight):
        if position in self.model.menu.keys():
            return self.model.set_weight(position, weight)
        else:
            return None

    def get_position(self, position):
        if position in self.model.menu.keys():
            return self.model.menu[position]
        else:
            return None

    def get_menu(self):
        return self.model.menu
