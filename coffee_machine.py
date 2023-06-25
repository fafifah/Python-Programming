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

# setup all the values
water_amount = 0
milk_amount = 0
coffee_amount = 0

def resource_count(water,milk,coffee):
  water_amount = water
  milk_amount = milk
  coffee_amount = coffee
  return water_amount ,milk_amount ,coffee_amount 
  

refund = False
resource_okay = True
should_continue = True

def coin_got():
  print("Please insert coins.")
  quarters = int(input("how many quarters?: "))
  dimes = int(input("how many dimes?: "))
  nickles = int(input("how many nickles?: "))
  pennies = int(input("how many pennies?: "))
  return quarters,dimes,nickles,pennies

def change(response ,quarters,dimes,nickles,pennies):
  paid = quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01
  cost = MENU[response]['cost']
  if paid > cost:
    give_change = paid - cost
    print(f"Here is ${give_change} in change.")
    print(f"Here is your {response}. Enjoy!")
    return refund == False
  else:
    print("Sorry that's not enough money. Money refunded")
    return refund == True

def resource_left(refund,response,water_amount,milk_amount,coffee_amount):
  if refund is False:
    water_amount = water_amount
    milk_amount = milk_amount
    coffee_amount = coffee_amount
    
  else:
    if response == 'espresso':
      water_amount -= MENU[response]['ingredients']['water']
      coffee_amount -= MENU[response]['ingredients']['coffee']
    else:
      water_amount -= MENU[response]['ingredients']['water']
      milk_amount -= MENU[response]['ingredients']['milk']
      coffee_amount -= MENU[response]['ingredients']['coffee']
  return water_amount ,milk_amount, coffee_amount
  

def check_resource(response,water_amount,milk_amount,coffee_amount):
  resource = ''
  if response == 'espresso':
    if water_amount <= 0:
      resource_okay = False
      resource = 'water'
      return resource_okay, resource 
    if coffee_amount <=0:
      resource_okay = False
      resource = 'coffee'
      return resource_okay, resource 
    else:
      resource_okay = True
      return resource_okay, resource 
    
  else:
    if water_amount <= 0:
      resource_okay = False
      resource = 'water'
      return resource_okay, resource 
    if milk_amount <= 0:
      resource_okay = False
      resource = 'milk'
      return resource_okay, resource 
    if coffee_amount <=0:
      resource = 'coffee'
      return resource_okay, resource 
    else:
      resource_okay = True
      return resource_okay, resource 
    
    
    
  
water_amount ,milk_amount ,coffee_amount = resource_count(resources["water"],resources["milk"],resources["coffee"])

#quarters,dimes,nickles,pennies = coin_got()
while should_continue:
  
  response = input("What would you like?(espresso/latte/cappuccino: ")
  check_okay, resource = check_resource(response,water_amount,milk_amount,coffee_amount)
  if response == 'report':
      print("Water: ",# setup all the values
    water_amount,"ml")
      print("Milk: ",# setup all the values
    milk_amount,"ml")
      print("Coffee: ",# setup all the values
    coffee_amount,"g")
  else:
    if check_okay == True:
      # coin received
      quarters,dimes,nickles,pennies  = coin_got()
      # find change or refund
      chnage_refund = change(response ,quarters,dimes,nickles,pennies)
      #calculate the water,milk,coffee
      water_amount,milk_amount,coffee_amount= resource_left(chnage_refund,response,water_amount,milk_amount,coffee_amount)
    else:
      print(f"Sorry there is not enough {resource}")
      manager_response = input("Does the owner want it still open? type 'y' or 'n': ").lower()
      if manager_response == 'y':
        should_continue = True
      else:
        should_continue = False
      
  

