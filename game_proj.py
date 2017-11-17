import inspect
import random
from abc import ABCMeta, abstractmethod

##############################################################
#Code for Observables
#############################################################
class Observable(object):
 
        def __init__(self):    
                self.observers = []
 
        def add_observer(self, observer):
                if not observer in self.observers:
                        self.observers.append(observer)
 
        def remove_observe(self, observer):
                if observer in self.observers:
                        self.observers.remove(observer)
 
        def remove_all_observers(self):
                self.observers = []
 
        def update(self):
                for observer in self.observers:
                        observer.update()
#############################################################
#Code for Observers
#############################################################
class Observer(object):
	__metaclass__ = ABCMeta

	@abstractmethod
	def update(self):
		pass
#############################################################
#Weapon class
#############################################################
class Weapon:
	name = ''
	attack_mod = 0
	num_uses = -1
	def __init__(self, name, atk, use):
		self.name = name
		self.attack_mod = atk
		self.num_uses = use
#############################################################
#Player class
#############################################################
class Player:
	health = 0
	equipped_weapon = ''
	attack_value = 0
	items = []
	current_location = 0
	def __init__(self):
		self.health = random.randint(100, 125)
		self.attack_value = 5
		self.current_location = [0, 0]
		HersheyKiss = Weapon('HersheyKiss', 1, -1)
		self.items.append(HersheyKiss)
		self.equipped_weapon = HersheyKiss
	def move(self, direction):
		#game movement
		if(direction == 'n'):
			if(self.current_location[1] != 5):
				self.current_location[1] += 1
			else:
				print 'Cannot go in that direction'
		if(direction == 's'):
			if(self.current_location[1] != 0):
				self.current_location[1] -= 1
			else:
				print 'Cannot go in that direction'
		if(direction == 'e'):
			if(self.current_location[0] != 5):
				self.current_location[0] += 1
			else:
				print 'Cannot go in that direction'
		if(direction == 'w'):
			if(self.current_location[0] != 0):
				self.current_location[0] -= 1
			else:
				print 'Cannot go in that direction'
	def equip_weapon(self, weapon):
		self.equipped_weapon = weapon
	def add_weapon(self, weapon):
		self.items.append(weapon)	
	def drop_weapon(self, weapon):
		if(weapon == self.items[0]):
			print 'Cannot drop this weapon.'
			return
		if(self.equipped_weapon == weapon):
			self.equipped_weapon = self.items[0]
		self.items.remove(weapon)
	def attack(self, monsters):
		power = self.attack_value + self.equipped_weapon.attack_mod
		for i in range(len(monsters)):
			while(monsters[i].health > 0):
				monsters[i].health -= power
			monsters[i].change(monsters[i])
		monsters[0].update(monsters)
		#for h in range(len(monsters)):
		#	print len(monsters)
		#	print monsters[h].species

###########################################################################
#Monster class
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
	def attack(self, player, atkvalue):
		player.health -= atkvalue
		if(player.health <= 0):
			#gameover
			print
	def change(self, monster):
		monster.species = 'Healed'
		monster.health = 100
		monster.attack_value = -2
	def update(self, monsters):
		pass
	def add_observer(self, observer):
		pass
#########################################################################
#House class
########################################################################
class House(Observable, Observer):
	population = 'empty'
	species = ['Zombie', 'Vampire', 'Ghoul', 'Werewolf', 'Person']
	def __init__(self):
		self.population = []
		for x in range(random.randint(1, 5)):
			enemy = Monster(self.species[random.randint(0,4)])
			self.population.append(enemy)
			enemy.add_observer(self)
		#print len(self.population)
	def show_monsters(self, house):
		r = len(house.population)
		for i in range(r):
			print house.population[i].species
	def update(self, monsters):
		self.population = monsters
		#update the health

	def add_observer(self, observer):
		pass
