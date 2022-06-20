from game_data import *
from art import *
from random import sample

right_guesses = 0
is_game_over = False
cache = []
while not is_game_over:
    print(f"\nRound {right_guesses + 1}")
    print(logo)
    if right_guesses != 0:
        print(f"You're right. Current score: {right_guesses}")

    if right_guesses == 0:
        rand_sample_a = sample(data, 1)[0]

    rand_sample_b = sample(data, 1)[0]

    while True:
        if rand_sample_a['name'] == rand_sample_b['name']:
            rand_sample_b = sample(data, 1)[0]
        else:
            break

    a_followers = rand_sample_a['follower_count']
    print(f"Compare A: {rand_sample_a['name']}, a {rand_sample_a['description']}, from {rand_sample_a['country']}.")
    print(a_followers)

    print(vs)

    b_followers = rand_sample_b['follower_count']
    print(f"Against B: {rand_sample_b['name']}, a {rand_sample_b['description']}, from {rand_sample_b['country']}.")
    print(b_followers)

    user_guess = input("Who has more followers: ").lower()

    if user_guess == 'a' and a_followers > b_followers or user_guess == 'b' and a_followers < b_followers:
        if b_followers > a_followers:
            rand_sample_a = rand_sample_b
        right_guesses += 1
        continue
    else:
        print(f"Sorry that's wrong. Your Final Score is {right_guesses}.")
        is_game_over = True
