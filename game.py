from observer import Observer
from player import Player
from house import House

import re

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
	monsters_left = 0
	def __init__(self):
		#placing houses (10)
		self.hood[0][5] = House()
		self.hood[1][0] = House()
		self.hood[1][5] = House()
		self.hood[2][5] = House()
		self.hood[2][0] = House()
		self.hood[3][0] = House()
		self.hood[4][0] = House()
		self.hood[4][1] = House()
		self.hood[4][4] = House()
		self.hood[4][5] = House()
		self.total_monsters()
		
	##
	#play creates the loop to accept commands from the user
	##
	def play(self):
		print '\nThere are walls all around you, but an open door in front of you. Where would you like to go?\n'
		while(self.end_of_game is 'false'):
			print '\n**Type help for a list of commands**'
			print 'Health:', self.hero.get_health()
			print 'Equipped Candy:', self.hero.get_equipped_weapon().get_weapon_name()
			print 'Monsters left: ', self.monsters_left
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
	#total_monsters calculates the number of monsters spawned in the game
	##
	def total_monsters(self):
		self.monsters_left = 0
		for a in range(6):
			for b in range(6):
				if(isinstance(self.hood[a][b], House)):
					self.monsters_left += self.hood[a][b].get_num_monsters()

	##
	#Getters and setters
	##
	def get_monsters_left():
		return self.monsters_left
	def set_monsters_left(x):
		self.monsters_left = x
	
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
		
		player.attack(house)
		house.get_monster(0).attack(player, temp)
		self.total_monsters()

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
			print '\nOther commands: quit, fight, (h)heal (when in a healed house), i (to display inventory), and c (change equipped weapon)\n\n'
			print 'Attack monsters to turn them back into people, once you clear a house completely of monsters, you will be able to heal yourself using the \'heal\' command when inside of the house.'
		if(cmd == 'quit'):
			exit(0)
		if(cmd == 'n' or cmd == 's' or cmd == 'e' or cmd == 'w'):
			self.hero.move(cmd)
		if(cmd == 'h'):
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
			if(self.hood[0][5].get_monster(0).get_species() == 'Person'):
				print 'You enter a house filled with people!'
			else:
				print 'You enter a house that is filled with', len(self.hood[0][5].get_population()), 'monsters, will you attack or run?'
			self.hood[0][5].show_monsters(self.hood[0][5])
		if(location == [1, 0]):
			if(self.hood[1][0].get_monster(0).get_species() == 'Person'):
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
			if(self.hood[1][5].get_monster(0).get_species() == 'Person'):
                                print 'You enter a house filled with people!'
                        else:
                                print 'You enter a house that is filled with', len(self.hood[1][5].get_population()), 'monsters, will you attack or run?'
			self.hood[1][5].show_monsters(self.hood[1][5])
		if(location == [2, 0]):
			if(self.hood[2][0].get_monster(0).get_species() == 'Person'):
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
			if(self.hood[2][5].get_monster(0).get_species() == 'Person'):
                                print 'You enter a house filled with people!'
                        else:
                                print 'You enter a house that is filled with', len(self.hood[2][5].get_population()), 'monsters, will you attack or run?'
			self.hood[2][5].show_monsters(self.hood[2][5])
		if(location == [3, 0]):
			if(self.hood[3][0].get_monster(0).get_species() == 'Person'):
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
			if(self.hood[4][0].get_monster(0).get_species() == 'Person'):
                                print 'You enter a house filled with people!'
                        else:
                                print 'You enter a house that is filled with', len(self.hood[4][0].get_population()), 'monsters, will you attack or run?'
			self.hood[4][0].show_monsters(self.hood[4][0])
		if(location == [4, 1]):
			if(self.hood[4][1].get_monster(0).get_species() == 'Person'):
                                print 'You enter a house filled with people!'
                        else:
                                print 'You enter a house that is filled with', len(self.hood[4][1].get_population()), 'monsters, will you attack or run?'
			self.hood[4][1].show_monsters(self.hood[4][1])
		if(location == [4, 2]):
			print 'You are in a cemetary that continues North and East, there is a house South, and a road West.'
		if(location == [4, 3]):
			print 'You are in a cemetary that continues South and East, there is a house North, and a road west.'
		if(location == [4, 4]):
			if(self.hood[4][4].get_monster(0).get_species() == 'Person'):
                                print 'You enter a house filled with people!'
                        else:
                                print 'You enter a house that is filled with', len(self.hood[4][4].get_population()), 'monsters, will you attack or run?'
			self.hood[4][4].show_monsters(self.hood[4][4])
		if(location == [4, 5]):
			if(self.hood[4][5].get_monster(0).get_species() == 'Person'):
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
		if(self.hero.get_health() <= 0):
			self.end_of_game = 'loss'

		if(self.monsters_left == 0):
			self.end_of_game = 'win'	
