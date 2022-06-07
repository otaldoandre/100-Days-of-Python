import doctest
from art import logo


def caesar(plain_text, shift_number, direction_caesar):
    if shift_number == 0:
        print(f"The {direction_caesar}ed text is {''.join(plain_text)}")

    if direction_caesar == "d":
        direction_caesar = "decode"
    if direction_caesar == "e":
        direction_caesar = "encode"

    plain_text = list(plain_text)
    i = 0
    for letter in plain_text:
        if not letter.isalpha():
            plain_text[i] = letter
            i += 1
            continue
        alphabet_index = alphabet.index(letter)
        if direction_caesar == "encode":
            if alphabet_index + shift_number > 26:
                new_letter = alphabet[(alphabet_index + shift_number) % 26]
            else:
                new_letter = alphabet[alphabet_index + shift_number]
        elif direction_caesar == "decode":
            if alphabet_index + shift_number > 26:
                new_letter = alphabet[(alphabet_index - shift_number) % 26]
            else:
                new_letter = alphabet[alphabet_index - shift_number]
        plain_text[i] = new_letter
        i += 1
    print(f"The {direction_caesar}d text is {''.join(plain_text)}")


print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
is_over = False
while not is_over:
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
    correct_answers = ["encode", "decode", "d", "e"]

    correct_answer = False
    while not correct_answer:
        if direction not in correct_answers:
            print("\nInvalidate answer, please try again.")
            direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
        else:
            correct_answer = True
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if shift > 26:
        shift = shift % 26

    caesar(plain_text=text, shift_number=shift, direction_caesar=direction)

    go_again = input("\nType 'yes' if you want to go again. Otherwise type 'no': ")
    if go_again == "yes" or go_again == "y":
        continue
    elif go_again == "no" or go_again == "n":
        is_over = True


