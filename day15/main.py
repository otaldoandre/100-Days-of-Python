MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

QUARTER = 0.25
DIME = 0.10
NICKEL = 0.05
PENNY = 0.01


def print_resources():
    for key, value in resources.items():
        print(f"{key}: {value}")


def is_there_enough_resources(coffee, machine_resources):
    lacking_resources = []
    for key, value in MENU[coffee]["ingredients"].items():
        if (resources[key] - MENU[coffee]["ingredients"][key]) < 0:
            lacking_resources.append(key)
    if len(lacking_resources) == 0:
        return True
    else:
        return lacking_resources


def user_has_enough_money(user_money, coffee_price):
    if user_money < coffee_price:
        return False
    else:
        return True


def calculate_change(user_money, coffee_price):
    if user_money > coffee_price:
        change = user_money - coffee_price
        return change
    elif user_money == coffee_price:
        return 0


def subtract_machine_resources(coffee_choice):
    """
    Subtracts resources from the coffee machine.

    >>> subtract_machine_resources("latte")
    >>> print_resources()
    water: 100
    milk: 50
    coffee: 76

    :param coffee_choice:
    :return:
    """
    for key_, value_ in MENU[coffee_choice]["ingredients"].items():
        resources[key_] = resources[key_] - MENU[coffee_choice]["ingredients"][key_]


machine_is_on = True
while machine_is_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "off":
        print("Turning off machine...")
        break
    elif user_choice == "report":
        print_resources()
        continue

    lack_resources = is_there_enough_resources(user_choice, resources)
    if lack_resources and type(lack_resources) != list:
        pass
    else:
        print(f"Sorry there is not enough {' and '.join(lack_resources)}.\n")
        continue

    print("Please insert coins.")
    user_quarters = QUARTER * int(input("How many quarters?: "))
    user_dimes = DIME * int(input("How many dimes?: "))
    user_nickles = NICKEL * int(input("How many nickels?: "))
    user_pennies = PENNY * int(input("How many pennies?: "))

    user_total_money = user_quarters + user_dimes + user_nickles + user_pennies
    if not user_has_enough_money(user_total_money, MENU[user_choice]["cost"]):
        print("Sorry, that's not enough money. Money refunded.\n")
        continue
    total_change = user_total_money - calculate_change(user_total_money, MENU[user_choice]["cost"])
    user_total_money -= total_change
    resources["money"] += MENU[user_choice]["cost"]
    subtract_machine_resources(user_choice)
    print(f"Here is your ${user_total_money} in change.")
    print(f"Here is your {user_choice}. Enjoy it!\n")


if __name__ == "__main__":
    import doctest
    ###doctest.testmod()
