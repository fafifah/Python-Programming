rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
# rules
# rock beats scissors, scissors beats paper, paper beats rock
import random
my_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: ")

choices = [rock, paper, scissors]
print(choices[int(my_choice)])

computer_choice = random.choice(choices)
print("Computer's choice\n", computer_choice)



if (choices[int(my_choice)] == rock) and (computer_choice == scissors):
  print("You win")
elif (choices[int(my_choice)] == scissors) and (computer_choice == rock):
  print("You lose")
elif (choices[int(my_choice)] == scissors) and (computer_choice == paper):
  print("You win")
elif (choices[int(my_choice)] == paper) and (computer_choice == scissors):
  print("You lose")
elif (choices[int(my_choice)] == paper) and (computer_choice == rock):
  print("You win")
elif (choices[int(my_choice)] == rock) and (computer_choice == paper):
  print("You lose")
else:
  print("Its a draw")