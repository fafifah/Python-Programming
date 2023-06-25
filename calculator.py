# my version of calculator

from art import logo2
from replit import clear

print(logo2)
def operation(number1, number2, operation):
  """Takes the numbers and perform operation + - * /"""
  if operation == '+':
    total = number1 + number2
    print(f"{number1} {operation} {number2} = {total}")
    return total
  elif operation == '-':
    total = number1 - number2
    print(f"{number1} {operation} {number2} = {total}")
    return total
  elif operation == '*':
    total = number1 * number2
    print(f"{number1} {operation} {number2} = {total}")
    return total
  elif operation == '/':
    total = number1 / number2
    print(f"{number1} {operation} {number2} = {total}")
    return total

first_number = float(input("What is the first number?:  "))

 
should_continue = True
while should_continue:
  pick_operation =input("Pick an operation: ")
  next_number = float(input("What is the next number?:  ")) 
  total = operation(first_number, next_number, pick_operation)
  
  response = input(f"Type 'y' to continue with {total} or type 'n' to start a new calculation: ")
  if response == 'y':
    first_number = total
    should_continue == True
  else:
    clear()
    first_number = float(input("What is the first number?:  "))
    should_continue == True
    
    
    
    
    
    
    

