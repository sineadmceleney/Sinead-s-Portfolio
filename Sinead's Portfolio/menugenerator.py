#Menu Generator

from random import *

#Create the list of words you want to choose from.
sides = ["french fries", "curly fries", "waffle fries", "caesar salad", "clam chowder", "wedge salad", "fruit salad" ]
mains = ["hamburger", "salmon", "grilled cheese", "mango chicken", "wrap", "spaghetti and meatballs", "chicken fingers"]
desserts = ["ice cream", "chocolate moose", "cake", "cupcake", "cookies", "brownie"]

#Generates a random integer.
x = randint(0, len(sides)-1)
y = randint(0, len(mains)-1)
z = randint(0, len(desserts)-1)

#Prints the menu
print(sides[x] + ", " + mains[y] + ", " + desserts[z])
