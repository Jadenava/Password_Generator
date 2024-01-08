import random
import string

def generator_password(min_length: int, numbers = True, special_characters = True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters

    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True

        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd


min_length = int(input("Enter the minimum length of characters needed for password: "))
has_number = input("Would you like password to contain number(s)? Please enter (y/n): ").lower() == "y"
has_special = input("Would you like password to contain special character(s)? Please enter (y/n): ").lower() == "y"


pwd = generator_password(min_length, has_number, has_special)

print(f"The password that has been generated for you is:    {pwd}")