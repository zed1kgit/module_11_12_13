from PastaController import PastaController


class PastaView:
    def __init__(self, controller: PastaController):
        self.controller = controller

    def show_all(self, position):
        result = self.controller.get_position(position)
        if result is not None:
            print(f"Позиция: {position}\n"
                  f"Цена: {result[0]}\n"
                  f"Вес: {result[1]}\n"
                  f"Ингредиенты: {", ".join(result[2])}\n")
        else:
            print("Позиция не найдена")

    def show_without_price(self, position):
        result = self.controller.get_position(position)
        if result is not None:
            print(f"Позиция: {position}\n"
                  f"Вес: {result[1]}\n"
                  f"Ингредиенты: {", ".join(result[2])}\n")
        else:
            print("Позиция не найдена")

    def show_only_with_price(self, position):
        result = self.controller.get_position(position)
        if result is not None:
            print(f"Позиция: {position}\n"
                  f"Цена: {result[0]}\n")
        else:
            print("Позиция не найдена")

    def show_menu(self):
        result = ", ".join(self.controller.get_menu().keys())
        print(f"Все позиции: {result}")
