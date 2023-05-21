MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

RESOURCES = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

MACHINE_IS_ON = True
CASH = 0
SUGAR_DEPOSIT = 30


def user_input():
    """
    Asks user for his input. If input is a coffee it returns it.
    If input is 'report' it returns the report function.
    if input is off it returns maintenance function.
    """
    input_data = input("What would you like? espresso [€1.5] / latte [€2.5] / cappuccino [€3]: ").lower()
    if input_data == "espresso" or input_data == "latte" or input_data == "cappuccino":
        return input_data
    elif input_data == "report":
        return report(input_data)
    elif input_data == "off":
        return maintenance(input_data)
    else:
        print(" Invalid input.")


def maintenance(data):
    """
    It takes input_data = off from "user_input" function and terminates 
    the program.
    """
    global MACHINE_IS_ON
    if data == "off":
        MACHINE_IS_ON = False
        print(" Maintenance mode initiated..... Terminating the coffee machine.")
        return MACHINE_IS_ON


def report(data):
    """
    It takes input_data = report from "user_input" function and 
    prints an analysis of the remaining resources' dictionary.
    """
    if data == "report":
        print(" Administrator mode initiated..... Calculating resources.")
        print(f"  Water: {RESOURCES['water']}ml")
        print(f"  Milk: {RESOURCES['milk']}ml")
        print(f"  Coffee: {RESOURCES['coffee']}g")
        print(f"  Sugar: {SUGAR_DEPOSIT}g")
        print(f"  Money: €{CASH}")


def want_sugar():
    """
    It checks if the sugar resources are sufficient. If that 
    is true, it asks the user if he wants any sugar
    in his coffee and subtracts the value from the deposit.
    """
    global SUGAR_DEPOSIT
    if SUGAR_DEPOSIT <= 20:
        print("Sorry we're out of sugar :(")
    else:
        sugar = input("Do you want sugar in your coffee? (black / sweet / extra): ")
        if sugar == "black":
            return False
        elif sugar == "sweet":
            SUGAR_DEPOSIT -= 10
        elif sugar == "extra":
            SUGAR_DEPOSIT -= 20
        else:
            print("Invalid input")
            want_sugar()


def check_resources(coffee_choice):
    """
    It takes input_data = "some coffee" from user_input" function
    and checks if the remaining resources in the resources dictionary
    are sufficient for the recipe ingredients of that coffee.
    """
    for item in RESOURCES:
        if RESOURCES[item] <= MENU[coffee_choice]["ingredients"][item]:
            return print(f" Sorry there is not enough {item}")
    return True


# def insert_coins():
#     """
#     It asks the user to give some money input. It sums up the input
#     and returns a total of money. It recognizes invalid values,
#     in case the user inserts a non-compatible input.
#     """
#     print("Please insert coins.")
#     money_list = []
#     for decimals in range(0, 1000):
#         money_list.append(decimals)
#     money_list = str(money_list)

#     total = [input(" How many coins of €2?: ")]
#     if total[0] not in money_list:
#         print("Invalid input.")
#         return insert_coins()
#     total.append(input(" How many coins of €1?: "))
#     if total[1] not in money_list:
#         print("Invalid input.")
#         return insert_coins()
#     total.append(input(" How many coins of €0.5?: "))
#     if total[2] not in money_list:
#         print("Invalid input.")
#         return insert_coins()
#     total.append(input(" How many coins of €0.2?: "))
#     if total[3] not in money_list:
#         print("Invalid input.")
#         return insert_coins()

#     total_money = int(total[0]) * 2 + int(total[1]) + int(total[2]) * 0.5 + int(total[3]) * 0.2

#     print(f"You've inserted €{total_money} in total.")
#     return total_money

def insert_coins():
    """
    It asks the user to give some money input. It sums up the 
    input and returns a total of money.
    """
    print("Please insert coins.")
    total = int(input(" How many coins of €2?: ")) * 2
    total += int(input(" How many coins of €1?: "))
    total += int(input(" How many coins of €0.5?: ")) * 0.5
    total += int(input(" How many coins of €0.2?: ")) * 0.2
    print(f"You've inserted €{total} in total.")
    return total


def check_transaction(coffee_choice, need_change):
    """
    It collects money to the vendor's cash equal to the cost of the
    coffee ordered. If the user needs change it gives back the
    subtracted value of the total inserted money (need_change parameter)
    minus the cost of the coffee ordered.
    """
    global CASH
    CASH += MENU[coffee_choice]["cost"]
    if need_change > MENU[coffee_choice]["cost"]:
        change = need_change - MENU[coffee_choice]["cost"]
        print(f"Here's €{round(change, 2)} in change.")


def make_coffee(coffee_choice):
    """
    It subtracts from the resources' dictionary, each ingredient 
    value needed for the recipe of the ordered coffee
    and gives feedback to the user that his coffee is ready.
    """
    for item in RESOURCES:
        RESOURCES[item] -= MENU[coffee_choice]["ingredients"][item]
    print(f"Here is your {coffee_choice}. Enjoy!")


while MACHINE_IS_ON:
    order = user_input()
    if order == "espresso" or order == "latte" or order == "cappuccino":
        want_sugar()
        if check_resources(order):
            money_inserted = insert_coins()
            if money_inserted < MENU[order]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            else:
                check_transaction(order, money_inserted)
                make_coffee(order)
