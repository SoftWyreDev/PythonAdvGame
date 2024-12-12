print("""\nWelcome to my Choose your Own Adventure Game!
      Enter "x" to exit the game.""")

first_choice = None
second_choicev1 = None
second_choicev2 = None
second_choicev3 = None
player_class = None
player_name = ""
choice = None
gameRunning = True

while gameRunning:
    choice = None
    while player_class is None:
        player_class = input("""\nChoose your class by number from the list below:
1: Knight 
2: Thief 
3: Mage
4: Archer 
Choice: """)

        if player_class == "1":
            print("\nWelcome Knight, I hope you are well equipped.")
            

        elif player_class == "2":
            print("\nWelcome Thief, I hope you have brought your wits.")

        elif player_class == "3":
            print("\nWelcome Mage, I hope you have studied well.")

        elif player_class == "4":
            print("\nWelcome Archer, I have you have a steady hand.")

        elif player_class.lower() == "x":
            print("\nYou have exited the game.")
            exit()

        else:
            print("\nInvalid choice, try again.")
            player_class = None
    
    # Choose Name
    while player_name == "":
        player_name = input("""What would you like to be called?\nEnter Name: """)

    
    print("""\nYou awaken in the back of a horse carriage riding through the dense forest on a foggy morning to the sound of ravens cackling above. You look over and see two scraggly
looking men wearing torn clothes in the front of the carriage sitting next to each other guiding the horses. You glance out the back and look around to see nothing but a small wooden
cabin in the distance behind you and smoke from a campsite in a different section of the woods no where near where you are headed.""")
    
    # First Choice
    while first_choice is None:
        first_choice = input("""\nWhat is your plan of action?:
1: Try to talk to the drivers and ask what's going on. 
2: Attack the drivers and attempt to steal the carriage. 
3: Try to escape the carriage and run into the forest. 
Choice: """)

        if first_choice == "1":
            print("""\nAs soon as you speak up and they notice that you are awake, they yell at you in an esoteric language. When they look back at you, you notice something wrong with their faces. It's as if
they have been turned upside down. As you are in shock, one of them sprays you with fine mist from a canister and you doze back off into a deep sleep.""")

        elif first_choice == "2":
            if player_class == "1":
                print("\nYou are a Knight fuck em up.")
            if player_class == "2":
                print("\nYou are a Thief fuck em up.")
            if player_class == "3":
                print("\nYou are a Mage shit on.")
            if player_class == "4":
                print("\nYou are an Archer shit on.")

        elif first_choice == "3":
            print("\nYou jump out of the back of the carriage as it is rolling and make a run for it into the trees.")

        elif first_choice.lower() == "x":
            print("\nYou have exited the game.")
            exit()

        else:
            print("\nInvalid choice, try again.")
            first_choice = None
            
    gameRunning = False        

    # Second Choice v1 Talking to Drivers
    if first_choice == "1":
        print("\nAfter a long while, you wake up feeling fucked. They did lots to you.")
        while second_choicev1 is None:
            second_choicev1 = input("""\nWhat is your plan of action?:
1: Invade. 
2: Hide. 
3: Kill. 
Choice: """)

        if second_choicev1 == "1":
            print("""\n""")

        elif second_choicev1 == "2":
            print("")

        elif second_choicev1.lower() == "x":
            print("\nYou have exited the game.")
            exit()

        else:
            print("\nInvalid choice, try again.")
            second_choicev1 = None

    # Second Choice v2 Attacking Drivers
    if first_choice == "2" and (player_class == "1" or player_class == "2"):
        print("\nYou survived attacking the drivers.")
        
        while second_choicev2 is None:
            second_choicev2 = input("""\nWhat is your plan of action?:
1: Hunt. 
2: Live. 
3: Eat. 
Choice: """)

        if second_choicev2 == "1":
            print("")

        elif second_choicev2 == "2":
            print("")

        elif second_choicev3 == "3":
            print("")


        elif second_choicev2.lower() == "x":
            print("\nYou have exited the game.")
            exit()

        else:
            print("\nInvalid choice, try again.")
            second_choicev2 = None

    elif first_choice == "2" and (player_class == "3" or player_class == "4"):
        print("\nYou died attacking the drivers.")
        exit()

    # Second Choice v3 Escaping Drivers
    if first_choice == "3":
        print("\nYou made it out into the woods")
        while second_choicev3 is None:
            second_choicev3 = input("""\nWhat is your plan of action?:
1: Hunt. 
2: Live. 
3: Eat. 
Choice: """)

        if second_choicev3 == "1":
            print("")

        elif second_choicev3 == "2":
            print("")

        elif second_choicev3 == "3":
            print("")


        elif second_choicev3.lower() == "x":
            print("\nYou have exited the game.")
            exit()

        else:
            print("\nInvalid choice, try again.")
            second_choicev3 = None