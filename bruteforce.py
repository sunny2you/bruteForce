import itertools
import random
import string
import time

def generate_passwords_1kind(num_passwords, length, characters):
    passwords = []
    for _ in range(num_passwords):
        passwords.append(''.join(random.choices(characters, k=length)))
    return passwords

def generate_passwords_2kinds(num_passwords, length, characters):
    passwords = []
    for _ in range(num_passwords):
        password = []
        # Ensure at least one number
        password.append(random.choice(string.digits))
        # Generate the remaining characters
        password.extend(random.choices(characters, k=length - 2))
        # Shuffle the password to randomize the position of characters
        random.shuffle(password)
        passwords.append(''.join(password))
    return passwords

def generate_passwords_3kinds(num_passwords, length, characters):
    passwords = []
    for _ in range(num_passwords):
        password = []
        # Ensure at least one number
        password.append(random.choice(string.digits))
        # Ensure at least one alphabet
        password.append(random.choice(string.ascii_letters))
        # Generate the remaining characters
        password.extend(random.choices(characters, k=length - 2))
        # Shuffle the password to randomize the position of characters
        random.shuffle(password)
        passwords.append(''.join(password))
    return passwords

def crack_password(password):
    start_time = time.time()
    characters = string.ascii_letters + string.digits + string.punctuation
    for length in range(4, 9):
        for guess in itertools.product(characters, repeat=length):
            guess_password = ''.join(guess)
            if guess_password == password:
                end_time = time.time()
                return guess_password, end_time - start_time

def main():
    print("What kind of password will you create?")
    print("1. Only numbers")
    print("2. Only alphabet")
    print("3. Number and alphabet")
    print("4. Number, alphabet, and special symbols")
    
    choice = input("Enter your choice: ")

    num_passwords = int(input("Enter the number of passwords to generate: "))
    password_length = int(input("Enter the length of each password: "))

    passwords = []
    if choice == '1':
        numbers = '0123456789'
        passwords = generate_passwords_1kind(num_passwords, password_length, numbers)
    elif choice == '2':
        alphabet = string.ascii_letters
        passwords = generate_passwords_1kind(num_passwords, password_length, alphabet)
    elif choice == '3':
        numbers = '0123456789'
        alphabet = string.ascii_letters
        passwords = generate_passwords_2kinds(num_passwords, password_length, numbers + alphabet)
    elif choice == '4':
        numbers = '0123456789'
        alphabet = string.ascii_letters
        symbols = string.punctuation
        passwords = generate_passwords_3kinds(num_passwords, password_length, numbers + alphabet + symbols)
    else:
        print("Invalid choice!")
        return

    print("Generated passwords:")
    for password in passwords:
        print(password)

    
    total_time = 0
    for i, password in enumerate(passwords, 1):
        print(f"\nCracking Password {i}...")
        cracked_password, time_taken = crack_password(password)
        total_time += time_taken
        print("Cracked Password:", cracked_password)
        print("Time taken to crack:", time_taken, "seconds")

    if num_passwords > 0:
        average_time = total_time / num_passwords
        print("\nAverage time to crack a password:", average_time, "seconds")

if __name__ == "__main__":
    main()
