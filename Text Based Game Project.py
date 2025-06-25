from colorama import Fore
import random
import time
health = 10
potion = ["potion",1,3] # name, cost, heal amount
gold = 0
sword = ["sword",4,5] # item name, gold cost, damage
dagger =["dagger",0,3] # this is a starter weapon
bow = ["bow",3,4]
spear = ["spear",5,6]
inventory = [dagger]
print(Fore.RED,"    _                                     "+"  _							")
print("    | |                                    "+" | |							")
print("  __| |_   _ _ __   __ _  ___  ___  _ __   "+" | |_ _____      _____ _ __ 	")
print(" / _` | | | | '_ \\ / _` |/ _ \\/ _ \\| '_ "+"\\   | __/ _ \\ \\ /\\ / / _ \\ '__|	")
print("| (_| | |_| | | | | (_| |  __/ (_) | | | | "+" | || (_) \\ V  V /  __/ |		")  
print(" \\__,_|\\__,_|_| |_|\\__, |\\___|\\___/|_|"+" |_|   \\__\\___/ \\_/\\_/ \\___|_|		") 
print("                    __/ |                 								")
print("                   |___/                    								")
print(Fore.BLACK)
print("-----------------------------------------------------------------------------------------")
print("| Welcome to dungeon tower, you will encounter a random enemy on each floor, defeat it. |")
print("| You will start off with a dagger and ten health, if health goes to zero you lose.     |")
print("| You will be able to buy better weapons/health potions using gold earned from enemies. |")
print("| There are three floors, get to the end of the dungeon to win!                         |")
print("| You can also block attacks 2 times.                                                   |")
print("| Hleath potions heals for 3 health but your health cannot go above 10.                 |")
print(Fore.RED+"| To quit the game type quit in any of the prompts.                                     |"+Fore.BLACK)
print("| Hint: Using shop every floor increases chances of winning.                            |")
print("-----------------------------------------------------------------------------------------")
print()
i1 = input("To continue press Enter: ")
if i1 == "quit":
    exit()
print()
d1 = ["You approach a rusted iron gate, faint groans echo beyond."]
d1.extend("You approach a rusted iron gate, faint groans echo beyond.")
d1.remove("You approach a rusted iron gate, faint groans echo beyond.")
d2 = ["Gatekeeper: \"Halt! Only the brave or the foolish tread here. Which are you, adventurer?\""]
d2.extend("Gatekeeper: \"Halt! Only the brave or the foolish tread here. Which are you, adventurer?\"")
d2.remove("Gatekeeper: \"Halt! Only the brave or the foolish tread here. Which are you, adventurer?\"")
d3 = ["You: \"Just open the gate.\""]
d3.extend("You: \"Just open the gate.\"")
d3.remove("You: \"Just open the gate.\"")
d4 = ["Gatekeeper: \"Lost souls often find themselves within. Dare to pass and face the curse of the Forgotten King?\""]
d4.extend("Gatekeeper: \"Lost souls often find themselves within. Dare to pass and face the curse of the Forgotten King?\"")
d4.remove("Gatekeeper: \"Lost souls often find themselves within. Dare to pass and face the curse of the Forgotten King?\"")
d5 = ["You: \"Lets go.\""]
d5.extend("You: \"Lets go.\"")
d5.remove("You: \"Lets go.\"")
for x in d1:          # prints out the dialogue 
    print(x, end = "")
    time.sleep(0.03)
print("\n")
for x in d2:
    print(x, end = "")
    time.sleep(0.03)
print("\n")
for x in d3:
    print(x, end = "")
    time.sleep(0.03)
print("\n")
for x in d4:
    print(x, end = "")
    time.sleep(0.03)
print("\n")
for x in d5:
    print(x, end = "")
    time.sleep(0.03)
