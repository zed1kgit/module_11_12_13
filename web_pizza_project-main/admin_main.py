from Pizza.Change_Pizza import ChangePizza
from Pasta.Change_Pasta import ChangePasta

while True:
    action_choice = input("""Выберите действие: 
    1) Посмотреть меню
    2) Поменять себестоимость
    3) Поменять цену продажи
    4) Поменять ингредиент
    5) Добавить новую позицию
    6) Убрать позицию из меню
    0) Закрыть
    """)
    if action_choice == "1":
        print(f"Меню пиццы:\n{ChangePizza().get_menu()}\n")
        print(f"Меню пасты:\n{ChangePasta().get_menu()}\n")
    elif action_choice == "0":
        break
    else:
        product_choice = input("Выберите: 1) пицца, 2) паста\n")
        if product_choice == "1":
            changer = ChangePizza()
        elif product_choice == "2":
            changer = ChangePasta()
        else:
            print("Такого нет\n")
            continue
        if action_choice == "2":
            position = input("Какую позицию хотите изменить: ")
            if position not in changer.get_menu().keys():
                print("Такой позиции не существует\n")
                continue
            price = input("Введите новую себестоимость")
            print(changer.set_new_cost_price(position, price))
        elif action_choice == "3":
            position = input("Какую позицию хотите изменить: ")
            if position not in changer.get_menu().keys():
                print("Такой позиции не существует\n")
                continue
            price = input("Введите новую стоимость")
            print(changer.set_new_sale_price(position, price))
        elif action_choice == "4":
            position = input("Какую позицию хотите изменить: ")
            if position not in changer.get_menu().keys():
                print("Такой позиции не существует\n")
                continue
            ingredients = input("Введите новые ингредиенты через запитую: ").split(",")
            print(changer.set_ingredients(position, ingredients))
        elif action_choice == "5":
            position = input("Какую позицию хотите добавить: ")
            if position in changer.get_menu().keys():
                print("Такая позиция уже существует\n")
                continue
            print(changer.add_to_menu(position))
        elif action_choice == "6":
            position = input("Какую позицию хотите удалить: ")
            if position not in changer.get_menu().keys():
                print("Такой позиции не существует\n")
                continue
            print(changer.remove_from_menu(position))
