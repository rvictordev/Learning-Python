import menu
from menu import Menu, MenuItem #Menu get_items(), find_drink(order_name) | #MenuItem name, cost, ingredients
from coffee_maker import CoffeeMaker # report() -> report of all resources, is_resources_sufficient(drink), make_coffee()
from money_machine import MoneyMachine # report()->current profit, make_payment(cost)
from os import system

machine_on = True
coffee_menu = Menu()
coffee_maker_machine = CoffeeMaker()
coffee_money_machine = MoneyMachine()
drinks = coffee_menu.get_items()
list_of_drinks = drinks.strip("/").split("/")

while machine_on:
    user_choice = input(f"What would you like? {coffee_menu.get_items()}: ").lower()

    if user_choice in list_of_drinks:
        drink = coffee_menu.find_drink(user_choice)
        if drink and coffee_maker_machine.is_resource_sufficient(drink) and coffee_money_machine.make_payment(drink.cost):
            coffee_maker_machine.make_coffee(drink)
    elif user_choice  == "report":
        coffee_maker_machine.report()
        coffee_money_machine.report()
    elif user_choice  == "off":
        print("report")
        machine_on = False
    else:
        print("Invalid Input. Try Again")
