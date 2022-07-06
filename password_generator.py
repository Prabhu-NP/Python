# Python password generator
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'
           , 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'
           , 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
           'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N'
           , 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
           'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+',
           '{', '}', '[', ']', ':', ';', '?', '/']

print("Basic Password Generator Program.")
user_letters = int(input("Enter the number of letters you want in your password : "))
user_numbers = int(input("Enter the number of numbers you want in your password : "))
user_symbols = int(input("Enter the number of symbols you want in your password : "))

def beginner_level(user_letters, user_numbers, user_symbols):
    # defining an empty string for the password generation
    password = ""

    # implementing for loops for password generation
    for char in range(1, user_letters + 1):
        password += random.choice(letters)

    for char in range(1, user_numbers + 1):
        password += random.choice(numbers)

    for char in range(1, user_symbols + 1):
        password += random.choice(symbols)

    return(password)

def amateur_level(user_letters, user_numbers, user_symbols):
    # defining an empty list for password generation
    password = []

    # implementing for loops for password generation
    for char in range(1, user_letters + 1):
        password += random.choice(letters)

    for char in range(1, user_numbers + 1):
        password += random.choice(numbers)

    for char in range(1, user_symbols + 1):
        password += random.choice(symbols)

    # randomly shuffling the generated password
    random.shuffle(password)

    final_password = ""

    for char in password:
        final_password += char

    return final_password

pwd_1 = beginner_level(user_letters, user_numbers, user_symbols)
print("Basic level password --> ", pwd_1)
pwd_2 = amateur_level(user_letters, user_numbers, user_symbols)
print("Mid level password --> ", pwd_2)
