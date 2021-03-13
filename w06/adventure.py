

#######################
# Clear the terminal
clear = chr(27) + "[2J"
print(clear)
#######################


d = "-" * 45

print("Guidlines:\n\nType the capitalized word of the choice you'd like to follow.\n")

print(
    f"""{d}\n\nThis is a simulation training Jedi. 
You find yourself on a road you've \nnever expect..."""

)
input("\nPress ENTER to continue your adventure...\n\n\n")
print(clear)


##############
# The option with 3 choices
###############
initial_choice = """
\nWelcome Master Jedi\n\npick one of this options LEFT or RIGHT (or QUIT)?
\n\n\n


"""
 



#############
# LEFT
##############

# LEVEL_1 from initial_choice
LEFT = """
If you pick this path, you hear a noise, Monsters 
gather round you.\nDo you RUN or FIGHT like a warrior?
\n\n\n\n\
"""

# LEVEL_2 from LEFT
RUN = """
You run for your life but fight Bro!. You find a image the wall.\n\n\nHey try to CHECK the image, 
or just CRY it thinking this is all a dream anyways?"
\n\n\n\n\
"""

# LEVEL_2 from LEFT
FIGHT = """
You remember that you are a Jedi and have a lightsaber. You slowly move 
you hand to your weapon. As the monster close in, you quickly USE out the 
lightsaber and prepare to defend yourself, or KEEP your hand ready?
\n\n\n\n\
"""

# LEVEL_3 
CHECK = """
This image show you that you are a loser...  The end.
\n\n\n\n\
"""

# LEVEL_3 
CRY = """
you are not a Jedi sorry Bro! ...you're dead. The end.
\n\n\n\n\
"""

# LEVEL_3 
USE = """
The Monster are coming for you.... You've lost the battle. 
You die. The end.
\n\n\n\n\
"""

# LEVEL_3 f
KEEP = """
Bro! no worries.... it is a dream!
Poof! You're back, safe and sound. The end.
\n\n\n\n\
"""

##################
# RIGHT
##################

# LEVEL_1 from initial_choice
# RIGHT
RIGHT = """
Well warrior is time to investigate... As you approach, you have a decision to make. Do 
you SNOOP around a bit, or GO up to the first person you see and try to get 
some answers?
\n\n\n\n\
"""

# LEVEL_2 from RIGHT
SNOOP = """
Go to the spaceship and...TRY to go in 
or head towards ANOTHER spaceship?
\n\n\n\n\
"""

# LEVEL_2 from RIGHT
GO = """
Now look's like you are ready for the challenge.... You're 
amazed! Do you RECITE the same chant, or keep LOOKING for someone else.
\n\n\n\n\
"""

# LEVEL_3 from SNOOP
TRY = """
You easily pass through, going in with no problem. OH no is an enbush your are in danger.... sorry to many Robots around you\nThe end.
\n\n\n\n\
"""

# LEVEL_3 from SNOOP
ANOTHER = """
You head off towards another building, but as you are snooping around, you hear
a voice call your name. Suddenly, you're captured, and wisped away to a 
Blackhawk Helicopter... Your countries armed forces have rescued you, you are 
no longer at risk of becoming a hostage, and upon returning to your native 
soil, you become a national icon and hero. The end.
\n\n\n\n\
"""

# LEVEL_3 from GO
RECITE = """
Fight like a real Jedi even if you live depende of it..... sorry Master Jedi. The end.
\n\n\n\n\
"""

# LEVEL_3 from GO
LOOKING = """
You continue looking fighting with the courage of a master Jedi... well done never give up 
The end.
\n\n\n\n\
"""









def get_input(question):
    print(clear)
    print(d)
    choice = input(f"{question}")
    return choice.upper()


inital = get_input(initial_choice)


an_error = f"""
\nMake sure to match the spelling of the capital word of your choice.
That input was incorrect.
"""






if inital == "LEFT" or inital == "RIGHT" or inital == "QUIT":
    if inital == "LEFT" or inital == "RIGHT":
        if inital == "LEFT":
            x = get_input(LEFT)
            if x == "RUN" or x == "FIGHT":
                if x == "RUN":
                    x = get_input(RUN)
                    if x == "CHECK" or x == "CRY":
                        if x == "CHECK":
                            print(clear)
                            print(d)
                            print(CHECK)
                        if x == "CRY":
                            print(clear)
                            print(d)
                            print(CRY)
                    else:
                        print(an_error)



                elif x == "FIGHT":
                    x = get_input(FIGHT)
                    if x == "USE" or x == "KEEP":
                        if x == "USE":
                            print(clear)
                            print(d)
                            print(USE)
                        if x == "KEEP":
                            print(clear)
                            print(d)
                            print(KEEP)
                    else:
                        print(an_error)
                else:
                    print(an_error)
            else:
                print(an_error)


        elif inital == "RIGHT":
            x = get_input(RIGHT)
            if x == "SNOOP" or x == "GO":
                if x == "SNOOP":
                    x = get_input(SNOOP)
                    if x == "TRY" or x == "ANOTHER":
                        if x == "TRY":
                            print(clear)
                            print(d)
                            print(TRY)
                        elif x == "ANOTHER":
                            print(clear)
                            print(d)
                            print(ANOTHER)
                    else:
                        print(an_error)


                elif x == "GO":
                    x = get_input(GO)
                    if x == "RECITE" or x == "LOOKING":
                        if x == "RECITE":
                            print(clear)
                            print(d)
                            print(RECITE)
                        elif x == "LOOKING":
                            print(clear)
                            print(d)
                            print(LOOKING)
                    else:
                        print(an_error)
                else:
                    print(an_error)
            else:
                print(an_error)
        else:
            print(an_error)



    elif inital == "QUIT":
        print(
            f"""\nThanks for trying ... 
You may not ready but sorry!\n"""
        )
else:
    print(an_error)