



print()
print('--------------------------------')
print()

pl_name = input('Greetings Adventurer! Please enter your name below:\n\n').capitalize()

print()
print('-------------------------------')
print()   

choice_1 = input(f'Hello {pl_name}, It is a pleasure to meet you. Would you like to play a game?\n\nYES/NO: ').capitalize()
trapped = False

if choice_1 == 'Yes':

    print()
    print('----------Character---------')
    print()
    # Give user a  description
    print('You are a Warrior. Clad in a suit of platemail and wielding a long-sword\nand shield, few men can stand against you, but you are not hunting men,\nyou are hunting monsters.\n\nYou have 25 Hit Points')
    # Break line for readability
    print()
    print('--------------Start---------')
    print()
    choice_2 = input('Your adventure starts at the entrance to an ancient tomb, untouched by man\nfor millenia, where you have tracked a monster that has been preying on the\nlocal village for the better half of the past year. There are runes etched\ninto the surface of the door and it appears to be unlocked.\n\nA long time ago in a galaxy far, far away, a farm boy on a desert planet dreamed\nof joining a rebellion and saving a princess from a dark lord, and thus,\none of the most successful cinematic sagas of all time was born...\nDo you wish to OPEN the door, or EXAMINE the temple runes.\n\nYour Choice: ').capitalize()
    # Break line for readability
    print()
    print('-----------------------------')
    print()


    if choice_2 == 'Search':
        choice_3 = input('As you search the surrounding landscape, you come across a trap door that\nappears to lead down into the tomb. Do you wish to ENTER the trap door or\nBLOCK it off to prevent anything from inside escaping and return to the\nmain entrance?\n\nYour Choice: ').capitalize()
        # Break line for readability
        print()
        print('---------------------------------------------------------------------------')
        print()
        if choice_3 == 'Enter':
            choice_4 = input('You slip into a dark cave and find yourself face to face with your target; \na large half snake, half woman known only as "Marilith." Do you wish to\nATTACK or attempt to SUBDUE her?\n\nYour Choice: ').capitalize()
            # Break line for readability
            print()
            print('---------------------------------------------------------------------------')
            print()
            if choice_4 == 'Attack':
                print('Your blade strikes true as the Marilith falls before you.')
                # Break line for readability
                print()
                print('---------------------------------------------------------------------------')
                print('CONGRATULATIONS! You have slain the monster terrorizing the nearby village.')
                print('---------------------------------------------------------------------------')
                print()
                # Break line for readability
                print('---------------------------------------------------------------------------')
                print('Stay tuned for further adventures!')
                print('---------------------------------------------------------------------------')
                print() 

       

          


                
            
        elif choice_3 == 'Shield':
            print('You raise your shield just in time to absorb the massive blow. You are knocked back\na few feet from the force but have bought yourself a few, much needed,\nseconds to react.\n\nYou still have 15 Hit Points')
            # Break line for readability
            print()
            print('---------------------------------------------------------------------------')
            print()
            
            
        elif choice_3 == 'Speak':
            print('Realizing that the prey you seek slithers across the ground and does not\nhave feet to run with, you shout, "halt! Whoever you are, I mean you no harm!\n\nThe man replies, "the Marilith has fled deeper into the cave. Come, join\nme in finishing her off."')
            # Break line for readability
            print()
            print('---------------------------------------------------------------------------')
            print()
            if trapped == True:
                print('As you enter the final part of the cave, you find the Marilith attempting\nto escape through the trap door you blocked off earlier. Your new friend\ngrabs her by the tail and slams her to the ground in font of you as you\ndeliver the final coup de grâce. The two of you lop off the head and head\nback to town to collect the bounty and celebrate.')
                print('Your blade strikes true as the Marilith falls before you.')
                # Break line for readability
                print()
                print('---------------------------------------------------------------------------')
                print('CONGRATULATIONS! You have slain the monster terrorizing the nearby village.')
                print('---------------------------------------------------------------------------')
                print()
                # Break line for readability
                print('---------------------------------------------------------------------------')
                print('Stay tuned for further adventures!')
                print('---------------------------------------------------------------------------')
                print()
            else:
                print('As you enter the final part of the cave, you find the Marilith escaping\nthrough a trap door in the ceiling towards the back. A loud *thud* shortly\nfollows as the door is blocked from the other side.')
                # Break line for readability
                print()
                print('---------------------------------------------------------------------------')
                print('OH NO! The monster has escaped. Better luck next time!')
                print('---------------------------------------------------------------------------')
                print()
                # Break line for readability
                print('---------------------------------------------------------------------------')
                print('Stay tuned for further adventures!')
                print('---------------------------------------------------------------------------')
                print()
        else:
            print('Invalid choice, please try again.')
    elif choice_2 == 'Examine':
        choice_3 = input('As you examine the runes, you can see they are meant to be a trap. Though\nthe finer points of how they work elude you, you do know that it will\nexplode if you just open the door. What is even more disturbing however,\nis that you have confirmed that the runes are freshly, if crudely, etched.\nDo you wish to try and SNEAK past the trap or SUFFER the\ntrap regardless of the outcome?\n\nYour Choice: ').capitalize()
        # Break line for readability
        print()
        print('---------------------------------------------------------------------------')
        print()
        if choice_3 == 'Sneak':
            print('You manage to get yourself past the runes without an explosion to the face\n\nYou still have 25 Hit Points.')
            print()
            print('---------------------------------------------------------------------------')
            print()
            
        elif choice_3 == 'Suffer':
            print('As you open the door, the runes shine a bright blue hue and explode in\nyour face. You take the full brunt of the damage and are\ntemporarily blinded from the explosion\n\nYou now have 10 Hit Points.')
            # Break line for readability
            print()
            print('---------------------------------------------------------------------------')
            print()
            choice_3 = input('As you reel from the shock of the explosion, still unable to see straight,\nyou hear thundering footsteps rushing towards you yelling a battlecry.\nDo you wish to STRIKE blindly towards the sound, raise your SHIELD in an\nattempt to block the oncoming attack, or SPEAK to your attacker?\n\nYour Choice: ').capitalize()
            # Break line for readability
            print()
            print('---------------------------------------------------------------------------')
            print()
            if choice_3 == 'Strike':
                print('As you strike wildly, you feel your sword thrust into open space. As the\nrealization that you have missed your target sets in, a heavy weight comes\ncrashing down onto your arm and knocks your sword out of your hand.\n\nYou now have 10 Hit Points')
                # Break line for readability
                print()
                print('---------------------------------------------------------------------------')
                print()
                
                    
            elif choice_3 == 'Shield':
                print('You raise your shield just in time to absorb the massive blow. You are knocked back\na few feet from the force but have bought yourself a few, much needed,\nseconds to react.\n\nYou still have 15 Hit Points')
                # Break line for readability
                print()
                print('---------------------------------------------------------------------------')
                print()
                
                
            elif choice_3 == 'Speak':
                print('Realizing that the prey you seek slithers across the ground and does not\nhave feet to run with, you shout, "halt! Whoever you are, I mean you no harm!\n\nThe man replies, "the Marilith has fled deeper into the cave. Come, join\nme in finishing her off."')
                # Break line for readability
                print()
                print('---------------------------------------------------------------------------')
                print()
                if trapped == True:
                    print('As you enter the final part of the cave, you find the Marilith attempting\nto escape through the trap door you blocked off earlier. Your new friend\ngrabs her by the tail and slams her to the ground in font of you as you\ndeliver the final coup de grâce. The two of you lop off the head and head\nback to town to collect the bounty and celebrate.')
                    print('Your blade strikes true as the Marilith falls before you.')
                    # Break line for readability
                    print()
                    print('---------------------------------------------------------------------------')
                    print('CONGRATULATIONS! You have slain the monster terrorizing the nearby village.')
                    print('---------------------------------------------------------------------------')
                    print()
                    # Break line for readability
                    print('---------------------------------------------------------------------------')
                    print('Stay tuned for further adventures!')
                    print('---------------------------------------------------------------------------')
                    print()
                else:
                    print('As you enter the final part of the cave, you find the Marilith escaping\nthrough a trap door in the ceiling towards the back. A loud *thud* shortly\nfollows as the door is blocked from the other side.')
                    # Break line for readability
                    print()
                    print('---------------------------------------------------------------------------')
                    print('OH NO! The monster has escaped. Better luck next time!')
                    print('---------------------------------------------------------------------------')
                    print()
                    # Break line for readability
                    print('---------------------------------------------------------------------------')
                    print('Stay tuned for further adventures!')
                    print('---------------------------------------------------------------------------')
                    print()
            else:
                print('Invalid choice, please try again.')
        else:
            print('Invalid choice, please try again.')
    else:
        # If loop designed to remove a double 'invalid choice' error code when going through
        # search option at beginning of code due to the 2 separate if loops. I'm sure there 
        # is a better way to do my overall loops with while statements but I couldn't get them
        # to work how I wanted them to so this at least works.
        if choice_2 != 'Search':
            print('Invalid choice, please try again.')

elif choice_1 == 'No':
    # Break line for readability
    print()
    print('---------------------------------------------------------------------------')
    print(f'Well, your loss, I guess. Goodbye, {pl_name}.')
    print('---------------------------------------------------------------------------')
    print()
else:
    # Break line for readability
    print()
    print('---------------------------------------------------------------------------')
    print('Invalid choice, please try again.')
    print('---------------------------------------------------------------------------')
    print()