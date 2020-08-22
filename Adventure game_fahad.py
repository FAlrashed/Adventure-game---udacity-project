import time
import random


'''Game based on luck & limited chices
to win you need to rech the ship on the shore of the city 
passing by the Evils forest before the night, there you 
will have to chose between "Rock, Paper, Scissor" as a tool,
a random choice of road will be decided by the Evil, if you are 
lucky you will pass by the easy road, or elas you have to go 
throght the hard road'''
# road Random Choice 
roadChoice = ["Easy Road", "Hard Road"]
# Hard Road Challenges list: First, Cold beast & Second, beasts, & third, birds (you will have the tool you choice in the game to use it here )
# rock beat birds, paper beats cold beast, and scissor beat beasts

# Win/Lose Statment
resultStatment = ["You are a Winner!\nyou are made it to the ship before down", "You've Lost!\nyou did not make it to the ship"]
# TimePrint function as pauseTime
# Limiting input by definding a "invalid" function


def pauseTime(message):
    print(message)
    time.sleep(1)


def invalid():
  print("You enterd an invalid input please try again !")
  print("")
  print(restarting())


def restarting():
    restart = input("Are you Ready to Start the Game ? (yes/no)\n\n").lower()
    if restart == "yes":
        start()
    else:
      exit()


def start():  # To Start The Game
    print(starter())


def leave():
    print('Comeback Again\n')
    pauseTime("")
    print('You are leaving the game...\n')
    pauseTime("")
    print('Bye!')


# Game brief
print("Welcome to the Game\n")
time.sleep(1)
print("You have to head to the  ship at the city shore passing by Forast."
      "However, the forest is under the evil contral before entering you"
      "have to decide on your tool than randomly one of the"
      "two paths easy or hard one will be selected ..."
      "if you are ready we have a hint for you...\n\n")
time.sleep(1)
print("\n Tool you choice in the game will help you overcome those challanges"
      "Hint: (rock beat birds), (paper beats cold) and (scissor beat beasts)\n\n")
time.sleep(1)
print("Good Luck! you will need it\n\n\n")


