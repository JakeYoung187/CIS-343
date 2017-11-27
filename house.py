from observer import Observer
from monster import Monster

import random

###########################################################################
#House class creates an instance of a house on the grid
#@var population - the monsters 'living' in the house
#@var species - a list of monster species for random selection
###########################################################################
class House(Observer):
	population = 'empty'
	species = ['Zombie', 'Vampire', 'Ghoul', 'Werewolf', 'Person']
	def __init__(self):
		#super(House, self).__init__()
		self.population = []
		for x in range(random.randint(1, 5)):
			enemy = Monster(self.species[random.randint(0,4)])
			self.population.append(enemy)
			#enemy.add_observer(self)

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
	def update(self):
		for x in range(len(self.population)):
			self.population[x] = Monster('Person')
	
	##
	#Getter and setter
	##
	def get_population(self):
		return self.population
	def get_monster(self, x):
		return self.population[x]
	def set_monster(self, x, monster):
		self.population[x] = monster


