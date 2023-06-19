# Rock Paper Scissors game
#import
import random

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

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors."))
computer_choice = random.randint(0, 2)

if user_choice == 0 and computer_choice == 2:
    print(f"{rock} beats {scissors} \n User wins")
elif user_choice == 0 and computer_choice == 1:
    print(f"{paper} beats {rock} \n Computer wins")
elif user_choice == 0 and computer_choice == 0:
    print(f"Computer chose {rock}, you chose {rock} \n draw")
elif user_choice == 1 and computer_choice == 0:
    print(f"{paper} beats {rock} \n You win")
elif user_choice == 1 and computer_choice == 1:
    print(f"Computer chose {paper}, you chose {paper} \n draw")
elif user_choice == 1 and computer_choice == 2:
    print(f"Computer chose {scissors} scissors beats {paper} \n Computer wins")
elif user_choice == 2 and computer_choice == 0:
    print(f"You chose {scissors}, Computer chose {rock} \n Computer wins")
elif user_choice == 2 and computer_choice == 1:
    print(f"{scissors} beats {paper} \n You win")
else:
    print(f"Computer chose {scissors}, you chose {scissors} \n draw")