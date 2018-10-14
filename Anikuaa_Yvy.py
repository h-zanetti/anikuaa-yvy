player = {"HP" : 10, "MP" : 100, "lvl" : 1, "XP" : 0, "points" : 0, "kills" : 0, "last_kill" : ""}
inventory = {}
clss = {"HEA" : 15, "STR" : 20, "AGI" : 10, "DEX" : 10, "INT" : 5, "CHA" : 5}

def check_command():
    while True:
        command = raw_input()
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
        else:
            return command
            break

check_command()
print command
