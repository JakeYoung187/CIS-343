from game import Game

import sys
import os

########################################################################################
#main method used to create an instance of the game and to print the intro messages.
########################################################################################
if __name__=="__main__":
	#create game
	game = Game()

	#intro message and game start
	print '\n\n**********************************************************'
	print 'Type \'start\' to begin!'
	print '***********************************************************'
	answer = raw_input()
	if(answer == 'start'):
		print '\n\n\n\n\n\n\n\nYou wake up out of your candy-induced coma in a detatched garage. All of your friends and family have been turned into monsters by a bad batch of candy! You must fight to turn them back into the people they once were. There is some candy on the ground, you pick it up and put it into your pocket, use the candy to attack monsters. (type \'i\' for your inventory)\n'
		#start game loop
		game.play()
		print 'Would you like to play again? (y/n)'
		answer = raw_input()
		if(answer == 'y' or answer == 'Y'):
			os.execl(sys.executable, sys.executable, *sys.argv)
	else:
		exit(0)
	
