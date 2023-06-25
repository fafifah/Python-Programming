import random
from art import logo4

print(logo4)

# list of numbers to choose from
numbers = range(1,101)

game_number = random.choice(numbers)
#game_number = random.randint(0,100)

def guesses(attempts):


  print(f"You have {attempts} attempts remaining to guess the number.")
  guess_made = int(input('Make a guess: '))
  
    
  
  
  while attempts > 0:
    
    
    
    #if (guess_made < game_number) and attempts != 0:
    if (guess_made < game_number) and attempts > 1:
      print("Too low.")
      print("Guess again.")
      attempts -= 1
      print(f"You have {attempts} attempts remaining to guess the number.")
      guess_made = int(input("Make a guess: "))
    elif (guess_made > game_number) and attempts > 1:
      print("Too high.")
      print("Guess again.")
      attempts -= 1
      print(f"You have {attempts} attempts remaining to guess the number.")
      guess_made = int(input("Make a guess: "))
    elif guess_made == game_number:
      print(f"You got it! The answer was {guess_made}")
      attempts = 0
      
    elif attempts == 1:
      #guess_made = int(input("Make a guess: "))
      if guess_made == game_number:
        print(f"You got it! The answer was {guess_made}")
        attempts -= 1
      elif (guess_made < game_number):
        print("Too low.")
        print("You've run out of guesses, you lose.")
        attempts -= 1
      elif (guess_made > game_number):
        print("Too high.")
        print("You've run out of guesses, you lose.")
        attempts -= 1
      
    
    

  

print("Welcome to the Number Guessing Game!")
print("I\'m thinking of a number between 1 and 100")
#print("psst, the number is ", game_number)
response = input("Choose a difficulty. Type 'easy' or 'hard': ")

if response == 'easy':
  attempts = 10
  guesses(attempts)
  
elif response == 'hard':
  attempts = 5
  guesses(attempts)

