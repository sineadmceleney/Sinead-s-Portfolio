#haiku generator

from random import *

#Create the list of words you want to choose from.
fivesyll = ["california", "abomination", "refridgerador", "the spring loaded punch", "watch out for that bus", "Haiku? Whyku? what?", "approximated", "imagination", "Larry equals purple?", "oxidization" ]
sevensyll = ["The forest is tall and green", "They're coming back for me!", "Is that a river or a pond?", "haiku generator fun", "truffalo trees on windows", "photobombing the tourists"]

#Generates a random integer.
x = randint(0, len(fivesyll)-1)
y = randint(0, len(sevensyll)-1)
z = randint(0, len(fivesyll)-1)

#Prints a random haiku
print(fivesyll[x])
print(sevensyll[y])
print(fivesyll[z])
