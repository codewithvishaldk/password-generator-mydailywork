import random
import string

def generate_password(length, include_numbers, include_uppercase, include_special):
    characters = string.ascii_lowercase
    if include_numbers:
        characters += string.digits
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_special:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")

    try:
        length = int(input("Enter the desired length of the password: "))
    except ValueError:
        print("Invalid input! Please enter a numeric value.")
        return

    include_numbers = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
    include_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
    include_special = input("Include special characters? (yes/no): ").strip().lower() == 'yes'

    password = generate_password(length, include_numbers, include_uppercase, include_special)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
