from random import choice
from hangman_art import *
from hangman_word import word_list


print(logo)
chosen_word = choice(word_list)
print(chosen_word)

display_list = []
for _ in range(1, len(chosen_word) + 1):
    display_list.append("_")

game_is_over = False
lives = 6
while not game_is_over:
    user_guess = input("\nGuess a letter: ").lower()
    index = 0
    if user_guess not in chosen_word:
        lives -= 1
        print(f"You guessed {user_guess}, that's not in the word. You lose a life.")
        if lives == 0:
            print("You lose")
            print(stages[lives])
            game_is_over = True
        print(stages[lives])
        print(f"{' '.join(display_list)}")
        continue
    print(stages[lives])

    if user_guess in display_list:
        print(f"You've already guessed {user_guess}")
        print(f"{' '.join(display_list)}")
        continue

    for letter in chosen_word:
        if letter == user_guess:
            display_list[index] = user_guess
        index += 1

    if "_" not in display_list:
        print("You win")
        game_is_over = True

    print(f"{' '.join(display_list)}")
