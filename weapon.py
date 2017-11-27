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


