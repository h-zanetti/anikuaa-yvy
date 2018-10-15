from random import randint

# Player
player = {"HP" : 10, "MP" : 100, "lvl" : 1, "XP" : 0, "points" : 0, "kills" : 0, "last_kill" : ""}
inventory = {}

# Classes
knight = {"HEA" : 15, "STR" : 20, "AGI" : 10, "DEX" : 10, "INT" : 5, "CHA" : 5}
mage = {"HEA" : 10, "STR" : 5, "AGI" : 10, "DEX" : 15, "INT" : 20, "CHA" : 5}
archer = {"HEA" : 10, "STR" : 5, "AGI" : 15, "DEX" : 20, "INT" : 10, "CHA" : 5}
thief = {"HEA" : 10, "STR" : 5, "AGI" : 10, "DEX" : 15, "INT" : 5, "CHA" : 20}
monk = {"HEA" : 10, "STR" : 15, "AGI" : 20, "DEX" : 10, "INT" : 5, "CHA" : 5}

# Player Info
print "Choose a name for your character:"
name = raw_input()
player["name"] = name

print "Greedings %s, choose a class to start your advanture!" % (name)
print "If you need, type 'classes' to check your options and it's attributes."
clss = "none"
# Choosing a class
while clss.lower() != "knight" and clss.lower() != "mage" and clss.lower() != "archer" and clss.lower() != "thief" and clss.lower() != "monk":
    clss = raw_input()
    if clss.lower() == "knight":
        clss = knight
        player["HP"] = player["HP"] * clss["HEA"]
        print "Welcome to Anikuaa Yvy, %s the Knight." % (name)
        break
    elif clss.lower() == "mage":
        clss = mage
        player["HP"] = player["HP"] * clss["HEA"]
        print "Welcome to Anikuaa Yvy, %s the Mage." % (name)
        break
    elif clss.lower() == "archer":
        clss = archer
        player["HP"] = player["HP"] * clss["HEA"]
        print "Welcome to Anikuaa Yvy, %s the Archer." % (name)
        break
    elif clss.lower() == "thief":
        clss = thief
        player["HP"] = player["HP"] * clss["HEA"]
        print "Welcome to Anikuaa Yvy, %s the Thief." % (name)
        break
    elif clss.lower() == "monk":
        clss = monk
        player["HP"] = player["HP"] * clss["HEA"]
        print "Welcome to Anikuaa Yvy, %s the Monk." % (name)
        break
    elif clss.lower() == "classes" or clss.lower() == "options":
        print "You have five options:"
        print "Knight:"
        print "  - Health: %s" % (knight["HEA"])
        print "  - Strength: %s" % (knight["STR"])
        print "  - Agility: %s" % (knight["AGI"])
        print "  - Intelligence: %s" % (knight["INT"])
        print "  - Dexterity: %s" % (knight["DEX"])
        print "  - Charisma: %s" % (knight["CHA"])
        print "Mage:"
        print "  - Health: %s" % (mage["HEA"])
        print "  - Strength: %s" % (mage["STR"])
        print "  - Agility: %s" % (mage["AGI"])
        print "  - Intelligence: %s" % (mage["INT"])
        print "  - Dexterity: %s" % (mage["DEX"])
        print "  - Charisma: %s" % (mage["CHA"])
        print "Archer:"
        print "  - Health: %s" % (archer["HEA"])
        print "  - Strength: %s" % (archer["STR"])
        print "  - Agility: %s" % (archer["AGI"])
        print "  - Intelligence: %s" % (archer["INT"])
        print "  - Dexterity: %s" % (archer["DEX"])
        print "  - Charisma: %s" % (archer["CHA"])
        print "Thief:"
        print "  - Health: %s" % (thief["HEA"])
        print "  - Strength: %s" % (thief["STR"])
        print "  - Agility: %s" % (thief["AGI"])
        print "  - Intelligence: %s" % (thief["INT"])
        print "  - Dexterity: %s" % (thief["DEX"])
        print "  - Charisma: %s" % (thief["CHA"])
        print "Monk:"
        print "  - Health: %s" % (monk["HEA"])
        print "  - Strength: %s" % (monk["STR"])
        print "  - Agility: %s" % (monk["AGI"])
        print "  - Intelligence: %s" % (monk["INT"])
        print "  - Dexterity: %s" % (monk["DEX"])
        print "  - Charisma: %s" % (monk["CHA"])
    else:
        print "Invalid..."
        print "Choose another class or type 'classes' to see your options and its atributes."


# Gameplay functions

