from data import MENU, resources

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f"Water: {res_water}ml\nMilk: {res_milk}ml\n"
              f"Coffee: {res_coffee}g\n Money: ${res_money}")

