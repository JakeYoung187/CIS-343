from weapon import Weapon

import random

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
	#(used for 'i' command)
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
	def attack(self, house):
		power = self.attack_value + self.equipped_weapon.get_attack_mod()
		for i in range(len(house.get_population())):
			while(house.get_monster(i).get_health() > 0):
				health = house.get_monster(i).get_health()
				house.get_monster(i).set_health(health - power)
		num = self.equipped_weapon.get_num_uses() 
		self.equipped_weapon.set_num_uses(num - 1)
		if(self.equipped_weapon.get_num_uses() == 0):
			self.drop_weapon(self.equipped_weapon)
		

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
			
