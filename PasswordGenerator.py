import string
from random import *
import random

# print("Two Types Of Passwords: ")

minlength = int(input("Enter min password length: "))
maxlength = int(input("Enter max password length: "))
# numwords = int(input("Enter a number between 4-8: "))

characters = string.ascii_letters + string.punctuation  + string.digits
passwordOne =  "".join(choice(characters) for x in range(randint(minlength, maxlength)))
print("Random Characters: " + passwordOne)

""" f = open("C:/Users/srija/Documents/TestFolder/words_alpha.txt", "r")
i = 1
words = f.readlines()
passwordTwo = ""
while i <= numwords:
    passwordTwo += (random.choice(words))
    i += 1

print("Words (More Secure & Easier to Remember): " + passwordTwo) """