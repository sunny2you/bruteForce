import itertools
import random
import string

def generate_passwords(length, characters):
    print('making')
    return [''.join(combination) for combination in itertools.product(characters, repeat=length)]
    

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

if __name__ == "__main__":
    main()
