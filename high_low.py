# import modules
import random
from art import logo5 , vs
from game_data import data
from replit import clear
answer = True
# define a global variable score
score = 0
# compare the elements
def compare(dict1,dict2,score):
  if dict1['follower_count'] > dict2['follower_count']:
      score += 1
      answer = True
    
  else:
      score = score
      answer = False
  
  return score, answer
  
      
  


# choose a random element from the data list and remove it. make a function
def choose_element(list1):
  """Takes an element from the list of dictonaries and removes it. Finally returns the element."""
  chosen_element = random.choice(list1)
  #list1.remove(chosen_element)
  return chosen_element

  
# import logo and print
print(logo5)





element_A = choose_element(data)
element_B = choose_element(data)
if element_A == element_B:
  element_B = choose_element(data)


while answer is True:
  
  print(f"Compare A: {element_A['name']}, {element_A['description']}, {element_A['country']}")
  
  # print vs
  print(vs)
  
  
  print(f"Aganist B: {element_B['name']}, {element_B['description']}, {element_B['country']}")
  
  
  
  # we compare
  chosen_one = input("Who has more followers? Type 'A' or 'B': ").upper()
  
  if chosen_one == 'A':
    guess = element_A
    score , answer = compare(guess,element_B,score)
  else:
    guess = element_B
    score , answer = compare(guess,element_A,score)
  # if you win , score goes up and if element A was right 
  if answer == False:
      clear()
      print(5)
      print(f"Sorry! You're Final score is {score}")
  elif answer == True:
    clear()
    print(logo5)
    print(f"You're right! Current score: {score}")
    element_A = guess
    element_B = choose_element(data)
    while element_A == element_B:
      element_B = choose_element(data)
  
# def high_low(element_A,element_B):
#   global score
#   print(f"Compare A: {element_A['name']}, {element_A['description']}, {element_A['country']}")
  
#   # print vs
#   print(vs)
  
  
#   print(f"Aganist B: {element_B['name']}, {element_B['description']}, {element_B['country']}")
  
  
  
#   # we compare
#   chosen_one = input("Who has more followers? Type 'A' or 'B': ").upper()
  
#   if chosen_one == 'A':
#     guess = element_A
#     score , answer = compare(guess,element_B,score)
#   else:
#     guess = element_B
#     score , answer = compare(guess,element_A,score)
#   # if you win , score goes up and if element A was right 
#   if answer == False:
#       clear()
#       print(f"Sorry! You're Final score is {score}")
#   while answer is True:
#     clear()
#     print(f"You're right! Current score: {score}")
#     element_A = guess
#     element_B = choose_element(data)
#     high_low(element_A,element_B)

    
  

# #high_low(element_A,element_B)
  
