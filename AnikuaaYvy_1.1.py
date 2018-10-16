from random import randint

# Player
player = {"HP" : 10, "MP" : 100, "lvl" : 1, "XP" : 0, "points" : 0, "kills" : 0, "last_kill" : ""}
inventory = {}

# Classes
knight = {"name" : "knight", "HEA" : 15, "STR" : 20, "AGI" : 10, "DEX" : 10, "INT" : 5, "CHA" : 5}
mage = {"name" : "mage", "HEA" : 10, "STR" : 5, "AGI" : 10, "DEX" : 15, "INT" : 20, "CHA" : 5}
archer = {"name" : "archer", "HEA" : 10, "STR" : 5, "AGI" : 15, "DEX" : 20, "INT" : 10, "CHA" : 5}
thief = {"name" : "thief", "HEA" : 10, "STR" : 5, "AGI" : 10, "DEX" : 15, "INT" : 5, "CHA" : 20}
monk = {"name" : "monk", "HEA" : 10, "STR" : 15, "AGI" : 20, "DEX" : 10, "INT" : 5, "CHA" : 5}
classes = [knight, mage, archer, thief, monk]

# Player Info
print ("Choose a name for your character:")
name = input()
player["name"] = name

print ("Greedings %s, choose a class to start your advanture!" % (name))
print ("If you need, type 'classes' to check your options and its attributes.")
clss = "none"

# Choosing a class
while True:
    clss = input()
    for c in classes:
        if clss.lower() == c["name"]:
            clss = c
            player["HP"] *= clss["HEA"]
            break
    if type(clss) is dict:
        if clss["name"].lower() == "knight" or clss["name"].lower() == "archer" or clss["name"].lower() == "mage" or clss["name"].lower() == "thief" or clss["name"].lower() == "monk":
            print("Welcom to Anikuaa Yvy, %s the %s." % (name, c["name"].capitalize()))
            break
    else:
        if clss.lower() == "classes":
            print ("You have five options:")
            for c in classes:
                print (c["name"].capitalize())
                print ("  - Health: %s" % (c["HEA"]))
                print ("  - Strength: %s" % (c["STR"]))
                print ("  - Agility: %s" % (c["AGI"]))
                print ("  - Intelligence: %s" % (c["INT"]))
                print ("  - Dexterity: %s" % (c["DEX"]))
                print ("  - Charisma: %s" % (c["CHA"]))
        else:
            print("Invalid...")
            print("Choose another class or type 'classes' to see your options and its atributes.")

# Gameplay functions
# Dice
def rowDice(n):
    dice = randint(1,n)
    return dice

#PVP
def attacked(cpu, lvl):
    dice = rowDice(20 + int(round(player["AGI"] / 10)))
    att = lvl * dice
    print("The %s attacked you!") % cpu["name"]
    if 1 <= dice <= 5:
        player["HP"] -= att
        print("Weak hit!")
        print("Your HP: %s" % (player["HP"]))