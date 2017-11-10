import random

playerItems = []

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

class Weapon:
	name = ''
	attack_mod = 0
	num_uses = -1
	def __init__(self, name, atk, use):
		self.name = name
		self.attack_mod = atk
		self.num_uses = use

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
		if(direction == 'N'):
			if(self.current_location[1] != 5):
				self.current_location[1] += 1
			else:
				print 'Cannot go in that direction'
		if(direction == 'S'):
			if(self.current_location[1] != 0):
				self.current_location[1] -= 1
			else:
				print 'Cannot go in that direction'
		if(direction == 'E'):
			if(self.current_location[0] != 5):
				self.current_location[0] += 1
			else:
				print 'Cannot go in that direction'
		if(direction == 'W'):
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
	def attack(self, monster):
		power = self.attack_value+self.equipped_weapon.attack_mod
		if(monster.species == 'Person'):
			return
		monster.health -= power
		if(monster.health <= 0):
			monster.change(monster)
		self.equipped_weapon.num_uses -= 1
		if(self.equipped_weapon.num_uses == 0):
			self.drop_weapon(self.equipped_weapon)		

class Monster():
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
			self.attack_value = -1
	def attack(self, player):
		player.health -= self.attack_value
		if(player.health <= 0):
			#gameover
			print
	def change(self, monster):
		monster.species = 'Person'
		monster.health = 100
		monster.attack_value = -1

class Location():
	loc_type = ''
	def __init__(self, lType):
		self.loc_type = lType

class House():
	population = []
	species = ['Zombie', 'Vampire', 'Ghoul', 'Werewolf','Person']
	loc_type = 'House'
	def __init__(self):
		for i in range(random.randint(1,5)):
			enemy = Monster(self.species[random.randint(0,4)])
			self.population.append(enemy)
	def show_monsters(self, house):
			r = len(house.population)
			for i in range(r):
				print house.population[i].species

if __name__=="__main__":
	#create character
	hero = Player()

	#create the grid
	hood = [[Location('Empty') for i in range(3)] for j in range(3)]
	hood[1][0] = House()
	#printing monsters for testing	
	for i in range(len(hood[1][0].population)):
		print hood[1][0].population[i].species

	while(1):
		print 'You are at 0,0 where would you like to move?'
		direction = raw_input()
		hero.move(direction)
		print hero.current_location,"\n"
		x = hero.current_location[0]
		y = hero.current_location[1]
		if(hood[x][y].loc_type == 'House'):
			print 'You have entered a house.'
			hood[x][y].show_monsters(hood[x][y])
			#use print method to show what is in the house