print("\n")
print()
floors = 1
zombie  = [8,2,4] # first number is health, second number is damage, third is gold
skeleton = [7,2,3]
vampire = [9,3,5]
enemies = [zombie,skeleton,vampire]
shop = ["sword","bow","spear","potion"] #creates shop
inventory = [] # back ground inventory
viewInventory = [] # inventory for viewing
while floors < 4:
    print("_______________________________________________________")
    print()
    print("You enter floor",Fore.BLUE,floors)
    print()
    i2 = ""
    i3 = ""
    i4 = ""
    shieldBlocks = 2
    randomEnemy = random.choice(enemies) #generates random enemy for each floor 
    if randomEnemy == zombie:     # assigns display names
        enemyName = "zombie"
    elif randomEnemy == skeleton:
        enemyName = "skeleton"
    elif randomEnemy == vampire:
        enemyName = "vampire"
    print("You encounter a "+Fore.RED+enemyName,Fore.BLACK)
    print()
    print("Enemy health: " + Fore.RED + str(randomEnemy[0]),"\n\n" + Fore.BLACK + "Enemy damage: " + Fore.RED + str(randomEnemy[1]))
    print(Fore.BLACK)
    while randomEnemy[0] > 0: # battling the enemy loop
        print("_______________________________________________________")
        print()
        if health > 0: # displays stats
            print("Inventory:",viewInventory)
            print()
            print(Fore.BLUE + "YOUR HEALTH: " + Fore.RED + str(health))
            print()
            print(Fore.BLUE + "ENEMY HEALTH: " + Fore.RED + str(randomEnemy[0]),Fore.BLACK)
            print()
        i2 = input("Attack it or block it or use potion? (a/b/p): ")
        if i2 == "quit":
            exit()
        print()
        if i2 != "a" and i2 != "b" and i2 != "p" :   # prevents errors
            print(Fore.RED,"Please enter a valid input!",Fore.BLACK)
            continue
        if i2 == "a":
            while True:
                i9 = input("What weapon would you like to use? (You start off with a dagger but you will have to buy the other weapons.) \n\nFor dagger type d\n\nFor sword type s\n\nFor bow type b\n\nFor spear type sp\n\nEnter weapon: ")
                print()
                if i9 == "quit":
                    exit()
                if i9 == "d":              # the following code is attacking options 
                    randomEnemy[0] -= dagger[2]
                    dEnemyHealth = randomEnemy[0]
                    if dEnemyHealth < 1:
                        dEnemyHealth = 0
                    print("You dealt " + Fore.RED + str(dagger[2]) + Fore.BLACK + " damage! The " + Fore.RED + enemyName + Fore.BLACK + " has " + Fore.RED + str(dEnemyHealth) + Fore.BLACK + " health left.")
                    print()
                    break
                if i9 == "s" and sword in inventory:
                    randomEnemy[0] -= sword[2]
                    dEnemyHealth = randomEnemy[0]
                    if dEnemyHealth < 1:
                        dEnemyHealth = 0
                    print("You dealt " + Fore.RED + str(sword[2]) + Fore.BLACK + " damage! The " + Fore.RED + enemyName + Fore.BLACK + " has " + Fore.RED + str(dEnemyHealth) + Fore.BLACK + " health left.")
                    print()
                    break
                elif sword not in inventory:
                    if i9 == "b" and bow in inventory:
                        randomEnemy[0] -= bow[2]
                        dEnemyHealth = randomEnemy[0]
                        if dEnemyHealth < 1:
                            dEnemyHealth = 0
                        print("You dealt " + Fore.RED + str(bow[2]) + Fore.BLACK + " damage! The " + Fore.RED + enemyName + Fore.BLACK + " has " + Fore.RED + str(dEnemyHealth) + Fore.BLACK + " health left.")
                        print()
                        break
                    elif bow not in inventory:
                        if i9 == "sp" and spear in inventory:
                            randomEnemy[0] -= spear[2]
                            dEnemyHealth = randomEnemy[0]
                            if dEnemyHealth < 1:
                                dEnemyHealth = 0
                            print("You dealt " + Fore.RED + str(spear[2]) + Fore.BLACK + " damage! The " + Fore.RED + enemyName + Fore.BLACK + " has " + Fore.RED + str(dEnemyHealth) + Fore.BLACK + " health left.")
                            print()
                            break
                        elif spear not in inventory:
                            if True:
                                print(Fore.RED+"Please enter a valid input or you do not own this weapon!"+Fore.BLACK)
                                print()
                                continue
        elif i2 == "b" and shieldBlocks > 0: # for blocking attacks, only allows 2 blocks
            shieldBlocks -= 1
            print("You blocked the attack! You have " + Fore.RED + str(shieldBlocks) + Fore.BLACK + " shield blocks left.")
            print()
            continue
        if i2 == "b" and shieldBlocks <= 0:
            print("You don't have any blocks left")
        if i2 == "p" and potion in inventory: # for using health potions, health isnt allowed to go above 10, prints amount of potions left
            health += 3
            inventory.remove(potion)
            if "potion" in viewInventory:
                viewInventory.remove("potion")
            print("You used a health potion and healed 3 health")
            if health > 10:
                health = 10
                print()
                print(Fore.RED,"You cannot go over 10 health!",Fore.BLACK)
            print()
            continue
        if i2 == "p" and potion not in inventory:     # if no more health potions left 
            print("You do not have health potions.")
            print()
            continue
        health -= randomEnemy[1]
        if health < 1:  # if health falls below 1 the player loses the game
            health = 0
            print("The "+Fore.RED+enemyName+Fore.BLACK+" deals "+Fore.RED+str(randomEnemy[1])+Fore.BLACK+" damage to you! You have "+Fore.RED+str(health)+Fore.BLACK+" health left.")
            print()
            print(Fore.RED,"YOU DIED")
            exit()
        print("The "+Fore.RED+enemyName+Fore.BLACK+" deals "+Fore.RED+str(randomEnemy[1])+Fore.BLACK+" damage to you! You have "+Fore.RED+str(health)+Fore.BLACK+" health left.")
        print()
        if randomEnemy[0] < 1:
            print("_______________________________________________________")
            print()
            print("You defeated the " + Fore.RED + enemyName + Fore.BLACK + ". you earned " + Fore.YELLOW + str(randomEnemy[2]) + Fore.BLACK + " gold.")
            print()
            floors += 1
            gold += randomEnemy[2]
            if floors < 4:
                print("You advance to floor " + Fore.BLUE + str(floors))
                print(Fore.BLACK)
            print("_______________________________________________________")
            if floors < 4:
                print()
                print("Shop:\t",shop) 
                print()
                print("You have "+Fore.YELLOW+str(gold)+Fore.BLACK+" gold.")
                print()
            while i3 != "y" and floors < 4:
                i3 = input("Use shop? (y/n): ")   # shop option and error prevention
                if i3 == "quit":
                    exit()
                print()
                if i3 != "n" and i3 != "y":
                    print()
                    print(Fore.RED,"Please enter a valid input!",Fore.BLACK)
                    print()
                    continue
                if i3 == "n":
                    floors += 1
                    break
            while i3 == "y" and floors < 4:
                print("_______________________________________________________") # the following code shows the shop options
                print()
                print("Options:")
                print()
                print("Health potion - heal amount: "+Fore.RED+str(potion[2])+Fore.BLACK+"       Gold cost: "+Fore.YELLOW+str(potion[1])+Fore.BLACK)
                print()
                print("Sword - damage: "+Fore.RED+str(sword[2])+Fore.BLACK+"                    Gold cost: "+Fore.YELLOW+str(sword[1])+Fore.BLACK)
                print()
                print("Bow - damage: "+Fore.RED+str(bow[2])+Fore.BLACK+"                      Gold cost: "+Fore.YELLOW+str(bow[1])+Fore.BLACK)
                print()
                print("Spear - damage: "+Fore.RED+str(spear[2])+Fore.BLACK+"                    Gold cost: "+Fore.YELLOW+str(spear[1])+Fore.BLACK)
                print()
                i4 = input("What would you like to buy? sword (to buy type s), bow (to buy type b), spear (to buy type sp), health potion (to buy type p) If you don't want to buy type n: ")
                if i4 == "quit":
                    exit()
                print()
                print("_______________________________________________________")
                print()
                if i4 == "n": # goes to next floor if player doesnt want to buy
                    break
                if i4 == "s" and gold >= sword[1]:    # the following code adds weapon to inventory and removes it from shop if bought
                    if "sword" in shop:
                        shop.remove("sword")
                        gold -= sword[1]
                        inventory.append(sword)
                        viewInventory.append(sword[0])
                        print("You bought a sword.")
                        print()
                        print("You have " + Fore.YELLOW + str(gold) + Fore.BLACK + " gold left.")
                        print()
                        print("Inventory:",viewInventory)
                        print()
                        continue
                    elif "sword" not in shop:
                        print("You already bought this item")
                        print()
                        continue
                elif i4 == "b" and gold >= bow[1]:
                    if "bow" in shop:
                        shop.remove("bow")
                        gold -= bow[1]
                        inventory.append(bow)
                        viewInventory.append(bow[0])
                        print("You bought a bow.")
                        print()
                        print("You have " + Fore.YELLOW + str(gold) + Fore.BLACK + " gold left.")
                        print()
                        print("Inventory:",viewInventory)
                        print()
                        continue
                    elif "bow" not in shop:
                        print("You already bought this item")
                        print()
                        continue
                elif i4 == "p" and gold >= potion[1]: # the player can buy infinite potions
                    gold -= potion[1]
                    inventory.append(potion)
                    viewInventory.append(potion[0])
                    print("You bought a health potion.")
                    print()
                    print("You have " + Fore.YELLOW + str(gold) + Fore.BLACK + " gold left.")
                    print()
                    print("Inventory:",viewInventory)
                    print()
                    continue
                elif i4 == "sp" and gold >= spear[1]:
                    if "spear" in shop:
                        shop.remove("spear")
                        gold -= spear[1]
                        inventory.append(spear)
                        viewInventory.append(spear[0])
                        print("You bought a spear.")
                        print()
                        print("You have " + Fore.YELLOW + str(gold) + Fore.BLACK + " gold left.")
                        print()
                        print("Inventory:",viewInventory)
                        print()
                        continue
                    elif "spear" not in shop:
                        print("You already bought this item")
                        print()
                        continue
                else:
                    print(Fore.RED+"You do not have enough gold or you entered a invalid iput!"+Fore.BLACK)
                    print()
                    continue
