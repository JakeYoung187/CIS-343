#import inspect
import random
import re
import sys
import os
#from abc import ABCMeta, abstractmethod
from observable import Observable
from observer import Observer

##############################################################
#The observer class is used to update observers when a change
#of state takes place.
#############################################################
#class Observable(object):
 
#        def __init__(self):    
#                self.observers = []
 
#        def add_observer(self, observer):
#                if not observer in self.observers:
#                        self.observers.append(observer)
 
#        def remove_observe(self, observer):
#                if observer in self.observers:
#                        self.observers.remove(observer)
 
#        def remove_all_observers(self):
#                self.observers = []
 
#        def update(self):
#                for observer in self.observers:
#                        observer.update()


#############################################################
#The observer class is used to create observers
#############################################################
#class Observer(object):
#	__metaclass__ = ABCMeta
#
#	@abstractmethod
#	def update(self):
#		pass


#############################################################
#Weapon class creates instances of weapons used by the Player
#@var name - the name of the weapon
#@var attack_mod - the attack modifier of the weapon
#@var num_uses - number of times a weapon can be used
#############################################################
class Weapon:
	name = ''
	attack_mod = 0
	num_uses = -1
	def __init__(self, name, atk, use):
		self.name = name
		self.attack_mod = atk
		self.num_uses = use
	##
	#Getters and setters
	##
	def get_weapon_name(self):
		return self.name
	def set_weapon_name(self, name):
		self.name = name
	def get_attack_mod(self):
		return self.attack_mod
	def set_attack_mod(self, atk):
		self.attack_mod = atk
	def get_num_uses(self):
		return self.num_uses
	def set_num_uses(self, uses):
		self.num_uses = uses


#############################################################
#Player class creates an instance of a player for the user to
#play as in the RPG.
#@var health - the health of the player
#@var equipped_weapon - the current equipped weapon
#@var items - list of weapons held by player
#@var current_location - current player location
#############################################################
class Player:
	health = 0
	equipped_weapon = ''
	attack_value = 0
	items = []
	current_location = 0
	def __init__(self):
		self.health = random.randint(100, 125)
		self.attack_value = random.randint(5, 20)
		self.current_location = [0, 0]
		HersheyKiss = Weapon('HersheyKiss', 1, -1)
		self.items.append(HersheyKiss)
		SourStraws = Weapon('SourStraws', random.randint(1, 2), 2)
		self.items.append(SourStraws)
		ChocolateBars = Weapon('ChocolateBars', random.randint(2, 3), 4)
		self.items.append(ChocolateBars)
		NerdBombs = Weapon('NerdBombs', random.randint(3, 5), 1)
		self.items.append(NerdBombs)
		self.equipped_weapon = NerdBombs
	##
	#The move method is used to change the players current
	#location, as well as make sure the player stays in the
	#bounds of the grid
	#@param direction - the direction of the move
	##
	def move(self, direction):
		#game movement
		if(direction == 'n'):
			if(self.current_location[1] != 5):
				self.current_location[1] += 1
			else:
				print '********************************'
				print 'You cannot go in that direction'
				print '********************************'
		if(direction == 's'):
			if(self.current_location[1] != 0):
				self.current_location[1] -= 1
			else:
				print '********************************'
                                print 'You cannot go in that direction'
                                print '********************************'
		if(direction == 'e'):
			if(self.current_location[0] != 5):
				self.current_location[0] += 1
			else:
				print '********************************'
                                print 'You cannot go in that direction'
                                print '********************************'
		if(direction == 'w'):
			if(self.current_location[0] != 0):
				self.current_location[0] -= 1
			else:
				print '********************************'
                                print 'You cannot go in that direction'
                                print '********************************'
	##
	#equip_weapon changes the current weapon the player is using
	#(used for the 'c' command)
	#@param weapon - the new equipped weapon
	##
	def equip_weapon(self, weapon):
		for a in range(len(self.items)):
			if(self.items[a].get_weapon_name() == weapon):
				self.equipped_weapon = self.items[a]
	
	##
	#show_inventory prints a list of the players remaining weapons
	##
	def show_inventory(self):
		print 'Weapons:'
		for x in range(len(self.items)):
			print '  '
			print self.items[x].get_weapon_name()
			print 'Attack: ', self.items[x].get_attack_mod()
			if(self.items[x].get_num_uses() < 0):
				print 'Number of uses: Infinite'
			else:
				print 'Number of uses: ', self.items[x].get_num_uses()	

		print '\n\n'

	##
	#drop_weapon drops the desired weapon from the items list,
	#as well as make sure the HersheyKiss cannot be dropped
	#@param weapon - the weapon to be dropped
	##	
	def drop_weapon(self, weapon):
		if(weapon == self.items[0]):
			print 'Cannot drop this weapon.'
			return
		if(self.equipped_weapon == weapon):
			self.equipped_weapon = self.items[0]
		self.items.remove(weapon)
	##
	#attack allows the player to attack all of the monsters
	#in the house, and updates the list of monsters in the
	#house
	#@param monsters - list of monsters to be attacked
	##
	def attack(self, monsters):
		power = self.attack_value + self.equipped_weapon.get_attack_mod()
		for i in range(len(monsters)):
			while(monsters[i].get_health() > 0):
				health = monsters[i].get_health()
				monsters[i].set_health(health - power)
			if(monsters[i].get_species() != 'Person' and monsters[i].get_species() != 'HealedPerson'):
				num = self.equipped_weapon.get_num_uses() 
				self.equipped_weapon.set_num_uses(num - 1)
				if(self.equipped_weapon.get_num_uses() == 0):
					self.drop_weapon(self.equipped_weapon)
			monsters[i].change(monsters[i])
		monsters[0].update(monsters)
	
	##
	#Getters and setters
	##
	def get_health(self):
		return self.health
	def set_health(self, health):
		self.health = health
	def get_equipped_weapon(self):
		return self.equipped_weapon
	def get_attack_value(self):
		return self.attack_value
	def set_attack_value(self, atk):
		self.attack_value = atk
	def get_current_location(self):
		return self.current_location
	def set_current_location(self, loc):
		self.current_location = loc
			

