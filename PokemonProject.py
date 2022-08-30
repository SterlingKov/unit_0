import random

#user class
class Player():
    def __init__(self,name):
        self.name = name
        name = input("What is your name? - ")
        self.pokemon = []
        self.current_pokemon = None

    def attack():
        pass
    def heal():
        pass
    def switch():
        pass
    def print_choices():
        pass

#computer class
class Computer(Player):
    def __init__(self):
        c_names = ['Jerry', 'Jeff', 'Guy Man', 'Dude', 'Cynthia']
        name = c_names[random.randint(0,len(c_names)-1)]
        self.name = name

#pokemon classes
class Pokemon():
    def __init__(self,name,hp,ap):
        self.name = name
        self.hp = hp
        self.ap = ap
        self.type = self.set_type()
        self.attacks = self.set_attacks()
        

#child classes
class WaterType(Pokemon):
    def set_type(self):
        return 'water'
    def set_attacks(self):
        return {
            'Bubble': [40, 100],
            'Hydro Pump': [185, 30],
            'Surf': [70, 90]
        }

class FireType(Pokemon):
    def set_type(self):
        return 'fire'
    def set_attacks(self):
        return {
            'Ember': [130, 90],
            'Fire Punch': [50, 100],
            'Flame Wheel': [55, 95]
        }
        

class GrassType(Pokemon):
    def set_type(self):
        return 'grass'
    def set_attacks(self):
        return {
            'Leaf Storm': [130, 90],
            'Mega Drain': [50, 100],
            'Razor Leaf': [55, 95]
        }
        

#--pokemon--
#grass
bulbosaur = GrassType('bulbosaur',60,40)
bellsprout = GrassType('bellsprout',40,60)
oddish = GrassType('oddish',50,50)

#fire
charmander = FireType('charmander',25,70)
ninetails = FireType('ninetails',30,50)
ponyta = FireType('ponyta',40,60)

#water
squirtle = WaterType('squirtle',80,20)
psyduck = WaterType('psyduck',70,40)
polywag = WaterType('polywag',50,50)

pokemon_list = [bulbosaur,bellsprout,oddish,charmander,ninetails,ponyta,squirtle,psyduck,polywag]

#computer stuff



#game and game loop

# while True:
#     comp = Computer()
#     print(f"Oh no! {comp.name} wants to fight!")

print(charmander.attacks)