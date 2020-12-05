from data import MENU, resources

user_input = input("What would you like? (espresso/latte/cappuccino)")
resources['money'] = 0


def ingredients(coffee_ingredients=None):
    if coffee_ingredients is None:
        coffee_ingredients = {}
    coffee_ingredients['user_money'] = insert_coins()
    coffee_ingredients['need_water'] = MENU[user_input]['ingredients']['water']
    if 'milk' in MENU[user_input]['ingredients']:
        coffee_ingredients['need_milk'] = MENU[user_input]['ingredients']['milk']
    coffee_ingredients['need_coffee'] = MENU[user_input]['ingredients']['coffee']
    coffee_ingredients['need_money'] = MENU[user_input]['cost']
    return coffee_ingredients


def coffee_machine(user_input_fn):
    res_water = resources['water']
    res_milk = resources['milk']
    res_coffee = resources['coffee']
    res_money = resources['money']
    if user_input_fn == 'report':
        return print(f"Water: {res_water}ml\nMilk: {res_milk}ml\n"
                     f"Coffee: {res_coffee}g\n Money: ${res_money}")


def insert_coins():
    money = int(input('How many quarters? ')) * 0.25
    money += int(input('How many dimes? ')) * 0.1
    money += int(input('How many nickles? ')) * 0.05
    money += int(input('How many pennies? ')) * 0.01
    return money


# print(MENU[user_input]['ingredients']['milk'])

while user_input != 'off':
    print("Please insert coins.")
    coffee_machine(user_input)
    user_input = input("What would you like? (espresso/latte/cappuccino)")
