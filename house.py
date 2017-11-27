from observer import Observer
from monster import Monster

import random

###########################################################################
#House class creates an instance of a house on the grid
#@var population - the monsters 'living' in the house
#@var species - a list of monster species for random selection
###########################################################################
class House(Observer):
	num_monsters = 0
	population = 'empty'
	species = ['Zombie', 'Vampire', 'Ghoul', 'Werewolf', 'Person']
	def __init__(self):
		self.population = []
		for x in range(random.randint(1, 5)):
			enemy = Monster(self.species[random.randint(0,4)], self)
			self.population.append(enemy)
			if(enemy.get_species() is not 'Person'):
				self.num_monsters += 1

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
	def update(self, monster):
		for monsters in self.population:
			print 'here'
			if monsters.get_species() is monster:
				print monsters
				monsters.change(monsters)
				self.num_monsters -= 1
				break
	
	##
	#Getter and setter
	##
	def get_population(self):
		return self.population
	def get_monster(self, x):
		return self.population[x]
	def set_monster(self, x, monster):
		self.population[x] = monster
	def get_num_monsters(self):
		return self.num_monsters
	def set_num_monsters(self, num):
		self.num_monsters = num