# Commands
def check_command(command, lvl_UP):
    if command.lower() == "help" or command.lower() == "?":
        print "  - 'help' or '?' will show you this menu."
        print "  - 'inventory' or 'inv' will show you all your items."
        print "  - 'status' or will show you your status."
        print "  - 'attributes' or 'att' will show you your attributes."
        print "  - If you have improvement points you can use it typing 'imporve att'."
        print "  - To explore, type the direction that you would like to go. Example: 'go North'."
        print "  - To make an action, just type it. Examples: 'get item', 'drop axe', 'attack troll', 'run', etc."
    elif command.lower() == "inventory" or command.lower() == "inv":
        if len(inventory) == 0:
            print "You are naked..."
        else:
            for item in inventory:
                if inventory[item][0] == 3:
                    print "%s - level %s" % (inventory[item][1], inventory[item][3])
                else:
                    print "%s - %sx" % (inventory[item][2], inventory[item][1])
    elif command.lower() == "status":
        print "Level: %s" % (player["lvl"])
        print "HP: %s" % (player["HP"])
        print "MP: %s" % (player["MP"])
        print "XP: %s" % (player["XP"])
        print "Improvement points: %s" % (player["points"])
    elif command.lower() == "attributes" or command.lower() == "att":
        print "Health: %s" % (clss["HEA"])
        print "Strength: %s" % (clss["STR"])
        print "Agility: %s" % (clss["AGI"])
        print "Intelligence: %s" % (clss["INT"])
        print "Dexterity: %s" % (clss["DEX"])
        print "Charisma: %s" % (clss["CHA"])
    elif command.lower() == "improve att":
        if player["points"] == 0:
            print "You don't have improvement points."
        else:
            lvl_UP
    else:
        return choice

    # Dices

def check_menu(command, out_put):
    if command != "help" and command != "?" and command != "status" and command != "att" and command != "attributes" and command != "inventory" and command!= "inv" and command != "improve att":
        if type(out_put) is str:
            print out_put
        else:
            out_put

# HAVE TO BE FIXED!
def get_item(cpu, choice):
    command = choice.split(' ')
    if command[0] == "get":
        if command[1] == "items":
            inventory.update(cpu["items"])
            cpu["items"] = {}
            print "You got all items."
        elif command[0] == "get" and command[1] != "items":
            while len(cpu["items"]) > 0:
                if command[1] in cpu["items"]:
                    inventory.update({command[1].lower() : cpu["items"][command[1].lower()]})
                    cpu["items"].pop(choice.split(' ')[1])
                    print "%s's items:" % (cpu["name"])
                    for item in cpu["items"]:
                        if cpu["items"][item][0] == 3:
                            print "%s - level %s" % (cpu["items"][item][2], cpu["items"][item][3])
                        else:
                            print "%s - %sx" % (cpu["items"][item][2], cpu["items"][item][1])
                else: 
                    print "unable to find '%s'" % (command[1])
                    choice = raw_input("Try again, or type 'stop searching' to move on: ")
                    command = choice.split(' ')
                    if command[0] == "stop":
                        break
    else:
        return choice

def search(cpu):
    command = raw_input()
    check_command(command, lvl_up())
    choice = command.split(' ')

    if choice[0].lower() == "search": 
        while len(cpu["items"]) > 0:
            if choice[1].lower() == cpu["name"].lower():
                print "Items found:"
                for item in cpu["items"]:
                    if cpu["items"][item][0] == 3:
                        print "%s - level %s" % (cpu["items"][item][2], cpu["items"][item][3])
                    else:
                        print "%s - %sx" % (cpu["items"][item][2], cpu["items"][item][1])
                if player["kills"] == 1:
                    print "To get a specific item just type 'get item'."
                    print "You can also type 'get items' to put all of them in your inventory."
                    choice = raw_input()
                    get_item(cpu, choice)
                    check_command(choice, lvl_up())
                else:
                    command = raw_input()
                    get_item(cpu, command)
                    check_command(command, lvl_up())
        else:
            print ("Its inventory is empty.")
            if player["kills"] == 1:
                print "All this commands are available for you any time."
                print "You can drop an item on the same way you got it if you want or have to."
    else:
        return choice

def use_item(command):
    first = command.split()[0].lower()
    second = command.split()[1].lower()
    if first == "eat" or first == "drink" or first == "use":
        if second in inventory:
            if inventory[second][0] == 0 and inventory[second][1] > 0:
                player["HP"] += 10
                if player["HP"] > clss["HEA"] * 10:
                    player["HP"] = clss["HEA"] * 10
                inventory[second][1] -= 1
                print "HP = %s" % (player["HP"])
            elif inventory[second][0] == 1 and inventory[second][1] > 0:
                player["HP"] += 20 * inventory[second][3]
                if player["HP"] > clss["HEA"] * 10:
                    player["HP"] = clss["HEA"] * 10
                inventory[second][1] -= 1
                print "HP = %s" % (player["HP"])
            else:
              if first == "use" and inventory[second][3]:
                print "You are using this item already."
              else:
                if second[0] == "a" or second[0] == "e" or second[0] == "i" or second[0] == "ao" or second[0] == "u":
                    print "You can't %s an %s" % (first, second)
                else:
                    print "You can't %s a %s" % (first, second)
    else:
        return command

