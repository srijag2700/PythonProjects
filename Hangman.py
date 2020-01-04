import random

f = open("C:/Users/srija/Documents/TestFolder/words_alpha.txt", "r")
word = random.choice(f.readlines())
print(word)