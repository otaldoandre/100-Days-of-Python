from handsigns import *
from random import randint

hand_signs = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print("\nYou chose:")
print(hand_signs[user_choice])

rand_choice = randint(0, 2)
print("Computer chose:")
print(hand_signs[rand_choice])


if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
elif user_choice == rand_choice:
    print("Draw")
elif user_choice == 0 and rand_choice == 2:
    print("You win!")
elif rand_choice == 0 and user_choice == 2:
    print("You lose")
elif rand_choice > user_choice:
    print("You lose")
elif user_choice > rand_choice:
    print("You win!")