# Row dices
def row_dice(n):
    dice = randint(1,n)
    return dice

# PVP
# Being attacked by a CPU
def attacked(cpu, lvl, d):
    dice = row_dice(d + clss["AGI"] / 10)
    att = lvl * dice * 5
    print "The %s attacked you!" % cpu["name"]
    if 1 <= dice < 4:
        player["HP"] -= att
        print "Weak hit!"
        print "Your HP: %s" % (player["HP"])
    elif 4 <= dice < 7:
        player["HP"] -= att
        print "Strong hit."
        print "Your HP: %s" % (player["HP"])
    elif 7 <= dice < 9:
        player["HP"] -= att
        print "Critical hit."
        print "Your HP: %s" % (player["HP"])
    else:
        print "You dodged it!"
        print "Your HP: %s" % (player["HP"])
    if player["HP"] <= 0:
        print "You died."

# Attacking a cpu
def attack(cpu, d):
    dice = row_dice(d)
    att = player["lvl"] * dice * 5 + clss["STR"] / 10
    if dice == 1:
        print "You missed."
    elif 1 < dice < 4:
        cpu["HP"] -= att
        print "Weak hit"
        print "%s's HP: %s" % (cpu["name"], cpu["HP"])
    elif 4 <= dice < 7:
        cpu["HP"] -= att
        print "Strong hit."
        print "%s's HP: %s" % (cpu["name"], cpu["HP"])
    else:
        cpu["HP"] -= att
        print "Critical hit!"
        print "%s's HP: %s" % (cpu["name"], cpu["HP"])

# Level UP
def lvl_up():
    if player["XP"] >= 100 * player["lvl"]:
        player["HP"] = clss["HEA"] * 10
        player["XP"] -= 100 * player["lvl"]
        player["lvl"] += 1
        player["points"] += 3
        print "LEVEL UP!"
        if player["lvl"] == 2:
            print "Congratulations! now you have three points to improve your attributes, choose it wiselly."
            print "Type 'att' to check your attributes."
            print "To improve an attribute type its name or its three first letters."
        else:
            print "You have 3 more improvement points."
    while player["points"] > 0:
        choice = raw_input()
        check_command(choice, None)
        if choice.lower()[0] + choice.lower()[1] + choice.lower()[2] == "hea":
            player["points"] -= 1
            clss["HEA"] += 1
            player["HP"] += 10
            print "%s's health is now: %s" % (player["name"], clss["HEA"])
            print "You have %s more improvement points." % ([player["points"]])
        elif choice.lower()[0] + choice.lower()[1] + choice.lower()[2] == "str":
            player["points"] -= 1
            clss["STR"] += 1
            print "%s's strength is now: %s" % (player["name"], clss["STR"])
            print "You have %s more improvement points." % ([player["points"]])
        elif choice.lower()[0] + choice.lower()[1] + choice.lower()[2] == "agi":
            player["points"] -= 1
            clss["AGI"] += 1
            print "%s's agility is now: %s" % (player["name"], clss["AGI"])
            print "You have %s more improvement points." % ([player["points"]])
        elif choice.lower()[0] + choice.lower()[1] + choice.lower()[2] == "dex":
            player["points"] -= 1
            clss["DEX"] += 1
            print "%s's dexterity is now: %s" % (player["name"], clss["DEX"])
            print "You have %s more improvement points." % ([player["points"]])
        elif choice.lower()[0] + choice.lower()[1] + choice.lower()[2] == "int":
            player["points"] -= 1
            clss["INT"] += 1
            print "%s's intelligence is now: %s" % (player["name"], clss["INT"])
            print "You have %s more improvement points." % ([player["points"]])
        elif choice.lower()[0] + choice.lower()[1] + choice.lower()[2] == "cha":
            player["points"] -= 1
            clss["CHA"] += 1
            print "%s's charisma is now: %s" % (player["name"], clss["CHA"])
            print "You have %s more improvement points." % ([player["points"]])
        else:
            message = "To improve an attribute first type 'improve att', then you can type its name or its first three letters. Type 'help' if you need it."
            check_menu(choice.lower(), message)

