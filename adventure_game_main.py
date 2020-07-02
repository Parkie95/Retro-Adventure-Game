import time
import random


# Prints a message and gives a time delay.
def print_pause(msg):
    time.sleep(1.5)
    print(msg)


# Prints the intro and begins the main part of the game.
def intro(items, enemy_name, weapon):
    print_pause("You find yourself in a foggy forest, late at night.")
    print_pause(f"There are rumours of a {enemy_name} "
                "running afoot amongst the trees...")
    print_pause("To your right is an abandoned mine. It looks dark and scary.")
    print_pause("In the distance, you can just about make out a faint light "
                "coming from what looks like a disused hut...")
    print_pause("In your hand you have... a banana that you took with you "
                "for a snack before getting lost in the forest.\n")
    forest(items, enemy_name, weapon)


# Entry point into the game, sets up the variables used, including random
# weapon name and enemy name.
def play_game():
    items = []
    enemy_names = ["Wild Beast", "Stinky Turtle", "Vicious Pig", "Fat Ox"]
    weapon_names = ["Sword of Excalibur", "Mace of Darkness",
                    "Axe of Death", "Bat of Badness",
                    "Wench of the Wilderness"]
    enemy_name = random.choice(enemy_names)
    weapon = random.choice(weapon_names)
    intro(items, enemy_name, weapon)


# The forest, the neutral area where the main choices are made in the game.
def forest(items, enemy_name, weapon):
    print_pause("Enter 1 to enter the abandoned mine if you dare...")
    print_pause("Enter 2 to seek refuge in the disused hut.")
    usr_input = input("What would you like to do?\n(Please enter 1 or 2.)\n")
    # The below will go into the abandoned_mine function.
    if usr_input == "1":
        abandoned_mine(items, enemy_name, weapon)
    # The below will go into the disused hut function.
    elif usr_input == "2":
        disused_hut(items, enemy_name, weapon)
    # The below handles invalid input.
    else:
        print_pause("A squirrel looks at you like "
                    "you're crazy as you randomly "
                    "flail your arms around and nearly tear your hair out. ")
        print_pause("You regain composure and think again.")
        forest(items, enemy_name, weapon)


# The mine where the player can obtain the weapon to win the game.
def abandoned_mine(items, enemy_name, weapon):
    if weapon in items:
        print_pause("A faint howl from the mine occurs. "
                    f"You have The {weapon} and you don't feel like "
                    "risking the darkness again...")
        forest(items, enemy_name, weapon)
    else:
        print_pause("You take a deep breath and enter the abandoned mine...")
        print_pause("You hear faint bat wings flap, you almost feel like a "
                    "ghost is watching you.\nMaybe these are the "
                    "spirits of those that once worked here...")
        print_pause("You discover what most have seeked for centuries... "
                    f"The {weapon}!")
        print_pause("Even the most immortal of creatures wouldn't mess "
                    "with you now!")
        print_pause("With no further need for your once fresh banana, "
                    "you toss the blackened fruit down the mine as you exit "
                    "to the forest.")
        items.append(weapon)
        forest(items, enemy_name, weapon)


# Entry to the disused hut, where the player either wins or loses.
def disused_hut(items, enemy_name, weapon):
    if weapon in items:
        # If the player has the weapon, this will happen:
        hut_intro_1 = ("Now feeling a new level of confidence, having found "
                       f"The {weapon} (it makes you look cooler), you "
                       "approach the hut.")
        hut_intro_2 = (f"The {enemy_name} howls and looks at you viciously, "
                       "awaiting your next move.")
        hut_intro_3 = (f"Pointing the {weapon} "
                       "at the creature heroicly, you feel like "
                       "Mel Gibson in Braveheart.")
        weapon_used = f" thwack it with The {weapon} "
        result_1 = (f"Readying yourself, you thwack the {enemy_name} with "
                    f"The {weapon}!")
        result_2 = (f"Injured and defeated, the {enemy_name} runs away!")
        result_3 = ("You win! Congratulatons on defeating the "
                    f"{enemy_name}!")
    else:
        # If the player doesn't have the weapon, this will happen:
        hut_intro_1 = ("You cautiously approach the disused hut. You feel "
                       "comforted by the faint glow of the gently "
                       "swinging lantern.")
        hut_intro_2 = ("It makes an ominous scream...")
        hut_intro_3 = (f"The {enemy_name} howls and looks at you viciously, "
                       "awaiting your next move.\nPointing your banana at the "
                       "creature defensively, you hardly feel like "
                       "Dangerous Dan at this point.")
        weapon_used = " slap it with your banana "
        result_1 = (f"Slapping the {enemy_name} with your rotting banana was "
                    "never going to be a good idea was it?")
        result_2 = ("You kick yourself for doing this as the beast tears "
                    "into you for their dinner.")
        result_3 = "GAME OVER"
    print_pause(hut_intro_1)
    print_pause(f"It's the {enemy_name}!")
    print_pause(hut_intro_2)
    print_pause(hut_intro_3)
    user_not_chosen = True # Variable for the while loop condition.
    while user_not_chosen:
        # Choice to fight the enemy or retreat to the forest.
        defence_choice = input(f"Do you (1){weapon_used}or (2) run away?\n")
        if defence_choice == "1":
            print_pause(result_1)
            print_pause(result_2)
            print_pause(result_3)
            user_not_chosen = False # Sets the loop to false, choice was made.
            play_again()
        elif defence_choice == "2":
            print_pause("Playing it safe, you run like crazy "
                        "back to the forest. "
                        "Lucky you weren't followed!")
            user_not_chosen = False # Sets the loop to false, choice was made.
            forest(items, enemy_name, weapon)
        else:
            print_pause("Come on there's no time for playing!")


# Allows the player to play again or quit the game.
def play_again():
    choice = input("Would you like to play again (y/n)?\n")
    # Allows the player to play again.
    if choice == "y":
        print("Awesome! Here we go...")
        play_game()
    # Allows the player to exit the game.
    elif choice == "n":
        print_pause("Thanks for playing, goodbye!")
    # Handles incorrect input.
    else:
        print_pause("Please enter a valid answer.")
        play_again()


# Entry point to the game is called here.
play_game()
