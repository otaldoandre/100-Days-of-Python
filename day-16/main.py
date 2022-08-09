from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
print(menu)

is_machine_on = True
while is_machine_on:
    options = menu.get_items()
    user_choice = input(f"What would you like? {options}: ")

    if user_choice == "off":
        print("Turning off machine...")
        is_machine_on = False
    elif user_choice == "report":
        money_machine.report()
        coffee_maker.report()
        continue
    else:
        user_order = menu.find_drink(user_choice)
        if not coffee_maker.is_resource_sufficient(user_order) is False\
                and money_machine.make_payment(user_order.cost) is False:
            continue
        else:
            coffee_maker.make_coffee(user_order)
