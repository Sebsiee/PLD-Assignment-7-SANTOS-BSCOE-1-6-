def introduction():
    print("Welcome to my Program 2 - Password Validity!")

def passwordValidation():
    password = input("Input: ")
    validator = 0
    while True:  
        if (len(password)<=15):
            validator = +1
            print("Your password should be greater than 15 characters")
        else:
            validator = 0
            print("Output: Valid Password")
        break
    
    if validator == 1:
        print("Output: Not a Valid Password")

introduction()
passwordValidation()