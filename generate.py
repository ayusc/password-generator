"""
My modifications to the given code:
	
	1) Include numbers and special characters in passwords
	2) Provide an option for all passwords to be of same length
        3) Add checks for invalid inputs 
	4) Provide options for various combinations of passwords
	
~ Ayus Chatterjee	
"""

import random

def generatePassword(pwlength, char_type):
    string = "abcdefghijklmnopqrstuvwxyz"
    special_characters = "!@#$%&"
    numbers = "0123456789"
    passwords = []

    for length in pwlength:
        password = ""
        for _ in range(length):
            if char_type == 1:
                password += random.choice(string)
            elif char_type == 2:
                password += random.choice(numbers)
            elif char_type == 3:
                password += random.choice(string + special_characters)
            elif char_type == 4:
                password += random.choice(numbers + special_characters)
            elif char_type == 5:
                password += random.choice(string + numbers)
            elif char_type == 6:
                password += random.choice(string + numbers + special_characters)
            else:
                password += random.choice(string + numbers + special_characters)
        
        password = replaceWithUppercaseLetter(password)
        passwords.append(password) 
    
    return passwords

def replaceWithUppercaseLetter(pword):
    for _ in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(pword)//2, len(pword))
        pword = pword[:replace_index] + pword[replace_index].upper() + pword[replace_index+1:]
    return pword

def main():
    try:
        numPasswords = int(input("How many passwords do you want to generate? "))
        if numPasswords <= 0:
            print("Please enter a positive integer for the number of passwords.")
            return
        
        print("Generating " + str(numPasswords) + " passwords")
        
        while True:
            choice = input("Select the type of characters for the passwords:\n"
                           "1. Entirely alphabetic\n"
                           "2. Entirely numeric\n"
                           "3. Alphabet + Special Characters\n"
                           "4. Number + Special Characters\n"
                           "5. Alphabet + Numbers\n"
                           "6. Alphabet + Numbers + Special Characters\n"
                           "Enter your choice (1/2/3/4/5/6): ").strip()
            try:
                char_type = int(choice)
                if char_type not in [1, 2, 3, 4, 5, 6]:
                    print("Invalid choice. Please enter a number between 1 and 6.\n")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a number.\n")

        while True:
            choice = input("Do you want all passwords to be of the same length? (yes/y/no/n): ").lower().strip()
            if choice in ['yes', 'y']:
                all_same_length = True
                break
            elif choice in ['no', 'n']:
                all_same_length = False
                break
            else:
                print("Invalid choice. Please enter 'yes', 'no' or 'y', 'n'\n")

        if all_same_length:
            while True:
                try:
                    length = int(input("Enter the length of all passwords: "))
                    if length < 3:
                        print("Password length must be at least 3 characters.")
                    else:
                        passwordLengths = [length] * numPasswords
                        break
                except ValueError:
                    print("Please enter a valid integer for the password length.")
        else:
            print("Minimum length of password should be 3")
            passwordLengths = []
            for i in range(numPasswords):
                while True:
                    try:
                        length = int(input("Enter the length of Password #" + str(i+1) + ": "))
                        if length < 3:
                            print("Password length must be at least 3 characters.")
                        else:
                            passwordLengths.append(length)
                            break
                    except ValueError:
                        print("Please enter a valid integer for the password length.")
        
        Passwords = generatePassword(passwordLengths, char_type)

        for i, password in enumerate(Passwords):
            print("Password #" + str(i+1) + " = " + password)
    
    except ValueError:
        print("Please enter a valid integer for the number of passwords.")


main()		    
