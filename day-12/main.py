from random import randint
from art import *

print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100!")

rand_num = randint(1, 100)
print(f"The correct answer is {rand_num}")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "easy" or difficulty == "e":
    num_of_attempts = 10
elif difficulty == "hard" or difficulty == "h":
    num_of_attempts = 5
print(f"You have {num_of_attempts} attempts remaining left! ")

while True:
    if num_of_attempts == 0:
        print("You Lose!")
        break
    user_guess = int(input("Guess a number: "))
    if user_guess == rand_num:
        print("You win!")
        break
    elif user_guess > rand_num:
        print("Too high")
    elif user_guess < rand_num:
        print("Too low.")
    num_of_attempts -= 1
    print("Guess again.")
    print(f"You have {num_of_attempts} attempts remaining left! ")
        
    
    
    
    
