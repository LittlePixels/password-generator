"""
Password Generator
------------------
A simple command-line password generator that creates a randomized password
based on the number of letters, symbols, and numbers the user specifies.

Usage:
    Run the script and answer the three prompts.
    The generated password will be printed to the terminal.

Part of the Angela Yu Python Bootcamp - Beginner section.
"""

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#Creating an empty List
password_list = []

#The _ is a placeholder. The range has to do with the letters input
for _ in range(nr_letters):
    #Taking and appending to the list a random choice from letters
    password_list.append(random.choice(letters))

for _ in range(nr_symbols):
    password_list.append(random.choice(symbols))

for _ in range(nr_numbers):
    password_list.append(random.choice(numbers))

#Shuffle the letters around in the password list
random.shuffle(password_list)

#Joining the content in the list and adding it to the variable password
password = "".join(password_list)
print(f"Your password is: {password}")
