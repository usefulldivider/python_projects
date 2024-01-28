MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk":0,
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
'''
This code is about simulating a coffee machine:
it has 3 drink options
fixed resources which it takes into consideration before making a drink 
collects money before making a drink in the form of coins and gives appropriate change
secret options:
                report-> shows how much resources are left 
                off-> switches off
'''
def money_checker(drink):
    print("Enter your coins:")
    q = float(input("How many quarters?"))
    d = float(input("How many dimes?"))
    n = float(input("How many nickels?"))
    p = float(input("How many pennies?"))
    tot=q*0.25+d*0.10+n*0.05+0.01*p
    if tot>=MENU[drink]["cost"]:
        tot=tot-MENU[drink]["cost"]
        print(f"Your change is {tot}")
        return True
    else:
        print("money too less")
        return False
def resource_checker(drink):
    c=0
    for i in resources:
        if resources[i] >= MENU[drink]["ingredients"][i]:
            c+=1
    if c==3:
        return True
    else:
        print("resources unavailable")
        return False
while True:
    choice=input("What would you like? (espresso/latte/cappuccino):").lower()
    if choice=="report":
        for i in resources:
            print(f"{i}:{resources[i]}")
    elif choice=="espresso":
        if resource_checker(choice) and money_checker(choice):
            for i in resources:
                resources[i] -= MENU[choice]["ingredients"][i]
            print("Here is your drink ☕")
        else:
            exit()
    elif choice=="latte":
        if resource_checker(choice) and money_checker(choice):
            for i in resources:
                resources[i] -= MENU[choice]["ingredients"][i]
            print("Here is your drink ☕")
        else:
            exit()
    elif choice=="cappuccino":
        if resource_checker(choice) and money_checker(choice):
            for i in resources:
                resources[i] -= MENU[choice]["ingredients"][i]
            print("Here is your drink ☕")
        else:
            exit()
    elif choice=="off":
        print("Machine switched off")
        exit()




