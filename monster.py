from observable import Observable

import random

###########################################################################
#Monster class creates the monsters to be added into the houses
#@var health - the health of the monster
#@var species - the type of monster (zombie, person, etc.)
#@var attack_value - the amount of damage the can do to the player
###########################################################################
class Monster(Observable):
	health = 0
	species = ''
	attack_value = 0
	def __init__(self, species, house):
		super(Monster, self).__init__()
		self.add_observer(house)
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
		monster.species = 'Person'
		monster.health = 100
		monster.attack_value = -2
	##
	#methods for Observer pattern
	##
	def update(self):
		for observer in self.observers:
			observer.update(self.species)
	
	##
	#Getters and setters
	##
	def get_health(self):
		return self.health
	def set_health(self, health):
		self.health = health
		if(self.health <= 0):
			if(self.species is not 'Person'):
				self.update()
	
	def get_attack_value(self):
		return self.attack_value
	def set_attack_value(self, atk):
		self.attack_value = atk
	def get_species(self):
		return self.species
	def set_species(self, species):
		self.species = species


