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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

stillOrdering = True

def check_resources():
    return resources

def get_recipe(drink): # pass in drinkOrder
    recipe = MENU[drink]["ingredients"]
    return recipe

def make_drink(order): # pass in ingredients needed
    resources["water"] = resources["water"] - MENU[order]["ingredients"]["water"]
    if (order != "espresso"):
        resources["milk"] = resources["milk"] - MENU[order]["ingredients"]["milk"]
    resources["coffee"] = resources["coffee"] - MENU[order]["ingredients"]["coffee"]
    print("Remaining resources:")
    print(check_resources())
    return "\nHeres your " + order + "\n"

# type == water, milk or coffee
# value == amount to add to type
def refill_resource(type, value):
    resources[type] = resources[type] + value
    return resources

while stillOrdering: 
    drinkOrder = input("What would you like? (espresso/latte/cappuccino): ")
    drinkOrder = drinkOrder.lower()

    if drinkOrder not in MENU:
        print("Please select a listed drink.")
        continue
    else:
        def drink(drink):
            order = make_drink(drink)
            return order # test listing ingredient items

        print(drink(drinkOrder))

        still = input("would you like to order another? y/n: " )
        if (still == "n"):
            stillOrdering = False
            exit()
        else:
            continue

