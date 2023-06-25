#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
#print(random.choices(letters,k=nr_letters))

# sampling letters, numbers, and symbols
'''
letter_choice = random.choices(letters,k=nr_letters)
symbol_choice = random.choices(symbols,k=nr_symbols)
number_choice = random.choices(numbers,k=nr_numbers)'''

letter_choice = random.sample(letters,k=nr_letters)
symbol_choice = random.sample(symbols,k=nr_symbols)
number_choice = random.sample(numbers,k=nr_numbers)

# adding all the lists
choices = letter_choice + symbol_choice + number_choice
print(choices)

# shuffling lists
random.shuffle(choices)
print(choices)

# forming the password
password = ''
for choice in choices:
  password += choice

print(f"Your password is {password}")
  
