from abc import ABC, abstractmethod
from Pizza.pizza_product import MenuPizza, OwnPizza
import json
import time


class PizzaCreator(ABC):
    @abstractmethod
    def make_pizza(self, order):
        pass

    @abstractmethod
    def add_additional_ingredient(self):
        pass

    @abstractmethod
    def bake_pizza(self, order):
        pass

    @abstractmethod
    def save_order_to_json(self, order):
        pass


class CreateMenuPizza(PizzaCreator):
    def make_pizza(self, order):
        return MenuPizza().make_pizza(order)

    def add_additional_ingredient(self):
        return MenuPizza().add_additional_ingredient()

    def bake_pizza(self, order):
        return MenuPizza().bake_pizza(order)

    def save_order_to_json(self, order):
        menu_pizza = {order: MenuPizza.menu[order]}
        menu_pizza[order][2].extend(MenuPizza.additional_ingredients)
        if menu_pizza:
            with open(f"Pizza/orders/{round(time.time(), 2)}_{order}.json", 'w', encoding='utf-8') as fp:
                json.dump(menu_pizza, fp, ensure_ascii=False, indent=2)
        return "Заказ сохранен в файл orders.json"


class CreateOwnPizza(PizzaCreator):
    def make_pizza(self, order):
        return OwnPizza().make_pizza(order)

    def add_additional_ingredient(self):
        return OwnPizza().add_additional_ingredient()

    def bake_pizza(self, order):
        return OwnPizza().bake_pizza(order)[0]

    def save_order_to_json(self, order):
        own_pizza = OwnPizza().bake_pizza(order)[1]
        if own_pizza:
            with open(f"Pizza/orders/{round(time.time(), 2)}_{order}.json", "w", encoding='utf-8') as fp:
                json.dump(own_pizza, fp, ensure_ascii=False, indent=2)
        return "Заказ сохранен в файл orders.json"