# Getting in a fight
def fight(cpu, lvl, dice):
    while cpu["HP"] > 0 and player["HP"] > 0:
        choice = raw_input()
        check_command(choice, lvl_up())
        if choice == "attack %s" % (cpu["name"].lower()) or choice == "attack":
            attack(cpu, dice)
            if cpu["HP"] > 0:
                attacked(cpu, lvl, dice)
                if player["HP"] <= 0:
                    print "You died."
                    break
            else:
                print "You killed the %s!" % (cpu["name"])
                player["XP"] += cpu["XP"]
                player["kills"] += 1
                player["last_kill"] = cpu
                lvl_up()
                if player["kills"] == 1:
                    if player["points"] == 0:
                        print "Type 'search %s' to check if it have something useful" % (player["last_kill"]["name"].lower())
                search(cpu)
                check_command(choice, lvl_up())
                break
        elif choice == "run":
            dice = row_dice(20)
            if dice <= 10:
                player["HP"] -= lvl * 45
                print "You tried to run, but the %s was faster." % (cpu["name"])
                print "Critical hit!"
                print "Your HP: %s" % (player["HP"])
                if player["HP"] <= 0:
                    print "you died."
                    break
            elif 10 < dice < 20:
                player["HP"] -= lvl * 33
                print "You tried to run, but the %s was faster." % (cpu["name"])
                print "Strong hit!"
                print "Your HP: %s" % (player["HP"])
                if player["HP"] <= 0:
                    print "You died."
                    break
            else:
                print "You scaped from the %s." % (cpu["name"])
                player["XP"] += cpu["XP"] / 2
                lvl_up()
                break
        else:
            check_menu(choice, attacked(cpu, lvl, dice))
            if player["HP"] <= 0:
                print "You died."
                break

# Itens

# Enemies
goblin = { "name" : "Goblin", "HP" : 50, "XP" : 50, "lvl" : 1, "items" : {"gold" : [2, 1, "Gold", 0], "armor" : [3, 1, "Armor", 1]} }
troll = {"name" : "Troll", "HP" : 100, "XP" : 100, "lvl" : 1, "items" : {"gold" : [2, 1, "Gold", 0], "knif" : [3, 1, "Knif", 1]} }

# Allies
dwarf = { "name" : "Dwarf", "HP" : 200, "XP" : 200, "lvl" : 5, "items" : {"potion" : [1, 2, "Health Potion", 3], "gold" : [2, 5, "Gold", 0], "armor" : [3, 1, "Armor", 5], "sword" : [3, 1, "Sword", 5] } }
hobbit = { "name" : "Hobbit", "HP" : 150, "XP" : 150, "lvl" : 2, "items" : {"potion" : [1, 5, "Health Potion", 5], "gold" : [2, 10, "Gold", 0], "ring" : [3, 1, "Ring", 10] } }


# The journey starts...
print "You are in a jungle, the only thing you can see is the nature. Tall trees of countless and unknown species are covering the sky, you can hear the birds singing and the sound of water coming from south."
print "what do you do?"

choice = ""
while choice != "go north" and choice != "go south" and choice != "go west" and choice != "go east":
    choice = raw_input()
    check_command(choice, lvl_up())
    if choice.lower() == "go north":
        print "You see a goblin approaching!"
        print "What do you do?"
        fight(goblin, 1, 9)
        break
    elif choice.lower() == "go south":
        print "You see a troll approaching!"
        print "What do you do?"
        fight(troll, 1, 9)
        break
    elif choice.lower() == "go east":
        print "You see a dwarf approaching!"
        print "What do you do?"
        break
    elif choice.lower() == "go west":
        print "You see a hobbit approaching!"
        print "What do you do?"
        break
    else:
        print "This command is invalid right now, try to explore the junggle going to a direction or, if you need, type 'help'."

# North Path
if choice.lower() == "go north":
    if player["HP"] <= 50:
        print "You are tired, the goblin was stronger then you thought."

    if clss["INT"] >= 7:
        print "Looking around you found some familiar plants and created a health potion."
        inventory.update({ "potion" : [1, 1, "Health Potion", 1] })
        if clss["INT"] >= 20:               # Defining level of potion
            inventory["potion"][3] = 3
        elif 10 <= clss["INT"] < 20:
            inventory["potion"][3] = 2
        else:
            inventory["potion"][3] = 1
        if clss["DEX"] >= 20:               # Defining how many potions the player can make
            inventory["potion"][1] = 3
        elif 10 <= clss["DEX"] < 20:
            inventory["potion"][1] = 2
        else:
            inventory["potion"][1] = 1
        print "To use an item type 'eat', 'drink', or 'use' and the name of an item you have in you inventory."
        command = raw_input()
        check_command(command, lvl_up())
        use_item(command)

    print "Now, it is becoming dark; you can see the light of a fire coming from North and hear the sound of water coming from South."
    print "What do you do?"
    choice = raw_input()
    check_command(choice, lvl_up())

# South Path
elif choice.lower() == "go south":
    print "South path"

# West Path
elif choice.lower() == "go west":
    print "West path"

# East Path
elif choice.lower() == "go east":
    print "East path"
else:
    message = "invalid..."
    check_menu(choice, message)
