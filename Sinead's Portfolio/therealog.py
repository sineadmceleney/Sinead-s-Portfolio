start = '''
You're in a forest in Canada and you see a beaver.  You can pick it up or run away.
'''


print(start)

print("Type 'A' to pick it up or '1' to run away.")
user_input = input()
if user_input == "A":
    print("You pick it up and it bites you.  You can assert your dominance or cry.")
    print("Type 'B' to assert your dominance or 'C' to cry.")

    user_input = input()
    if user_input == "B":
        print("The beaver slaps you with its tail. You can drop it or yell at it.")
        print("Type 'D' to drop it or 'E' to yell at it.")

        user_input = input()
        if user_input == "D":
            print("It turns into a were-beaver and since it bit you, you will become one too. You can either give into your were-beaver instinct or try to become human again.")
            print("Type 'H' to give into your instincts or 'I' to try to be human again.")

            user_input = input()
            if user_input == "H":
                print("You've given into your were-beaver instincts.  Your front teeth grow into beaver teeth and you have a sudden urge to cut down trees.  You build a beautiful dam, settle down with a lovely beaver, and live happily ever after.  THE END")
                exit()
            elif user_input == "I":
                print("You try to become human again.  Society rejects you.  You join a good circus that takes care of its animals and travel the world as the Wonderful Were-beaver. You live happily ever after.  THE END")
                exit()
            else:
                print("Incorrect input!! try again!!! :O :0")

        elif user_input == "E":
            print("You yelled at the beaver and it cries.  You're so mean. Now you have to take responsibility for your actions. You can give the beaver a granola bar or take it home.")
            print("Type 'J' to give it a granola bar or 'K' to take it home.")

            user_input = input()
            if user_input == "J":
                print("You gave the beaver a granola bar from your bag.  Unfortunately, granola bars are poisonous to beavers.  The beaver is dying and the other beavers are coming to hunt you down.  Should you run away or try to save the dying beaver?")
                print("Type 'L' to run away or 'M' to try to save the beaver.")

                user_input = input()
                if user_input == 'L':
                    print("bklah")
                elif user_input == 'M':
                    print("You succeeded in saving the beaver! Congrats. The beavers are so thankful that they build you an incredible dam and they crown you the beaver queen.")
                    exit()
                else:
                    print("Incorrect input!! try again!!! :O :0")

            elif user_input == "K":
                print("You took the beaver home and you guys eventually become the best of friends. Y'all plan on forming a crime-fighting duo.")
                print("Type 'O' to fight crime or 'P' to have a tea party")

                user_input = input()
                if user_input == "O":
                    print("You form the best crime-fightingduo of all time.  They call you the best dam cops they've ever seen.  You live happily ever after with your beaver bestie. THE END")
                    exit()

                elif user_input == 'P':
                    print("Your tea party invited some very highly held tea tasting officials and you are now one of the most renown tea makers in the world.  Please stay away from Boston Harbor. THE END")
                    exit()

                else:
                    print("Incorrect input!! try again!!! :O :0")

    elif user_input == "C":
        print("You cry. The beaver takes pity on you and leads you back to its dam. You can stay or run away.")
        print("Type 'F' to stay or 'G' to run away.")

        user_input = input()
        if user_input == "F":
            print("You become beaver queen you live happily ever after. THE END")
            exit()
        elif user-input == "G":
            print("You ran away and got lost.")
    else:
        print("Incorrect input!! try again!!! :O :0")




elif user_input == "1":
    print("You choose to run away and you get lost in the forest. You can either follow the sun or follow the river") # finished the story writing what happens
    print("Type '2' to follow the sun or '3' to follow the river.")

    user_input = input()
    if user_input == "2":
        print("You follow the sun and discover a new world and see and unicorn with a marshmallow horn. You can either eat the horn or run away.")
        print("Type '4' to eat the horn or '5' to run away.")

        user_input= input()
        if user_input == "4":
            print("You ate the unicorn's horn. Now you can fly. You fly away and live happily ever after. THE END")
            exit()
        elif user_input == "5":
            print("You ran away. Bad choice! You're so overcome by emotions due to seeing the unicorn that you can't even and fall out of the sky and die! THE END")
            exit()
        else:
            print("Incorrect input!! try again!!! :O :0")


    elif user_input == "3":
        print("The river leads you to a cute, young fisherman. He asks for your help.")
        print("Type '6' to help him or '7' to not help him.")

        user_input= input()
        if user_input == "6":
            print ("You help the fisherman fish and he falls madly in love with your fishing skills. You get married and you have two kids, a house, and a dog. You're living the typical American Dream that all English teachers talk abput. You live happily ever after. THE END.")
            exit()
        elif user_input == "7":
            print ("You choose not to help the fisherman and karma gets you instantly. You could have married the fisherman and lived an American Dream, but you were too inconsiderate. Karma pushes you into the river and you float to the nearest McDonald's. You spend the rest of your life flipping burgers :(. THE END.")
            exit()
        else:
            print("Incorrect input!! try again!!! :O :0")

    else:
        print("Incorrect input!! try again!!! :O :0")

else:
    print("Incorrect input!! try again!!! :O :0")
