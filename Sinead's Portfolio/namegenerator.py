
from random import *


#Create the list of words you want to choose from.
name_list = ["Piplup", "Henrietta", "Baker", "Elephant", "Cannon", "Outlet", "Truffalo"]

#Generates a random integer.
x = randint(0, len(name_list)-1)
y = randint(0, len(name_list)-1)

#Will generate a first and last name from the name list
print(name_list[x] + " " + name_list[y])