else:
    print("\n\n\n\n")
    print("_______________________________________________________")
    print()
    # if the player wins the game
    d6 = ["\"You found the crown of the forgotten king and beat the curse!\""]
    d6.extend("\"You found the crown of the forgotten king and beat the curse!\"")
    d6.remove("\"You found the crown of the forgotten king and beat the curse!\"")
    for x in d6:
        print(x, end = "")
        time.sleep(0.03)
    print("\n")
    d7 = ["You win the game!"]
    d7.extend("You win the game!")
    d7.remove("You win the game!")
    for x in d7:
        print(x, end = "")
        time.sleep(0.03)
    print("\n")
    print(Fore.YELLOW,'                                    o')
    print(Fore.YELLOW,'                                   $\"\"$o')
    print(Fore.YELLOW,'                                  $\"  $$')
    print(Fore.YELLOW,'                                   $$$$')
    print(Fore.YELLOW,'                                   o \"$o')
    print(Fore.YELLOW,'                                  o\"  \"$')
    print(Fore.YELLOW,'             oo\"$$$\"  oo$\"$ooo   o$    \"$    ooo\"$oo  $$$\"o')
    print(Fore.YELLOW,'o o o o    oo\"  o\"      \"o    $$o$\"     o o$\"\"  o$      \"$  \"oo   o o o o')
    print(Fore.YELLOW,'\"$o   \"\"$$$\"   $$         $      \"   o   \"\"    o\"         $   \"o$$\"    o$$')
    print(Fore.YELLOW,'  \"\"o       o  $          $\"       $$$$$       o          $  ooo     o\"\"')
    print(Fore.YELLOW,'     \"o   $$$$o $o       o$        $$$$$\"       $o        \" $$$$   o\"')
    print(Fore.YELLOW,'      \"\"o $$$$o  oo o  o$\"         $$$$$\"        \"o o o o\"  \"$$$  $')
    print(Fore.YELLOW,'        \"\" \"$\"     \"\"\"\"\"            \"\"$\"            \"\"\"      \"\"\" \"')
    print(Fore.YELLOW,'         \"oooooooooooooooooooooooooooooooooooooooooooooooooooooo$\"')
    print(Fore.YELLOW,'          \"$$$$\"$$$$\" $$$$$$$\"$$$$$$ \" \"$$$$$\"$$$$$$\"  $$$\"\"$$$$')
    print(Fore.YELLOW,'           $$$oo$$$$   $$$$$$o$$$$$$o\" $$$$$$$$$$$$$$ o$$$$o$$$\"')
    print(Fore.YELLOW,'           $\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"$')
    print(Fore.YELLOW,'           $\"                                                  o')
    print(Fore.YELLOW,'           $\"$\"$\"$\"$\"$\"$\"$\"$\"$\"$\"$\"$\"$\"$\"$\"$\"$\"$\"$\"$\"$\"$\"$\"$\"$$')
    time.sleep(1)
    exit()
    
    
                    
