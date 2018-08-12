from sys import exit

##########################################
#Lol this is where you come when you die
def dead(why):
	print(why, "Good job!")
	exit(0)
	
##########################################
#This is the golden room
def golden_door():
	#Brnging health and list through global
	global max_health	
	global current_health
	global items
	global gold
	print("You have entered the golden room through the golden door")
	print("The door through which you have entered has disappeared.")
	if (gold == False):
		dead("A scary ogre appears and eats you alive, maybe if you had a suit of armor and a weapon you would've survived")
	

##########################################
#This is the silver room
def silver_door():
	#Brnging health and list through global
	global max_health	
	global current_health
	global items
	global gold
	global silver
	print("You have entered the silver room through the silver door")
	print("The door through which you have entered has disappeared.")
	if (silver == False):
		dead("A crazed bear appears and and attacks you, maybe if you had a weapon you would've survived")
	
##########################################
#This is the bronze room
def bronze_door():
	#Brnging health and list through global
	global max_health	
	global current_health
	global items
	print("You have entered the bronze room through the bronze door")
	print("The door through which you have entered has disappeared.")
	exit(0)
##########################################
#This is the regular room
def wooden_door():
	#Brnging health and list through global
	global max_health	
	global current_health
	global items
	print("You have entered the regular room through the wooden door")
	print("The door through which you have entered has disappeared.")
	exit(0)
##########################################
#This is where the game begins
def starting_point():
	#Choice between the door
	print("""You are in a dark room and you see four doors in front of you.
	1. A golden door
	2. A silver door
	3. A bronze door
	4. A wooden door
	Which do you choose?
	""")

	#Choose your destiny
	choice = input("> ")

	#Sending player to the chosen room
	if choice == "1" or "golden" in choice or "gold" in choice:
		golden_door()
	elif choice == "2" or "silver" in choice:
		silver_door()
	elif choice == "3" or "bronze" in choice:
		bronze_door()
	elif choice == "4" or "wooden" in choice or "wood" in choice:
		wooden_door()
	else:
		dead("You do something stupid, like trip and fall on a knife and die.")
	
##########################################
# Heals the player at the cost of 1 potion
def use_potion():

	#Brnging health and list through global
	global max_health	
	global current_health
	global items 
	
	#Health < Max & Potion
	if current_health != max_health and "potion" in items:
		current_health = max_health
		items.remove("potion")
		print(f"Health has been restored to {current_health} HP\n")
		
	#Health < Max & No Potion
	elif current_health != max_health and "potion" not in items:
		print("Sorry, you are out of potions!\n")
		
	#Health = Max & No Potion
	elif current_health == max_health and "potion" not in items:
		print("You are at full health, there's no point using a potion. PS: you are out of potions\n")
		
	#Health = Max & Potion
	else:
		print("You are at full health, there's no point using a potion.\n")

##########################################
# Prints the status of the player
def status(health, item):
	global name
	global max_health
	if item == []:
		item = "nothing"
	else:
		item = items
	print(f"{name}, this is your current status")
	print(f"Your health is {health} HP")
	
	if max_health > health:
		print("Oh no, you are not at full health! Consider using a potion if you have one")
	else:
		print("Yayy! You're at full health. Find a magical elixer to increase max health")
		
	print(f"You have {item} with you in your bag pack\n")
	
	
##########################################
max_health = 3
current_health = 3
items = ["potion"]
gold = False
silver = False
key = False

print("""Hello there!!
Welcome to my game!!
Have fun!!\n""")

#Asks and gets the name
print("What's your name?\n")
name = input("> ")

#Comments about name, welcomes {name}
if len(name) < 5:
	print(f"Wow, that's a short name! Welcome {name}\n")
elif len(name) > 9:
	print(f"Wow, that's a long name! Welcome {name}\n")
else:
	print(f"Cool name, Welcome {name}\n")

#prints status once before game begins
status(current_health, items)

starting_point()
