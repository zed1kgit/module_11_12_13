from abc import ABC, abstractmethod
from Pasta.pasta_product import MenuPasta, OwnPasta
import json
import time


class PastaCreator(ABC):
    @abstractmethod
    def make_pasta(self, order):
        pass

    @abstractmethod
    def add_additional_ingredient(self):
        pass

    @abstractmethod
    def cook_pasta(self, order):
        pass

    @abstractmethod
    def save_order_to_json(self, order):
        pass


class CreateMenuPasta(PastaCreator):
    def make_pasta(self, order):
        return MenuPasta().make_pasta(order)

    def add_additional_ingredient(self):
        return MenuPasta().add_additional_ingredient()

    def cook_pasta(self, order):
        return MenuPasta().cook_pasta(order)

    def save_order_to_json(self, order):
        menu_pasta = {order: MenuPasta.menu[order]}
        menu_pasta[order][2].extend(MenuPasta.additional_ingredients)
        if menu_pasta:
            with open(f"Pasta/orders/{round(time.time(), 2)}_{order}.json", 'w', encoding='utf-8') as fp:
                json.dump(menu_pasta, fp, ensure_ascii=False, indent=2)
        return "Заказ сохранен в файл orders.json"


class CreateOwnPasta(PastaCreator):
    def make_pasta(self, order):
        return OwnPasta().make_pasta(order)

    def add_additional_ingredient(self):
        return OwnPasta().add_additional_ingredient()

    def cook_pasta(self, order):
        return OwnPasta().cook_pasta(order)[0]

    def save_order_to_json(self, order):
        own_pasta = OwnPasta().make_pasta(order)[1]
        if own_pasta:
            with open(f"Pasta/orders/{round(time.time(), 2)}_{order}.json", "w", encoding='utf-8') as fp:
                json.dump(own_pasta, fp, ensure_ascii=False, indent=2)
        return "Заказ сохранен в файл orders.json"
