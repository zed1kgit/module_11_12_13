from abc import ABC, abstractmethod


class PizzaProduct(ABC):

    @abstractmethod
    def make_pizza(self, order):
        pass

    @abstractmethod
    def add_additional_ingredient(self):
        pass

    @abstractmethod
    def bake_pizza(self, order):
        pass


class MenuPizza(PizzaProduct):
    menu = {
        "Гавайская": [100, 150, ["сырный соус", "ветчина", "филе цыпленка", "ананасы", "сыр моцарелла", "базилик"]],
        "Грибная": [80, 120, ["чесночный соус", "ветчина", "свежие шампиньоны", "сыр моцарелла", "базилик"]],
        "Сырный цыпленок": [110, 155, ["сырный соус", "филе цыпленка", "свежие томаты", "сыр моцарелла", "базилик"]],
        "Пепперони": [120, 170, ["пицца-соус", "пепперони", "сыр моцарелла", "базилик"]],
        "Тунец - тысяча островов": [200, 300,
                                    ["соус тысяча островов", "тунец", "маслины", "сыр моцарелла", "лимон", "базилик"]],
    }
    additional_ingredients = []

    def make_pizza(self, order):
        if order in self.menu.keys() and self.additional_ingredients:
            return f"Формируем пиццу {order} с составом:\n{', '.join(self.menu[order][2])}\nДополнительно: {', '.join(self.additional_ingredients)}"
        elif order in self.menu.keys():
            return f"Формируем пиццу {order} со стандартным составом:\n{', '.join(self.menu[order][2])}\n"

    def add_additional_ingredient(self):
        ingredient = input("Выберете дополнительный ингредиент или нажмите стоп: ")
        while ingredient not in ['stop', 'end', 'стоп', 'конец', 'нет']:
            self.additional_ingredients.append(ingredient)
            ingredient = input("Выберете дополнительный ингредиент или нажмите стоп: ")

    def bake_pizza(self, order):
        if not self.additional_ingredients:
            return f"Выпекаем пиццу {order} со стандартным составом:\n{', '.join(self.menu[order][2])}\n"
        else:
            return f"Выпекаем пиццу {order} со дополнительными ингредиентами:\n{', '.join(self.additional_ingredients)}\n"


class OwnPizza(PizzaProduct):
    ingredients = []

    def make_pizza(self, order):
        ingredient = input("Выберете желаемый ингредиент или нажмите стоп: ")
        while ingredient not in ['stop', 'end', 'стоп', 'конец', 'нет']:
            self.ingredients.append(ingredient)
            ingredient = input("Выберете желаемый ингредиент или нажмите стоп: ")
        print()
        return f"Формируем пиццу {order} с желаемыми ингредиентами:\n{', '.join(self.ingredients)}"

    def add_additional_ingredient(self):
        pass

    def bake_pizza(self, order):
        own_pizza = {order: [150, 200, self.ingredients]}
        return f"Выпекаем пиццу {order} с желаемыми ингредиентами:\n{', '.join(self.ingredients)}\n", own_pizza
