############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
from replit import clear
import random
from art import logo



cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def append_card(list_name):
  list_name.append(random.choice(cards))

def card_score(list_name):
  if sum(list_name) > 10:
    cards[0] = 1
  score = sum(list_name)
  return score

def choose_winner(list1,list2):
  if card_score(list1) > card_score(list2):
    if card_score(list1) > 21:
      print("Bust! You lose")
    elif card_score(list1) == 21:
      print("BlackJack! You win")
    else:
      print("You win!")
  elif card_score(list1) < card_score(list2):
    if card_score(list2) > 21:
      print("Computer Bust. You win!")
    elif card_score(list2) == 21:
      print("Computer's BlackJack! You lose")
    else:
      print("You lose!")
  elif card_score(list1) == card_score(list2):
    print("It's a draw")
  
def play_game():
  
  print(logo)
  user_cards = []
  computer_cards = []


  for _ in range(2):
    append_card(user_cards)
    append_card(computer_cards)
    
  should_continue = True
    
  while should_continue:
    print("Your cards: ",user_cards)
    print("Computer's first card: ",computer_cards[0])
    total_so_far = card_score(user_cards)
    if total_so_far > 21:
      print("BUST. You lose!")
      should_continue = False
    elif total_so_far == 21:
      print("Blackjack! You win!")
      should_continue = False
    else:
      print(f"Your score so far is {total_so_far}")
      response = input("Type 'y' to get another card or type'n' to pass: ").lower()
      if response == 'y':
        append_card(user_cards)
        should_continue == True
        
        
      elif response == 'n':
        print("Your final card is: ",user_cards)
        print("Computer's final card is:",computer_cards)
        if card_score(computer_cards) < 17:
          while card_score(computer_cards) < 17:
            append_card(computer_cards)
            print("Computer's final card is:",computer_cards)
        print(f"You're score is {card_score(user_cards)} and Computer's score is {card_score(computer_cards)}")
        choose_winner(user_cards,computer_cards)
        should_continue = False
        '''else:
          choose_winner(user_cards,computer_cards)
          break'''
    
  
  
#play_card()

while input("Do you want to play blackjack? 'y' or 'n': ") == 'y':
  clear()
  play_game()
