from PastaModel import PastaModel
from PastaController import PastaController
from PastaView import PastaView

pasta_model = PastaModel()
pasta_controller = PastaController(pasta_model)
pasta_view = PastaView(pasta_controller)

if __name__ == "__main__":
    pasta_controller.set_ingredients("Карбонара", ["спагетти", "бекон", "яйца", "сыр пармезан", "молоко"])
    pasta_controller.set_price("Карбонара", 380)
    pasta_controller.set_weight("Карбонара", 1200)

    print("Выберите позицию из меню: ")
    pasta_view.show_menu()
    user_choice = input()
    user_action = input("Что хотите посмотреть:\n"
                        "1) Показать всё\n"
                        "2) Показать состав и вес\n"
                        "3) Показать цену\n")
    if user_action == "1":
        pasta_view.show_all(user_choice)
    elif user_action == "2":
        pasta_view.show_without_price(user_choice)
    elif user_action == "3":
        pasta_view.show_only_with_price(user_choice)
