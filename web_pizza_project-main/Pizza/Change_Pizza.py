from Pizza.pizza_product import MenuPizza


class ChangePizza:

    def __init__(self):
        self.menu = MenuPizza.menu

    def set_new_cost_price(self, position, price):
        self.menu[position][0] = price
        return self.menu

    def set_new_sale_price(self, position, price):
        if price < self.menu[position][0]:
            return "Невозможно установить цену ниже себестоимости"
        else:
            self.menu[position][1] = price
            return self.menu

    def set_ingredients(self, position, ingredients: list):
        self.menu[position][2] = ingredients
        return self.menu

    def add_to_menu(self, position):
        MenuPizza.menu[position] = self.menu[position]
        return MenuPizza.menu

    def remove_from_menu(self, position):
        if position in self.menu:
            removed_position = self.menu.pop(position)
            return removed_position, self.menu
        else:
            return "Позиции нет в меню"

    def get_menu(self):
        return self.menu
