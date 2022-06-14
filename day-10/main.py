from art import *


def add (n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


print(logo)
operators = ["+", "-", "*", "/"]

first_num = int(input("What's the first number? "))
print("+ \n - \n * \n / ")
operator = input("Pick an operation: ")
if operator not in operators:
    while True:
        operator = input("Invalid operator. Try again: ")
        if operator not in operators:
            continue
        else:
            break


second_num = int(input("What's the next number? "))
if operator == "+":
    result = add(first_num, second_num)
elif operator == "-":
    result = subtract(first_num, second_num)
elif operator == "*":
    result = multiply(first_num, second_num)
elif operator == "/":
    result = divide(first_num, second_num)
    
print(f"{first_num} {operator} {second_num} = {result}")
