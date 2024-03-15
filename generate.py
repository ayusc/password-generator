"""
My modifications to the given code:
	
	1) Include numbers and special characters in passwords
	2) Provide an option for all passwords to be of same length
        3) Add checks for invalid inputs 
	
~ Ayus Chatterjee	
"""

import random

def generatePassword(pwlength, all_same_length=False):
    string = "abcdefghijklmnopqrstuvwxyz"
    special_characters = "!@#$%&"
    numbers = "0123456789"
    passwords = []

    for length in pwlength:
        password = ""
        for _ in range(length):
            char_type = random.choice([1, 2, 3])  # 1: lowercase letter, 2: special character, 3: number
            if char_type == 1:
                password += random.choice(string)
            elif char_type == 2:
                password += random.choice(special_characters)
            else:
                password += random.choice(numbers)
        
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
            choice = input("Do you want all passwords to be of the same length? (yes/y/no/n): ").lower().strip()
            if choice in ['yes', 'y']:
                all_same_length = True
                break
            elif choice in ['no', 'n']:
                all_same_length = False
                break
            else:
                print("Invalid choice. Please enter 'yes', 'no' or 'y', 'n'")

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
        
        Passwords = generatePassword(passwordLengths, all_same_length)

        for i, password in enumerate(Passwords):
            print("Password #" + str(i+1) + " = " + password)
    
    except ValueError:
        print("Please enter a valid integer for the number of passwords.")

main()
