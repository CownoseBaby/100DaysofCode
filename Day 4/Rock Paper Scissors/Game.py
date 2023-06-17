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

import random

games_images = [rock, paper, scissors]

your_choice = int(input("Do you choose rock, paper, or scissors? Type 0 for Rock, type 1 for paper, type 2 for scissors"))
if your_choice >= 3 or your_choice < 0:
    print("You chose an invalid number, try again!")
else:
    print(games_images[your_choice])

computer_choice = random.randint(0, 2)
print(games_images[computer_choice])

print(f"Computer chooses {computer_choice}")

if your_choice == 0 and computer_choice == 2:
    print("Computer wins!")
elif your_choice == computer_choice:
    print("It's a tie!")
elif computer_choice == 0 and your_choice == 2:
    print("Your lose!")
elif your_choice > computer_choice:
    print("You win!")
elif computer_choice > your_choice:
    print("You win!")