###########################################################################
#Monster class creates the monsters to be added into the houses
#@var health - the health of the monster
#@var species - the type of monster (zombie, person, etc.)
#@var attack_value - the amount of damage the can do to the player
###########################################################################
class Monster(Observer):
	health = 0
	species = ''
	attack_value = 0
	def __init__(self, species):
		self.species = species
		if(species == 'Zombie'):
			self.health = random.randint(50, 100)
			self.attack_value = random.randint(0, 10)
		if(species == 'Person'):
			self.health = 100
			self.attack_value = -2
		if(species == 'Vampire'):
			self.health = random.randint(50, 100)
			self.attack_value = random.randint(0, 15)
		if(species == 'Ghoul'):
			self.health = random.randint(40, 80)
			self.attack_value = random.randint(5, 20)
		if(species == 'Werewolf'):
			self.health = 200
			self.attack_value = random.randint(0, 40)
	##
	#attack allows the monsters to attack the player
	#@param player - instance of the player to be attacked
	#@param atkvalue - the amount of damage the monster can do
	##
	def attack(self, player, atkvalue):
		health = player.get_health()
		player.set_health(health - atkvalue)
	
	##
	#change creates the healed people after a monster is destroyed
	#@param monster - the monster that has been destroyed
	##
	def change(self, monster):
		monster.species = 'HealedPerson'
		monster.health = 100
		monster.attack_value = -2
	##
	#methods for Observer pattern
	##
	def update(self, monsters):
		pass
	def add_observer(self, observer):
		pass
	
	##
	#Getters and setters
	##
	def get_health(self):
		return self.health
	def set_health(self, health):
		self.health = health
	def get_attack_value(self):
		return self.attack_value
	def set_attack_value(self, atk):
		self.attack_value = atk
	def get_species(self):
		return self.species
	def set_species(self, species):
		self.species = species

