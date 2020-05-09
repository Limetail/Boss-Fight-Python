# Text adventure much like Zork, but much more basic
# I'll be making a dungeon for the player to go through
# Minimum actions with some responses, as well as inventory (works like additonal commands), and combat
# Random is needed, mainly for attack damage
# After 3 enemies, there'll be a miniboss like enemy, maybe give a  magic spell for one additional action to use on miniboss
# Declare victory once boss is defeated

import random
print("Welcome to Drake's dungeon adventure, best of luck!\n")

print("\nAvailable Commands: n, e, s, w, attack, block,")
print("\ninventory, look around, use (item),")
print("\nstats and open (object). To quit the adventure, type quit.\n")

print("\nYou enter the dungeon of a powerful creature.\n")

print("\nYou tread carefully into the room and find yourself in an empty room")
print("\nwith a door on the right and a door in front of you.\n")

inventory = ['Wood Sword', 'Healing Potion', 'Leather Armor', 'Wooden Shield']

RemovedItems = []

Heal = 0
MaxHP = 10
HP = 10
Atk = 1
Def = 1
Shield = 1
# Skeleton1MaxHP = 5
Skeleton1HP = 10
SkeletonAtk = 1

Room1=True
while Room1:
    menu = "Please enter an action: "
    option = input(menu)

    if option == "n":
        print("\nYou head into the North room and is ambushed by a armed skeleton, prepare for combat!\n\n")
        Room1=False
        Combat1=True
        Room1ESR=False

    elif option == "e":
        print("\nIt's a storage room with a single half-full health potion.")
        print("\nYou pocket it.\n\n")
        inventory.append('Half Health Potion')
        Heal = Heal + 1
        Room1=False
        Room1ESR=True

    elif option == "s":
        print("\nThat's the entrance, you're not leaving until the evil is slain.\n\n")

    elif option == "w":
        print("\nThat's a wall...\n\n")

    elif option == "quit":
        print("Game Over\n\n")
        Room1=False
        Room1ESR=False
        Combat1=False
    
    elif option == "look around":
        print("You're in a empty room with a door to the north and a door to the east.\n\n")

    elif option == "inventory":
        print(inventory)
    
    elif option == "stats":
        print(f"\nMax HP: {MaxHP}\n    HP: {HP}\n   Atk: {Atk}\n   Def: {Def}\nShield Bonus: {Shield}\n\n")

    elif option == "heal":
        print("That'd be a waste to use it right now.\n\n")

    elif option == "attack":
        print("There's nothing in here to attack.\n\n")

    elif option == "block":
        print("What are you scared of?\n\n")

    else:
        print("Invalid Command!\n\n")

while Room1ESR:
    menu = "Please enter an action: "
    option = input(menu)

    if option == "n":
        print("\nYou head into the North room and is ambushed by a armed skeleton, prepare for combat!\n\n")
        Room1ESR=False
        Combat1=True

    elif option == "e":
        print("\nIt's an empty storage room.\n\n")

    elif option == "s":
        print("\nThat's the entrance, you're not leaving until the evil is slain.\n\n")

    elif option == "w":
        print("\nThat's a wall...\n\n")

    elif option == "quit":
        print("Game Over\n\n")
        Room1ESR=False
        Combat1=False
    
    elif option == "look around":
        print("You're in a empty room with a door to the north and an empty storage room to the east.\n\n")

    elif option == "inventory":
        print(inventory)
    
    elif option == "stats":
        print(f"\nMax HP: {MaxHP}\n    HP: {HP}\n   Atk: {Atk}\n   Def: {Def}\nShield Bonus: {Shield}\n\n")

    elif option == "heal":
        print("That'd be a waste to use it right now.\n\n")

    elif option == "attack":
        print("There's nothing in here to attack.\n\n")

    elif option == "block":
        print("What are you scared of?\n\n")

    else:
        print("Invalid Command!\n\n")

while Combat1:
    menu = "Please enter an action: "
    option = input(menu)

    if option == "n":
        print("\nYou can't move in combat!\n\n")

    elif option == "e":
        print("\nYou can't move in combat!\n\n")

    elif option == "s":
        print("\nYou can't move in combat!\n\n")

    elif option == "w":
        print("\nYou can't move in combat!\n\n")

    elif option == "quit":
        print("Game Over")
        Combat1=False

    elif option == "heal":
        if Heal > 0:
            HP = HP + 5
            print ("You drink the health potion")
            
        if Heal == 0:
            print ("You are lacking health potions")
        
        if MaxHP < HP:
            Hp = MaxHP
   
    
    elif option == "attack":
        Skeleton1HP = Skeleton1HP - (random.randrange(1,5))
        print(f"\nYou hurt the skeleton for {str((random.randrange(1,5)))} of damage!")
        HP = HP - random.randrange(1,5)
        print(f"\nThe skeleton hit you for {str((random.randrange(1,5)))} of damage!\n\n")
        
        
        if Skeleton1HP <= 0:
            print("The skeleton was defeated!\n\n")
            Combat1=False
        
        elif HP <= 0:
            print("You died, Game Over.\n\n")
            Combat1=False
        
    elif option == "stats":
        print(f"\nMax HP: {MaxHP}\n    HP: {HP}\n   Atk: {Atk}\n   Def: {Def}\nShield Bonus: {Shield}\n\n")