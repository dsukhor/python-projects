import random
import time
def choose_metal(metal = "mithril"): # Function to choose a metal with a default argument for "mithril"
    clean_metal = metal.strip().lower()
    metals = ("mithril","adamantium","vibranium","orichalcum")
    while True:
        if clean_metal in metals:
            if clean_metal == "mithril":
                print("\n------------------------------\n")
                print("You chose mithril.")
                return 9
            elif clean_metal == "adamantium":
                print("\n------------------------------")
                print("You chose adamantium.")
                return 7
            elif clean_metal == "vibranium":
                print("\n------------------------------")
                print("You chose vibranium.")
                return 5
            elif clean_metal == "orichalcum":
                print("\n------------------------------")
                print("You chose orichalcum.")
                return 3
        if clean_metal not in metals: # If the input does not match any available metals, prompt again
            print("\nOops! Try typing in a available metal instead.\n")
            clean_metal = input("Choose metal: ").strip().lower()

def forge(power, player_name): # Function to forge a weapon, taking the player's chosen power and name
    weapons = {"mace": "knockback", "spear": "reach", "hammer": "stun"}
    rarities = {"common": (1,"3 out of 6"), "rare": (3,"2 out of 6"), "legendary": (6,"1 out of 6")}
    print("\n------------------------------")
    print("\n"+player_name+"! Get ready for some forging.")
    print("\nWeapons Avaliable\n")
    for key, value in weapons.items():
        print(key.upper()+":\t"+value+" effect.\n")
    while True:
        weapon = input("\nChoose a weapon: ").strip().lower()
        print("\n------------------------------")
        if weapon in weapons:
            print("\nYou chose the",weapon)
            time.sleep(1)
            print("\nA six sided die will be rolled, guess a number to determine the weapons rarity.\n")
            print("---------------------------------------")
            for key,value in rarities.items():
                print(value[1],"will be",key.upper(),"(+"+str(value[0])+" POWER)")
            print("---------------------------------------")
            print("\nRolling...\n")
            time.sleep(1)
            dice = []
            while len(dice) < 6: # Fills dice list with unique numbers 1 - 6 and assigns them to different rarities
                random_roll = random.randint(1,6)
                if random_roll not in dice:
                    dice.append(random_roll)
            common_num = dice[0:3]
            rare_num = dice[3:5]
            legendary_num = dice[5]
            print("Dice rolled.\n")
            while True: # Prompt user for their guess
                try:
                    guess = int(input("Your guess: "))
                    if guess < 1 or guess > 6:
                        print("\nOnly 1 through 6!\n")
                        continue
                    else:
                        break # Valid guess, break out of the loop
                except: # Catch specific exception for invalid input
                    print("\nAn error happened, retry...\n")
                    continue
            print("\n---------------------------------\n")
            if guess in common_num:  # Determine the rarity based on the guess
                rarity = rarities["common"]
                rarity_name = "common"
                print("You got a COMMON!")
                break
            if guess in rare_num:
                rarity = rarities["rare"]
                rarity_name = "rare"
                print("You got a RARE!")
                break
            if guess == legendary_num:
                rarity = rarities["legendary"]
                rarity_name = "legendary"
                print("You got a lEGENDARY!")
                break
        if weapon not in weapons: # If the input weapon is not recognized, prompt again
            print("\nOops! You made a mistake, retry...")
            continue
    time.sleep(1)
    print("\nForging Complete!")
    print("\n---------------------------------\n")
    stats = [power + rarity[0], rarity_name, weapon, weapons[weapon]]     # Create weapon stats based on power and rarity
    return stats 
            
def describe_weapon(stats): # Function to describe the forged weapon
    description = "\tWEAPON DESCRIPTION\n---------------------------------\nWEAPON: "+str(stats[2])+"\nPOWER: "+str(stats[0])+"\nSPECIAL EFFECT: "+str(stats[3])+"\nRARITY: "+str(stats[1])+"\n---------------------------------"
    return description


print("\nYou are forging a weapon. Choose a metal below to start.\n") # Start of the program execution
print("mithril (+9 POWER), adamantium (+7 POWER), vibranium (+5 POWER), orichalcum (+3 POWER).\n")
# Capture user input for metal selection
metal_input = input("Choose metal (or press Enter for default 'mithril'): ").strip().lower()
# Use the default argument if the user pressed Enter
if metal_input == "":
    power = choose_metal()  # Call without argument to use the default "mithril"
else:
    power = choose_metal(metal_input)  # Call with user input
stats = forge(power, player_name = "Warrior")  # Using keyword argument for player name
description = describe_weapon(stats)  # Get the weapon description
print(description)