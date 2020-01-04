import random

print("DICE SIMULATOR")

num_dice = int(input("How many dice do you want to roll? "))
num_sides = int(input("How many sides will each die have? "))

print("\nNumber of Dice: ", num_dice)
print("Number of Sides per Die: ", num_sides)

i = 1
while i <= num_dice:
    print(("Die #{}: {}").format(i, random.randint(1,num_sides)))
    i += 1