# Start with game choices 
def starter():
    inputing = input("Ready to Start the advanture? (yes/no)\n\n").lower()
    if inputing.lower() == "yes":  # Starting game, the other option is exiting smoothly.
        inputing = input("""You Have to choice between your tools:
        -1 Rock
        -2 Paper
        -3 Scissor
        """).lower()
        if inputing == "1":  # Rock Tool (easy/hard)
            roadDirection = random.choice(roadChoice)
            print("Your road is " + roadDirection + "." + " Your tool is Rock" + "(To continue, Click Enter)")
            inputing = ""
            inputing = input()
            inputing = input("""You are entering the forest heading to the ship, What do you want to ride.
            choose:
            -1 Horse 
            -2 Bicycle 
            """).lower()
            # The following if you chose "1" you will ride a "Horse" 2 will ride a "Bicycle".
            if inputing == "1":
                print("You are taking the " + roadDirection + " Your riding a Horse and your tool is Rock")
                inputing = input("\n\n Remember! Rock beat birds, Paper beats cold beast, and Scissor beat beasts." + "(To continue, Click Enter)" +"""\n\nYou are on your way on your horse and you see a laying tree in your way What are you going to do?...
                choose:
                -1 Avoid it 
                -2 ignore it
                """).lower()
                if inputing == "1" and roadDirection[0]:
                    inputing = input("You did well by avoiding it! you can continue your journy" + """You are about to leave the forest... there is a bird attacking you... what are you going to do
                    choose:
                    -1 attack the bird back with Rock (P.S. Birds quite aggressive)
                    -2 ignore it 
                    """).lower()
                    if inputing == "1":
                        print("You did well your choice is wise...")
                        print(resultStatment[0])
                        pauseTime("")
                        print("\n\n")
                        print(restarting())
                    elif inputing == "2":
                        print("Your chose was wrong the bird attacked you and injured you, you no longer can continue\n\n")
                        pauseTime("")
                        print(resultStatment[1])
                        print("\n\n")
                        pauseTime("")
                        print(restarting())
                    else:
                        print(invalid())
                elif inputing == "1" and roadDirection[1]:
                    print("You did well by avoiding it! you can continue your journy ")
                    inputing = input()
                    inputing = input("""You are about to leave the forest... there is a beast walking around you... what are you going to do
                    choose:
                    -1 attack the beast back with Rock (P.S. beasts can't see or hear they only attack once you make noise)
                    -2 Pause and wait for them to pass by 
                    """).lower()
                    if inputing == "1":
                        print("Your chose was wrong the Beasts attached you and injured you, you no longer can continue\n\n")
                        pauseTime("")
                        print(resultStatment[1])
                        print("\n\n")
                        pauseTime("")
                        print(restarting())
                    elif inputing == "2":
                        print("You did well your choice is wise...\nbeasts passed by with no damages")
                        pauseTime("")
                        print(resultStatment[0])
                        print("\n\n")
                        pauseTime("")
                        print(restarting())
                    else:
                        print(invalid())                        
                elif inputing == "2" and roadDirection[0]:
                    inputing = input("Almost was a risky choice but do not worry about it, Your hourse was able to avoid it!"+ """You are about to leave the forest... there is a bird attacking you... what are you going to do
                    choose:
                    -1 attack the bird back with Rock (P.S. Birds quite aggressive)
                    -2 ignore it 
                    """).lower()
                    if inputing == "1":
                        print("You did well your choice is wise...")
                        print(resultStatment[0])
                        pauseTime("")
                        print("\n\n")
                        print(restarting())
                    elif inputing == "2":
                        print("Your chose was wrong the bird attacked you and injured you, you no longer can continue\n\n")
                        pauseTime("")
                        print(resultStatment[1])
                        print("\n\n")
                        pauseTime("")
                        print(restarting())
                    else:
                        print(invalid())
                elif inputing == "2" and roadDirection[1]:
                    print("It was a risky choice, Your hourse was not able to avoid it!")
                    print("Your chose was wrong the bird attacked you and injured you, you no longer can continue\n\n")
                    pauseTime("")
                    print(resultStatment[1])
                    print("\n\n")
                    pauseTime("")
                    print(restarting())
                else:
                    print(invalid()) 
            elif inputing == "2":  # you ride a Bicycle
                print("You are taking the " + roadDirection + " Your riding a Bicycle and your tool is Rock")
                inputing = input(""""\n\nRemember! Rock beat birds, Paper beats cold beast, and Scissor beat beasts"+ " (To continue, Click Enter)\n\n\n You are on your way on your Bicycle and you see a laying tree in your way What are you going to do?...
                choose:
                -1 Avoid it 
                -2 ignore it
                """).lower()
                if inputing == "1" and roadDirection[0]:
                    print("You did well by avoiding it! you can continue your journy ")
                    pauseTime("")  # continue with the game     
                    inputing = ""
                    inputing = input()
                    inputing = input("""You are about to leave the forest... there is a bird attacking you... what are you going to do
                    choose:
                    -1 attack the bird back with Rock (P.S. Birds quite aggressive)
                    -2 ignore it 
                    """).lower()
                    if inputing == "1":
                        print("You did well your choice is wise...")
                        pauseTime("")
                        print(resultStatment[0])
                        print("\n\n")
                        pauseTime("")
                        print(restarting())
                    elif inputing == "2":
                        print("Your chose was wrong the bird attacked you and injured you, you no longer can continue\n\n")
                        pauseTime("")
                        print(resultStatment[1])
                        print("\n\n")
                        pauseTime("")
                        print(restarting())
                    else:
                        print(invalid())
                elif inputing == "1" and roadDirection[1]:
                    print("You did well by avoiding it! you can continue your journy, (To continue click Enter )")
                    inputing = input("""You are about to leave the forest... there is a beast walking around you... what are you going to do
                    choose:
                    -1 attack the beast back with Rock (P.S. beasts can't see or hear they only attack once you make noise)
                    -2 Pause and wait for them to pass by 
                    """).lower()
                    if inputing == "1":
                        print("Your chose was wrong the Beasts attached you and injured you, you no longer can continue\n\n")
                        pauseTime("")
                        print(resultStatment[1])
                        print("\n\n")
                        pauseTime("")
                        print(restarting())
                    elif inputing == "2":
                        print("You did well your choice is wise..." + pauseTime("") + "beasts passed by with no damages")
                        pauseTime("")
                        print(resultStatment[0])
                        print("\n\n")
                        pauseTime("")
                        print(restarting())
                    else:
                        print(invalid())                        
                elif inputing == "2" and roadDirection[0]:
                    print("Almost was a risky choice but do not worry about it, Your Bicycle was able to smoothly ride over it!")
                    pauseTime("")
                    print(resultStatment[0])
                    print("\n\n")
                    pauseTime("")
                    print(restarting())
                elif inputing == "2" and roadDirection[1]:
                    print("It was a risky choice, Your Bicycle was not able to cope with the curves!,(To continue click Enter)")
                    inputing = ""
                    inputing = input()
                    inputing = input("""You are about to leave the forest... there is a beast walking around you... what are you going to do
                    choose:
                    -1 attack the beast back with Rock (P.S. beasts can't see or hear they only attack once you make noise)
                    -2 Pause and wait for them to pass by 
                    """).lower()
                    if inputing == "1":
                        print("Your chose was wrong the Beasts attached you and injured you, you no longer can continue\n\n")
                        pauseTime("")
                        print(resultStatment[1])
                        print("\n\n")
                        pauseTime("")
                        print(restarting())
                    elif inputing == "2":
                        print("You did well your choice is wise..." + pauseTime("") + "beasts passed by with no damages")
                        pauseTime("")
                        print(resultStatment[0])
                        print("\n\n")
                        pauseTime("")
                        print(restarting())
                    else:
                        print(invalid())     
                else:
                    print(invalid()) 
            else:  # invalid choice
                print(invalid())
        elif inputing == "2":  # Paper Tool (easy/hard)
            roadDirection = random.choice(roadChoice)
            print("Your road is " + roadDirection + "." + " Your tool is Paper" + "(To continue, Click Enter)")
            inputing = ""
            inputing = input()
            inputing = input("""You are entering the forest heading to the ship, What do you want to ride.
            choose:
            -1 Horse 
            -2 Bicycle 
            """).lower()
            # The following if you chose "1" you will ride a "Horse" 2 will ride a "Bicycle".
            if inputing == "1":
                print("You are taking the " + roadDirection + " Your riding a Horse and your tool is Paper")
                inputing = input("\n\n Remember! Rock beat birds, Paper beats cold beast, and Scissor beat beasts." + "(To continue, Click Enter)" +"""\n\nYou are on your way on your horse and you see a laying tree in your way What are you going to do?...
                choose:
                -1 Avoid it 
                -2 ignore it
                """).lower()
                if inputing == "1" and roadDirection[0]:
                    inputing = input("You did well by avoiding it! you can continue your journy" + """You are about to leave the forest... there is a bird attacking you... what are you going to do
                    choose:
                    -1 attack the bird back with Rock (P.S. Birds quite aggressive)
                    -2 ignore it 
                    """).lower()
                    if inputing == "1":
                        print("You did well your choice is wise...")
                        print(resultStatment[0])
                        pauseTime("")
                        print("\n\n")
                        print(restarting())
                    elif inputing == "2":
                        print("Your chose was wrong the bird attacked you and injured you, you no longer can continue\n\n")
                        pauseTime("")
                        print(resultStatment[1])
                        print("\n\n")
                        pauseTime("")
                        print(restarting())
                    else:
                        print(invalid())
                elif inputing == "1" and roadDirection[1]:
                    print("You did well by avoiding it! you can continue your journy ")
                    inputing = input()
                    inputing = input("""You are about to leave the forest... there is a beast walking around you... what are you going to do
                    choose:
                    -1 attack the beast back with Rock (P.S. beasts can't see or hear they only attack once you make noise)
                    -2 Pause and wait for them to pass by 
                    """).lower()
                    if inputing == "1":
                        print("Your chose was wrong the Beasts attached you and injured you, you no longer can continue\n\n")
                        pauseTime("")
                        print(resultStatment[1])
                        print("\n\n")
                        pauseTime("")
                        print(restarting())
                    elif inputing == "2":
                        print("You did well your choice is wise...\nbeasts passed by with no damages")
                        pauseTime("")
                        print(resultStatment[0])
                        print("\n\n")
                        pauseTime("")
                        print(restarting())
                    else:
                        print(invalid())                        
                elif inputing == "2" and roadDirection[0]:
                    inputing = input("Almost was a risky choice but do not worry about it, Your hourse was able to avoid it!"+ """You are about to leave the forest... there is a bird attacking you... what are you going to do
                    choose:
                    -1 attack the bird back with Rock (P.S. Birds quite aggressive)
                    -2 ignore it 
                    """).lower()
                    if inputing == "1":
                        print("You did well your choice is wise...")
                        print(resultStatment[0])
                        pauseTime("")
                        print("\n\n")
                        print(restarting())
                    elif inputing == "2":
                        print("Your chose was wrong the bird attacked you and injured you, you no longer can continue\n\n")
                        pauseTime("")
                        print(resultStatment[1])
                        print("\n\n")
                        pauseTime("")
                        print(restarting())
                    else:
                        print(invalid())
                elif inputing == "2" and roadDirection[1]:
                    print("It was a risky choice, Your hourse was not able to avoid it!")
                    print("Your chose was wrong the bird attacked you and injured you, you no longer can continue\n\n")
                    pauseTime("")
                    print(resultStatment[1])
                    print("\n\n")
                    pauseTime("")
                    print(restarting())
                else:
                    print(invalid()) 
            elif inputing == "2":  # you ride a Bicycle
                print("You are taking the " + roadDirection + " Your riding a Bicycle and your tool is Paper")
                inputing = input(""""\n\nRemember! Rock beat birds, Paper beats cold beast beast, and Scissor beat beasts"+ " (To continue, Click Enter)\n\n\n You are on your way on your Bicycle and you see a laying tree in your way What are you going to do?...
                choose:
                -1 Avoid it 
                -2 ignore it
                """).lower()
                if inputing == "1" and roadDirection[0]:
                    print("You did well by avoiding it! you can continue your journy ")
                    pauseTime("")  # continue with the game     
                    inputing = ""
                    inputing = input()
                    inputing = input("""You are about to leave the forest... there is a bird attacking you... what are you going to do
                    choose:
                    -1 attack the Birds back with Paper (P.S. Birds quite aggressive)
                    -2 ignore it 
                    """).lower()
                    if inputing == "1":
                        print("You did well your choice is wise...")
                        pauseTime("")
                        print(resultStatment[0])
                        print("\n\n")
                        pauseTime("")
                        print(restarting())
                    elif inputing == "2":
                        print("Your chose was wrong the ice attacked you and injured you, you no longer can continue\n\n")
                        pauseTime("")
                        print(resultStatment[1])
                        print("\n\n")
                        pauseTime("")
                        print(restarting())
                    else:
                        print(invalid())
                elif inputing == "1" and roadDirection[1]:
                    print("You did well by avoiding it! you can continue your journy, (To continue click Enter )")
                    inputing = input("""You are about to leave the forest... there is a cold beast walking around you... what are you going to do
                    choose:
                    -1 attack the cold beast back with Paper (P.S. beasts can't see or hear they only attack once you make noise)
                    -2 Pause and wait for them to pass by 
                    """).lower()
                    if inputing == "1":
                        print("Your chose was wrong the Beasts attached you and injured you, you no longer can continue\n\n")
                        pauseTime("")
                        print(resultStatment[1])
                        print("\n\n")
                        pauseTime("")
                        print(restarting())
                    elif inputing == "2":
                        print("You did well your choice is wise..." + pauseTime("") + "beasts passed by with no damages")
                        pauseTime("")
                        print(resultStatment[0])
                        print("\n\n")
                        pauseTime("")
                        print(restarting())
                    else:
                        print(invalid())                        
                elif inputing == "2" and roadDirection[0]:
                    print("Almost was a risky choice but do not worry about it, Your Bicycle was able to smoothly ride over it!")
                    pauseTime("")
                    print(resultStatment[0])
                    print("\n\n")
                    pauseTime("")
                    print(restarting())
                elif inputing == "2" and roadDirection[1]:
                    print("It was a risky choice, Your Bicycle was not able to cope with the curves!,(To continue click Enter)")
                    inputing = ""
                    inputing = input()
                    inputing = input("""You are about to leave the forest... there is a beast walking around you... what are you going to do
                    choose:
                    -1 attack the beast back with Rock (P.S. beasts can't see or hear they only attack once you make noise)
                    -2 Pause and wait for them to pass by 
                    """).lower()
                    if inputing == "1":
                        print("Your chose was wrong the Beasts attached you and injured you, you no longer can continue\n\n")
                        pauseTime("")
                        print(resultStatment[1])
                        print("\n\n")
                        pauseTime("")
                        print(restarting())
                    elif inputing == "2":
                        print("You did well your choice is wise..." + pauseTime("") + "beasts passed by with no damages")
                        pauseTime("")
                        print(resultStatment[0])
                        print("\n\n")
                        pauseTime("")
                        print(restarting())
                    else:
                        print(invalid())     
                else:
                    print(invalid()) 
            else:  # invalid choice
                print(invalid())
        elif inputing == "3":  # Scissor Tool (easy/hard)
            roadDirection = random.choice(roadChoice)
            print("Your road is " + roadDirection + "." + " Your tool is Scissor" + "(To continue, Click Enter)")
            inputing = ""
            inputing = input()
            inputing = input("""You are entering the forest heading to the ship, What do you want to ride.
            choose:
            -1 Horse 
            -2 Bicycle 
            """).lower()
            # The following if you chose "1" you will ride a "Horse" 2 will ride a "Bicycle".
            if inputing == "1":
                print("You are taking the " + roadDirection + " Your riding a Horse and your tool is Scissor")
                inputing = input("\n\n Remember! Rock beat birds, Paper beats cold beast, and Scissor beat beasts." + "(To continue, Click Enter)" +"""\n\nYou are on your way on your horse and you see a laying tree in your way What are you going to do?...
                choose:
                -1 Avoid it 
                -2 ignore it
                """).lower()
                if inputing == "1" and roadDirection[0]:
                    inputing = input("You did well by avoiding it! you can continue your journy" + """You are about to leave the forest... there is a bird attacking you... what are you going to do
                    choose:
                    -1 attack the bird back with Rock (P.S. Birds quite aggressive)
                    -2 ignore it 
                    """).lower()
                    if inputing == "1":
                        print("You did well your choice is wise...")
                        print(resultStatment[0])
                        pauseTime("")
                        print("\n\n")
                        print(restarting())
                    elif inputing == "2":
                        print("Your chose was wrong the bird attacked you and injured you, you no longer can continue\n\n")
                        pauseTime("")
                        print(resultStatment[1])
                        print("\n\n")
                        pauseTime("")
                        print(restarting())
                    else:
                        print(invalid())
                elif inputing == "1" and roadDirection[1]:
                    print("You did well by avoiding it! you can continue your journy ")
                    inputing = input()
                    inputing = input("""You are about to leave the forest... there is a beast walking around you... what are you going to do
                    choose:
                    -1 attack the beast back with Rock (P.S. beasts can't see or hear they only attack once you make noise)
                    -2 Pause and wait for them to pass by 
                    """).lower()
                    if inputing == "1":
                        print("Your chose was wrong the Beasts attached you and injured you, you no longer can continue\n\n")
                        pauseTime("")
                        print(resultStatment[1])
                        print("\n\n")
                        pauseTime("")
                        print(restarting())
                    elif inputing == "2":
                        print("You did well your choice is wise...\nbeasts passed by with no damages")
                        pauseTime("")
                        print(resultStatment[0])
                        print("\n\n")
                        pauseTime("")
                        print(restarting())
                    else:
                        print(invalid())                        
                elif inputing == "2" and roadDirection[0]:
                    inputing = input("Almost was a risky choice but do not worry about it, Your hourse was able to avoid it!"+ """You are about to leave the forest... there is a bird attacking you... what are you going to do
                    choose:
                    -1 attack the bird back with Rock (P.S. Birds quite aggressive)
                    -2 ignore it 
                    """).lower()
                    if inputing == "1":
                        print("You did well your choice is wise...")
                        print(resultStatment[0])
                        pauseTime("")
                        print("\n\n")
                        print(restarting())
                    elif inputing == "2":
                        print("Your chose was wrong the bird attacked you and injured you, you no longer can continue\n\n")
                        pauseTime("")
                        print(resultStatment[1])
                        print("\n\n")
                        pauseTime("")
                        print(restarting())
                    else:
                        print(invalid())
                elif inputing == "2" and roadDirection[1]:
                    print("It was a risky choice, Your hourse was not able to avoid it!")
                    print("Your chose was wrong the bird attacked you and injured you, you no longer can continue\n\n")
                    pauseTime("")
                    print(resultStatment[1])
                    print("\n\n")
                    pauseTime("")
                    print(restarting())
                else:
                    print(invalid()) 
            elif inputing == "2":  # you ride a Bicycle
                print("You are taking the " + roadDirection + " Your riding a Bicycle and your tool is Scissor")
                inputing = input(""""\n\nRemember! Rock beat birds, Paper beats cold beast, and Scissor beat beasts"+ " (To continue, Click Enter)\n\n\n You are on your way on your Bicycle and you see a laying tree in your way What are you going to do?...
                choose:
                -1 Avoid it 
                -2 ignore it
                """).lower()
                if inputing == "1" and roadDirection[0]:
                    print("You did well by avoiding it! you can continue your journy ")
                    pauseTime("")  # continue with the game     
                    inputing = ""
                    inputing = input()
                    inputing = input("""You are about to leave the forest... there is a bird attacking you... what are you going to do
                    choose:
                    -1 attack the bird back with Rock (P.S. Birds quite aggressive)
                    -2 ignore it 
                    """).lower()
                    if inputing == "1":
                        print("You did well your choice is wise...")
                        pauseTime("")
                        print(resultStatment[0])
                        print("\n\n")
                        pauseTime("")
                        print(restarting())
                    elif inputing == "2":
                        print("Your chose was wrong the bird attacked you and injured you, you no longer can continue\n\n")
                        pauseTime("")
                        print(resultStatment[1])
                        print("\n\n")
                        pauseTime("")
                        print(restarting())
                    else:
                        print(invalid())
                elif inputing == "1" and roadDirection[1]:
                    print("You did well by avoiding it! you can continue your journy, (To continue click Enter )")
                    inputing = input("""You are about to leave the forest... there is a beast walking around you... what are you going to do
                    choose:
                    -1 attack the beast back with Rock (P.S. beasts can't see or hear they only attack once you make noise)
                    -2 Pause and wait for them to pass by 
                    """).lower()
                    if inputing == "1":
                        print("Your chose was wrong the Beasts attached you and injured you, you no longer can continue\n\n")
                        pauseTime("")
                        print(resultStatment[1])
                        print("\n\n")
                        pauseTime("")
                        print(restarting())
                    elif inputing == "2":
                        print("You did well your choice is wise..." + pauseTime("") + "beasts passed by with no damages")
                        pauseTime("")
                        print(resultStatment[0])
                        print("\n\n")
                        pauseTime("")
                        print(restarting())
                    else:
                        print(invalid())                        
                elif inputing == "2" and roadDirection[0]:
                    print("Almost was a risky choice but do not worry about it, Your Bicycle was able to smoothly ride over it!")
                    pauseTime("")
                    print(resultStatment[0])
                    print("\n\n")
                    pauseTime("")
                    print(restarting())
                elif inputing == "2" and roadDirection[1]:
                    print("It was a risky choice, Your Bicycle was not able to cope with the curves!,(To continue click Enter)")
                    inputing = ""
                    inputing = input()
                    inputing = input("""You are about to leave the forest... there is a beast walking around you... what are you going to do
                    choose:
                    -1 attack the beast back with Rock (P.S. beasts can't see or hear they only attack once you make noise)
                    -2 Pause and wait for them to pass by 
                    """).lower()
                    if inputing == "1":
                        print("Your chose was wrong the Beasts attached you and injured you, you no longer can continue\n\n")
                        pauseTime("")
                        print(resultStatment[1])
                        print("\n\n")
                        pauseTime("")
                        print(restarting())
                    elif inputing == "2":
                        print("You did well your choice is wise..." + pauseTime("") + "beasts passed by with no damages")
                        pauseTime("")
                        print(resultStatment[0])
                        print("\n\n")
                        pauseTime("")
                        print(restarting())
                    else:
                        print(invalid())     
                else:
                    print(invalid()) 
            else:  # invalid choice
                print(invalid())
        else:
            print(invalid())
    elif inputing.lower() == "no":  # Exit the game
        print(leave())
    else:  # Any Other inputs invalid
        print(invalid())
start()