#########################################################################
#House class creates an instance of a house on the grid
#@var population - the monsters 'living' in the house
#@var species - a list of monster species for random selection
########################################################################
class House(Observable):
	population = 'empty'
	species = ['Zombie', 'Vampire', 'Ghoul', 'Werewolf', 'Person']
	def __init__(self):
		self.population = []
		for x in range(random.randint(1, 5)):
			enemy = Monster(self.species[random.randint(0,4)])
			self.population.append(enemy)
			enemy.add_observer(self)

	##
	#show_monsters displays the monsters currently in the house
	#@param house - the house to be searched
	##
	def show_monsters(self, house):
		r = len(house.population)
		print '******************************'
		print 'Monsters currently in the house:'
		for i in range(r):
			print house.population[i].get_species()
		print '******************************'
	
	##
	#method for observer pattern
	##
	def update(self, monsters):
		self.population = monsters

	def add_observer(self, observer):
		pass
	
	##
	#Getter and setter
	##
	def get_population(self):
		return self.population
	def get_monster(self, x):
		return self.population[x]
	def set_monster(self, x, monster):
		self.population[x] = monster


########################################################################
#Game class creates the game loop
#@var hero - the users character
#@var hood - the 'neighborhood' or grid of houses
#@var end_of_game - variable to show games progress
########################################################################
class Game():
	hero = Player()
        hood = [[0 for i in range(6)] for j in range(6)]
	end_of_game = 'false'
	def __init__(self):
		#placing houses (9)
		self.hood[0][5] = House()
		self.hood[0][5].add_observer(self.hood)
		self.hood[1][0] = House()
		self.hood[1][0].add_observer(self.hood)
		self.hood[1][5] = House()
		self.hood[1][5].add_observer(self.hood)
		self.hood[2][5] = House()
		self.hood[2][5].add_observer(self.hood)
		self.hood[2][0] = House()
		self.hood[2][0].add_observer(self.hood)
		self.hood[3][0] = House()
		self.hood[3][0].add_observer(self.hood)
		self.hood[4][0] = House()
		self.hood[4][0].add_observer(self.hood)
		self.hood[4][1] = House()
		self.hood[4][1].add_observer(self.hood)
		self.hood[4][4] = House()
		self.hood[4][4].add_observer(self.hood)
		self.hood[4][5] = House()
		self.hood[4][5].add_observer(self.hood)

	##
	#play creates the loop to accept commands from the user
	##
	def play(self):
		print '\nThere are walls all around you, but an open door in front of you. Where would you like to go?\n'
		while(self.end_of_game is 'false'):
			print '\n**Type help for a list of commands**'
			print 'Health:', self.hero.get_health()
			print 'Equipped Candy:', self.hero.get_equipped_weapon().get_weapon_name()
			command = raw_input()
			#not sure if this is bad practice
			x = self.hero.get_current_location()[0]
			y = self.hero.get_current_location()[1]
			print '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
			self.process_command(command, self.hood[x][y])
			if(command == 'fight'):
				if(isinstance(self.hood[x][y], House)):
					if(self.hero.get_health() > 0):
						print 'You have successfully defeated the monsters inside of the house!'
			self.print_surroundings(self.hero.get_current_location())
			self.game_over()
		if(self.end_of_game is 'loss'):
			print 'The monsters inside the house have defeated you!\n'
		if(self.end_of_game is 'win'):
			print 'YOU WON!\n'
			print 'You have saved the neighborhood from the candy plague that had taken them over'

	##
	#check_house loops through house population to see if any monsters
	#are still unturned (used for end of game checks)
	#@param house - the house to be searched
	##
	def check_house(self, house):
		for x in range(len(house.get_population())):
			if(house.get_monster(x).get_species() is not 'HealedPerson'):
				return 0
		return 1
	
	##
	#fight loops attacks from both the player and the monster until
	#the monsters are defeated or the players health reaches 0
	#@param player - the users character
	#@param house - the house that the player is currently in
	##
	def fight(self, player, house):
		temp = 0
		for x in range(len(house.get_population())):
			temp += house.get_monster(x).get_attack_value()
		player.attack(house.get_population())
		house.get_monster(x).attack(player, temp)
		
	##
	#processes the command that the user enters
	#@param cmd - the command entered
	#@param house - the house the player is in (used if the player is attacking)
	##
	def process_command(self, cmd, house):
		if(cmd == 'i'):
			self.hero.show_inventory()
		if(cmd == 'help'):
			print '\nMovement commands: n(North), s(South), e(East), w(West)'
			print '\nOther commands: quit, fight, heal (when in a healed house), i (to display inventory), and c (change equipped weapon)\n\n'
			print 'Attack monsters to turn them back into people, once you clear a house completely of monsters, you will be able to heal yourself using the \'heal\' command when inside of the house.'
		if(cmd == 'quit'):
			exit(0)
		if(cmd == 'n' or cmd == 's' or cmd == 'e' or cmd == 'w'):
			self.hero.move(cmd)
		if(cmd == 'heal'):
			if(isinstance(house, House)):
				self.fight(self.hero, house)
			else:
				return
		if(cmd == 'fight'):
			if(isinstance(house, House)):
				self.fight(self.hero, house)
			else:
				return
		split_cmd = re.split('\s+', cmd)
		if(split_cmd[0] == 'c'):
			self.hero.equip_weapon(split_cmd[1])

	##
	#displays the message to inform the player of their current location
	#@param location - the players current location
	##
	def print_surroundings(self, location):
		if(location == [0, 0]):
			print 'You are in a garage, there is a road North and a House East'
		if(location == [0, 1]):
			print 'You are on the corner of a road that continues North or East, the garage is South'
		if(location == [0, 2] or location == [0, 3]):
			print 'You are on a road that continues heading North or South. There is a park to the East.'
		if(location == [0, 4]):
			print 'You are at the corner of a road that coninues South or East, there is a house directly North.'
		if(location == [0, 5]):
			if(self.hood[0][5].get_monster(0).get_species() == 'HealedPerson'):
				print 'You enter a house filled with people!'
			else:
				print 'You enter a house that is filled with', len(self.hood[0][5].get_population()), 'monsters, will you attack or run?'
			self.hood[0][5].show_monsters(self.hood[0][5])
		if(location == [1, 0]):
			if(self.hood[1][0].get_monster(0).get_species() == 'HealedPerson'):
                                print 'You enter a house filled with people!'
                        else:
                                print 'You enter a house that is filled with ', len(self.hood[1][0].get_population()), ' monsters, will you attack or run?'
			self.hood[1][0].show_monsters(self.hood[1][0])
		if(location == [1, 1]):
			print 'You are on a road that continues West or East, there is also a park directly North, and a house directly South.'
		if(location == [1, 2]):
			print 'You are in a park, the park continues North and East, there is a road South and West'
		if(location == [1, 3]):
			print 'You are in a park, the park continues South and East, there is a road North and West'
		if(location == [1, 4]):
			print 'You are in a road that continues East and West, there is a house North, and a park South'
		if(location == [1, 5]):
			if(self.hood[1][5].get_monster(0).get_species() == 'HealedPerson'):
                                print 'You enter a house filled with people!'
                        else:
                                print 'You enter a house that is filled with', len(self.hood[1][5].get_population()), 'monsters, will you attack or run?'
			self.hood[1][5].show_monsters(self.hood[1][5])
		if(location == [2, 0]):
			if(self.hood[2][0].get_monster(0).get_species() == 'HealedPerson'):
                                print 'You enter a house filled with people!'
                        else:
                                print 'You enter a house that is filled with', len(self.hood[2][0].get_population()), 'monsters, will you attack or run?'
			self.hood[2][0].show_monsters(self.hood[2][0])
		if(location == [2, 1]):
			print 'You are on a road that continues West or East, there is also a park directly North, and a house South'
		if(location == [2, 2]):
			print 'You are in a park that continues North and West, there is also a road East or South'
		if(location == [2, 3]):
			print 'You are in a park that continues South and West, there is also a road East North'
		if(location == [2, 4]):
			print 'You are on a road that continues East and West, there is a house North, or a park South'
		if(location == [2, 5]):
			if(self.hood[2][5].get_monster(0).get_species() == 'HealedPerson'):
                                print 'You enter a house filled with people!'
                        else:
                                print 'You enter a house that is filled with', len(self.hood[2][5].get_population()), 'monsters, will you attack or run?'
			self.hood[2][5].show_monsters(self.hood[2][5])
		if(location == [3, 0]):
			if(self.hood[3][0].get_monster(0).get_species() == 'HealedPerson'):
                                print 'You enter a house filled with people!'
                        else:
                                print 'You enter a house that is filled with', len(self.hood[3][0].get_population()), 'monsters, will you attack or run?'
			self.hood[3][0].show_monsters(self.hood[3][0])
		if(location == [3, 1]):
			print 'You are on a road that continues North and West. There are also houses directly South and East.'
		if(location == [3, 2]):
			print 'You are on a road that continues North and South, there is a park West, and a graveyard East.'
		if(location == [3, 3]):
			print 'You are on a road that continues North and South, there is a park West, and a graveyard East.' 	
		if(location == [3, 4]):
			print 'You are on a road that continues North, West, and South. There is also a House directly East.'
		if(location == [3, 5]):
			print 'You are on a road that continues South, there are houses East and West.'
		if(location == [4, 0]):
			if(self.hood[4][0].get_monster(0).get_species() == 'HealedPerson'):
                                print 'You enter a house filled with people!'
                        else:
                                print 'You enter a house that is filled with', len(self.hood[4][0].get_population()), 'monsters, will you attack or run?'
			self.hood[4][0].show_monsters(self.hood[4][0])
		if(location == [4, 1]):
			if(self.hood[4][1].get_monster(0).get_species() == 'HealedPerson'):
                                print 'You enter a house filled with people!'
                        else:
                                print 'You enter a house that is filled with', len(self.hood[4][1].get_population()), 'monsters, will you attack or run?'
			self.hood[4][1].show_monsters(self.hood[4][1])
		if(location == [4, 2]):
			print 'You are in a cemetary that continues North and East, there is a house South, and a road West.'
		if(location == [4, 3]):
			print 'You are in a cemetary that continues South and East, there is a house North, and a road west.'
		if(location == [4, 4]):
			if(self.hood[4][4].get_monster(0).get_species() == 'HealedPerson'):
                                print 'You enter a house filled with people!'
                        else:
                                print 'You enter a house that is filled with', len(self.hood[4][4].get_population()), 'monsters, will you attack or run?'
			self.hood[4][4].show_monsters(self.hood[4][4])
		if(location == [4, 5]):
			if(self.hood[4][5].get_monster(0).get_species() == 'HealedPerson'):
                                print 'You enter a house filled with people!'
                        else:
                                print 'You enter a house that is filled with', len(self.hood[4][5].get_population()), 'monsters, will you attack or run?'
			self.hood[4][5].show_monsters(self.hood[4][5])
		if(location == [5, 0]):
			print 'You are in a backyard, there is a house West, and another backyard North.'
		if(location == [5, 1]):
			print 'You are in a backyard, there is a house West, another backyard South, and a cemetary North.'
		if(location == [5, 2]):
			print 'You are in a cemetary that continues North and West, there is a backyard South.'
		if(location == [5, 3]):
			print 'You are in a cemetary that continues South and West, there is a backyard North.'
		if(location == [5, 4]):
			print 'You are in a backyard, there is a house West, another backyard North, and a cemetary South.'
		if(location ==[5, 5]):
			print 'You are in a backyard, there is a house West and another backyard South.'

	##
	#game_over checks the status of the game to see if it should end
	##
	def game_over(self):
		healed_houses = 0
		if(self.hero.get_health() <= 0):
			self.end_of_game = 'loss'
			
		for a in range(6):
			for b in range(6):
				if(isinstance(self.hood[a][b], House)):
					if(self.check_house(self.hood[a][b]) is 1):
						healed_houses += 1
		if(healed_houses == 10):
			self.end_of_game = 'win'
	

	
########################################################################################
#main method used to create an instance of the game and to print the intro messages.
########################################################################################
if __name__=="__main__":
	#create game
	game = Game()

	#intro message and game start
	print '\n\n********************************************************************************'
	print 'Welcome to Short Gritty Coffin\n(Name credit to random word generator)\n\nWould you like to play? (y/n)'
	print '********************************************************************************'
	answer = raw_input()
	if(answer == 'y' or answer == 'Y'):
		print '\nYou wake up out of your candy-induced coma in a detatched garage. All of your friends and family have been turned into a monsters by a bad batch of candy! You must fight to turn them back into the people they once were. There is some candy on the ground, you pick it up and put it into your pocket. (use the candy to attack monsters)\n'
		game.play()
		print 'Would you like to play again? (y/n)'
		answer = raw_input()
		if(answer == 'y' or answer == 'Y'):
			os.execl(sys.executable, sys.executable, *sys.argv)
	else:
		exit(0)
	
