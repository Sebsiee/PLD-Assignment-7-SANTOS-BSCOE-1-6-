import re

def introduction():
    print("Welcome to my Program 2 - Password Validity!")

def passwordValidation():
    password = input("Input: ")
    validator = 0
    while True:  
        if (len(password)<=15):
            validator = +1
            print("Your password should be greater than 15 characters")
        elif not re.search("[A-Z]", password):
            validator = +1
            print("Your password should have a capital letter.")
        elif not re.search("[0-9]", password):
            validator = +1
            print("Your password should have a number.")
        else:
            validator = 0
            print("Output: Valid Password")
        break
    
    if validator == 1:
        print("Output: Not a Valid Password")

introduction()
passwordValidation()