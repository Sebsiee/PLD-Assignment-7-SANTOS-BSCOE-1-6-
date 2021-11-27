def introduction():
    print("Welcome to my Program 1 - Word Counter!")

def wordCounter():
    sentence = input("Input: ")
    vowels = 0
    consonants = 0
    for i in sentence:
        if(i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U"):
            vowels = vowels+1
        else:
            consonants = consonants+1
    print ("Output: " +  sentence)
    countWords = len(sentence.split())
    print ("Words: " +  str(countWords))
    print("Vowels:", vowels)
    print("Consonants:", consonants - sentence.count(" "))

def goodbye():
    print()
    print("Thank you for using my program!")

introduction()
wordCounter()
goodbye()