import itertools
import random
import string
import time

def generate_passwords(length, characters):
    return [''.join(combination) for combination in itertools.product(characters, repeat=length)]

def crack_password(password_to_crack, characters):
    start_time = time.time()
    for length in range(4, 9):
        for combination in itertools.product(characters, repeat=length):
            attempted_password = ''.join(combination)
            if attempted_password == password_to_crack:
                end_time = time.time()
                print(f"Password cracked: {attempted_password}")
                print(f"Time required to crack: {end_time - start_time} seconds")
                return
    print("Password not found!")

def main():
    print("What kind of password will you create?")
    print("1. Only numbers")
    print("2. Only alphabet")
    print("3. Number and alphabet")
    print("4. Number, alphabet, and special symbols")
    
    choice = input("Enter your choice: ")

    passwords = []
    if choice == '1':
        numbers = '0123456789'
        for length in range(4, 9):
            passwords.append(''.join(random.choices(numbers, k=length)))
    elif choice == '2':
        alphabet = string.ascii_letters
        for length in range(4, 9):
            passwords.append(''.join(random.choices(alphabet, k=length)))
    elif choice == '3':
        numbers = '0123456789'
        alphabet = string.ascii_letters
        for length in range(4, 9):
            password = ''.join(random.choices(numbers + alphabet, k=length))
            passwords.append(password)
    elif choice == '4':
        numbers = '0123456789'
        alphabet = string.ascii_letters
        symbols = string.punctuation
        for length in range(4, 9):
            password = ''.join(random.choices(numbers + alphabet + symbols, k=length))
            passwords.append(password)
    else:
        print("Invalid choice!")
        return

    print("Generated passwords:")
    for password in passwords:
        print(password)

    # Crack the first password
    print("\nStarting to crack the first password...")
    crack_password(passwords[0], string.digits)

if __name__ == "__main__":
    main()
