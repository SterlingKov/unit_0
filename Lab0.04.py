'''
############
# Lab 0.04 #
############

Overview
--------
Given the following Sample Code, practice using inheritance 
to create specific child classes for different types of Pokemon.

Create the three child classes below:
1. Water Type
When attacking a fire type, the attack is more effective

When attacking a grass type the effect is less effective

When growl is called print out Splish Splash

2. Fire Type
When attacking a water type, the attack is less effective

When attacking a grass type the effect is more effective

When growl is called print out "Fire Fire"

3. Grass Type
When attacking a water type, the attack is more effective

When attacking a fire type the effect is less effective

When growl is called print out "Cheep Cheep"

##############################################################
# Note: In order to check what type an object is you can use #
# isinstance which takes in an object, a class and returns a #
# Boolean if the object is the type of the inputted class.   #
##############################################################

Example Code
------------
my_pet = Pet()
isinstance(my_pet, Pet) # returns true
isinstance(my_pet, Dog) # returns false
'''
import random

class Pokemon():
    def __init__(self,name):
        self.name = name

#child classes
class WaterType(Pokemon):
    def __init__(self,name):
        Pokemon.__init__(self,name)
        self.name = name

class FireType(Pokemon):
    def __init__(self,name):
        Pokemon.__init__(self,name)
        self.name = name

class GrassType(Pokemon):
    def __init__(self,name):
        Pokemon.__init__(self,name)
        self.name = name

squirtle = WaterType('squirtle')
charizard = FireType('charizard')
bulbosaur = GrassType('bulbosaur')

poke_list = [squirtle,charizard,bulbosaur]
player_poke_inv = []

def rand_poke(list):
    return(list[random.randint(0,len(list)-1)])

while True:
    player_pokemon = input("Which pokemon would you like to chose?: squirtle, charizard, or bulbosaur? - ")
    if player_pokemon == squirtle.name:
        player_poke_inv.append(squirtle)
    random_pokemon = rand_poke(poke_list)
    print(f"A wild {random_pokemon.name} appeared! Which attack would you like to use?")
    move = input(f"growl - ")
    if move == 'growl':
        if isinstance(player_poke_inv[0], WaterType) and isinstance(random_pokemon, WaterType):
            print('splash splash')
        elif isinstance(player_poke_inv[0], WaterType) and isinstance(random_pokemon, FireType):
            print('splash splash')
            print('Your attack was super effective!')
        elif isinstance(player_poke_inv[0], WaterType) and isinstance(random_pokemon, GrassType):
            print('splash splash')
            print('Your attack was not very effective...')
        elif isinstance(player_poke_inv[0], FireType) and isinstance(random_pokemon, FireType):
            print('splash splash')
            print('Your attack was super effective!')