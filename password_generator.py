import random
import string

print("===== Random Password Generator =====")

while True:
    try:
        length = int(input("Enter password length (minimum 8): "))

        if length < 8:
            print("Error: Password length must be at least 8.")
            continue

        print("\nChoose at least 2 character types:")
        print("1. Lowercase letters")
        print("2. Uppercase letters")
        print("3. Numbers")
        print("4. Symbols")

        choices = input("Enter your choices (example: 123): ")

        if len(set(choices)) < 2:
            print("Error: Please choose at least 2 character types.")
            continue

        characters = ""

        if "1" in choices:
            characters += string.ascii_lowercase

        if "2" in choices:
            characters += string.ascii_uppercase

        if "3" in choices:
            characters += string.digits

        if "4" in choices:
            characters += string.punctuation

        if not characters:
            print("Error: Invalid character type selection.")
            continue

        password = ""

        for i in range(length):
            password += random.choice(characters)

        print("\nGenerated Password:", password)

        again = input("\nGenerate another password? (yes/no): ")

        if again.lower() != "yes":
            print("Thank you for using the Password Generator!")
            break

    except ValueError:
        print("Error: Please enter a valid number.")