########################################################################
#Game class
########################################################################
class Game():
	hero = Player()
	#hood = [[Location('Empty') for i in range(6)] for j in range(6)]
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

	def play(self):
		print '\nThere are walls all around you, but an open door in front of you. Where would you like to go?\n'
		while(self.end_of_game == 'false'):
			#print '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
			print '\nCommands: n(North), s(South), e(East), w(West)'
			print 'Health:', self.hero.health
			print 'Equipped Candy:', self.hero.equipped_weapon.name
			#print '\nWhat would you like to do?'
			command = raw_input()
			self.process_command(command)
			x = self.hero.current_location[0]
			y = self.hero.current_location[1]
			self.print_surroundings(self.hero.current_location)
			if(isinstance(self.hood[x][y], House)):
				self.hood[x][y].show_monsters(self.hood[x][y])
				self.fight(self.hero, self.hood[x][y])	
					#self.hood[x][y].show_monsters

	def check_house(self, house):
		if all(x != 'Healed' for x in house.population):
			return 0
		else:
			return 1

	def fight(self, player, house):
		temp = 0
	#while(self.check_house(house) is 0 and player.health > 0):
		for x in range(len(house.population)):
			temp += house.population[x].attack_value
			#print house.population[x].species
			#house.population[x].attack(player)
		player.attack(house.population)
		house.population[x].attack(player, temp)
		#player.attack(house.population[x])

	def process_command(self, cmd):
		if(cmd == 'quit'):
			exit(0)
		if(cmd == 'n' or cmd == 's' or cmd == 'e' or cmd == 'w'):
			self.hero.move(cmd)
		if(cmd == 'attack'):
			print
			#if in a house attack otherwise dont self.hero.attack
	def print_surroundings(self, location):
		print '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
		if(location == [0, 0]):
			print 'You are in a garage, there is a road North and a House East'
		if(location == [0, 1]):
			print 'You are on the corner of a road that continues North or East, the garage is South'
		if(location == [0, 2] or location == [0, 3]):
			print 'You are on a road that continues heading North or South. There is a park to the East.'
		if(location == [0, 4]):
			print 'You are at the corner of a road that coninues South or East, there is a house directly North.'
		if(location == [0, 5]):
			num_people = 0
			for i in range(len(self.hood[0][5].population)):
				if(self.hood[0][5].population[i] == 'Person'):
					num_people += 1

			if(num_people != len(self.hood[0][5].population)):
				print 'You enter a house that is filled with monsters, will you attack or run?' #run just takes you outside
			else:
				print 'You enter a house filled with people!'
		if(location == [1, 0]):
			num_people = 0
                        for i in range(len(self.hood[1][0].population)):
                                if(self.hood[1][0].population[i] == 'Person'):
                                        num_people += 1

                        if(num_people != len(self.hood[1][0].population)):
                                print 'You enter a house that is filled with monsters, will you attack or run?' #run just takes you outside
                        else:
                                print 'You enter a house filled with people!'
		if(location == [1, 1]):
			print 'You are on a road that continues West or East, there is also a park directly North, and a house directly South.'
		if(location == [1, 2]):
			print 'You are in a park, the park continues North and East, there is a road South and West'
		if(location == [1, 3]):
			print 'You are in a park, the park continues South and East, there is a road North and West'
		if(location == [1, 4]):
			print 'You are in a road that continues East and West, there is a house North, and a park South'
		if(location == [1, 5]):
			num_people = 0
                        for i in range(len(self.hood[1][5].population)):
                                if(self.hood[1][5].population[i] == 'Person'):
                                        num_people += 1

                        if(num_people != len(self.hood[1][5].population)):
                                print 'You enter a house that is filled with monsters, will you attack or run?' #run just takes you outside
                        else:
                                print 'You enter a house filled with people!'
		if(location == [2, 0]):
			num_people = 0
                        for i in range(len(self.hood[2][0].population)):
                                if(self.hood[2][0].population[i] == 'Person'):
                                        num_people += 1

                        if(num_people != len(self.hood[2][0].population)):
                                print 'You enter a house that is filled with monsters, will you attack or run?' #run just takes you outside
                        else:
                                print 'You enter a house filled with people!'
		if(location == [2, 1]):
			print 'You are on a road that continues West or East, there is also a park directly North, and a house South'
		if(location == [2, 2]):
			print 'You are in a park that continues North and West, there is also a road East or South'
		if(location == [2, 3]):
			print 'You are in a park that continues South and West, there is also a road East North'
		if(location == [2, 4]):
			print 'You are on a road that continues East and West, there is a house North, or a park South'
		if(location == [2, 5]):
			num_people = 0
                        for i in range(len(self.hood[2][5].population)):
                                if(self.hood[2][5].population[i] == 'Person'):
                                        num_people += 1

                        if(num_people != len(self.hood[2][5].population)):
                                print 'You enter a house that is filled with monsters, will you attack or run?' #run just takes you outside
                        else:
                                print 'You enter a house filled with people!'
		if(location == [3, 0]):
			num_people = 0
                        for i in range(len(self.hood[3][0].population)):
                                if(self.hood[3][0].population[i] == 'Person'):
                                        num_people += 1

                        if(num_people != len(self.hood[3][0].population)):
                                print 'You enter a house that is filled with monsters, will you attack or run?' #run just takes you outside
                        else:
                                print 'You enter a house filled with people!'
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
			num_people = 0
                        for i in range(len(self.hood[4][0].population)):
                                if(self.hood[4][0].population[i] == 'Person'):
                                        num_people += 1

                        if(num_people != len(self.hood[4][0].population)):
                                print 'You enter a house that is filled with monsters, will you attack or run?' #run just takes you outside
                        else:
                                print 'You enter a house filled with people!'
		if(location == [4, 1]):
			num_people = 0
                        for i in range(len(self.hood[4][1].population)):
                                if(self.hood[4][1].population[i] == 'Person'):
                                        num_people += 1

                        if(num_people != len(self.hood[4][1].population)):
                                print 'You enter a house that is filled with monsters, will you attack or run?' #run just takes you outside
                        else:
                                print 'You enter a house filled with people!'
		if(location == [4, 2]):
			print 'You are in a cemetary that continues North and East, there is a house South, and a road West.'
		if(location == [4, 3]):
			print 'You are in a cemetary that continues South and East, there is a house North, and a road west.'
		if(location == [4, 4]):
			num_people = 0
                        for i in range(len(self.hood[4][4].population)):
                                if(self.hood[4][4].population[i] == 'Person'):
                                        num_people += 1

                        if(num_people != len(self.hood[4][4].population)):
                                print 'You enter a house that is filled with monsters, will you attack or run?' #run just takes you outside
                        else:
                                print 'You enter a house filled with people!'
		if(location == [4, 5]):
			num_people = 0
                        for i in range(len(self.hood[4][5].population)):
                                if(self.hood[4][5].population[i] == 'Person'):
                                        num_people += 1

                        if(num_people != len(self.hood[4][5].population)):
                                print 'You enter a house that is filled with monsters, will you attack or run?' #run just takes you outside
                        else:
                                print 'You enter a house filled with people!'
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

	def game_over(self):
		print
		#check houses and health maybe update command or something
########################################################################################
#main method
########################################################################################
if __name__=="__main__":
	#create game (player, grid, houses, and monsters)
	game = Game()

	#intro message and game start
	print '\n\n********************************************************************************'
	print 'Welcome to Short Gritty Coffin\n(Name credit to random word generator)\n\nWould you like to play? (y/n)'
	print '********************************************************************************'
	answer = raw_input()
	if(answer == 'y' or answer == 'Y'):
		print '\nYou wake up out of your candy-induced coma in a comfortable, cultish, yet freaky garage. There is some candy on the ground, you pick it up and put it into your pocket.\n'
		game.play()
	else:
		exit(0)
	
