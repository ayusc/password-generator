import random

def generatePassword(pwlength):

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
    
    numPasswords = int(input("How many passwords do you want to generate? "))
    
    print("Generating " + str(numPasswords) + " passwords")
    
    passwordLengths = []

    print("Minimum length of password should be 3")

    for i in range(numPasswords):
        length = int(input("Enter the length of Password #" + str(i+1) + ": "))
        if length < 3:
            length = 3
        passwordLengths.append(length)
    
    
    Passwords = generatePassword(passwordLengths)

    for i, password in enumerate(Passwords):
        print("Password #" + str(i+1) + " = " + password)

main()
