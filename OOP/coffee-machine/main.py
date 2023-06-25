from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# make objects from different class

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
# print(menu.menu[0].ingredients['water'])
# print(menu.get_items())

is_on = True
while is_on:
  options =  menu.get_items()
  choice = input(f"​What would you like? {options}: ")
  if choice == "off":
      is_on = False
  elif choice == "report":
    coffee_maker.report()
    money_machine.report()
  else:
    #menu_item = MenuItem()
    drink = menu.find_drink(choice)
    if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
      coffee_maker.make_coffee(drink)
        
      
    
      
  
  
