from Pizza.pizza_creator import PizzaCreator, CreateMenuPizza, CreateOwnPizza
from Pasta.pasta_creator import PastaCreator, CreateMenuPasta, CreateOwnPasta


def pizza_client_code(creator: PizzaCreator, order: str):
    creator.add_additional_ingredient()
    print(creator.make_pizza(order))
    print(creator.bake_pizza(order))
    print(creator.save_order_to_json(order))


def pasta_client_code(creator: PastaCreator, order: str):
    creator.add_additional_ingredient()
    print(creator.make_pasta(order))
    print(creator.cook_pasta(order))
    print(creator.save_order_to_json(order))


if __name__ == "__main__":
    user_choice = input("Выберите \n1) Пицца\n2) Паста\n")
    pizza_menu = ["Гавайская", "Грибная", "Сырный цыпленок", "Пепперони", "Тунец - тысяча островов"]
    pasta_menu = ["Карбонара", "Паста с креветками", "Паста с курицей и грибами"]
    if user_choice == "1":
        print(f"Список пицц:\n{", ".join(pizza_menu)}")
        user_order = input("Введите ваш заказ: ")
        if user_order in pizza_menu:
            pizza_client_code(CreateMenuPizza(), user_order)
        else:
            pizza_client_code(CreateOwnPizza(), user_order)
    elif user_choice == "2":
        print(f"Список паст:\n{", ".join(pasta_menu)}")
        user_order = input("Введите ваш заказ: ")
        if user_order in pasta_menu:
            pasta_client_code(CreateMenuPasta(), user_order)
        else:
            pasta_client_code(CreateOwnPasta(), user_order)
