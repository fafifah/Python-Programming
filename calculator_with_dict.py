# my version of calculator

from art import logo2
#from replit import clear

print(logo2)

def add(n1,n2):
  return n1 + n2
def substract(n1,n2):
  return n1 - n2
def multiply(n1,n2):
  return n1 * n2
def divide(n1,n2):
  return n1 / n2

operation = {
  '+' :add,
  '-' :substract,
  '*' :multiply,
  '/' :divide 
}


first_number = float(input("What is the first number?:  "))

for all_op in operation:
  print(all_op)

 
should_continue = True

while should_continue:
  pick_operation =input("Pick an operation: ")
  next_number = float(input("What is the next number?:  ")) 
  tot_op = operation[pick_operation]
  total = tot_op(first_number, next_number)
  print(f"{first_number} {pick_operation} {next_number} = {total}")
  
  response = input(f"Type 'y' to continue with {total} or type 'n' to start a new calculation: ")
  if response == 'y':
    first_number = total
    should_continue == True
  else:
    #clear()
    first_number = float(input("What is the first number?:  "))
    should_continue == True
    
    
    
    
    
    

