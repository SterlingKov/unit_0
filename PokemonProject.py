import random
import sys

valid_int_inputs = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
valid_inputs = ['0', '1', '2', 'y', 'n']

def input_int_check(input):
    if input in valid_int_inputs:
        return True
    else:
        return False

def input_check(input):
    if input in valid_inputs:
        return True
    else:
        return False

#user class
class Player():
    def __init__(self,name):
        self.name = name
        self.pokemon = []
        self.current_pokemon = None
    def switch(self):
        if isinstance(self, Computer):
            self.current_pokemon = self.pokemon[random.randint(0, len(self.pokemon)-1)]
            print(f"{comp.name} threw out {self.current_pokemon.name}!")
            spacing()
        else:
            if len(self.pokemon) > 1:
                num = 1
                for poke in self.pokemon:
                    print(f"{num}. {poke.name} - HP: {poke.hp} - AP: {poke.ap}")
                    num += 1
                choice = input("Which pokemon would you like to chose? - ")
                if input_int_check(choice):
                    choice = int(choice)
                    self.current_pokemon = self.pokemon[choice-1]
                    print(f"You threw out {self.current_pokemon.name}")
                    spacing()
                else:
                    print(f"{choice} is not a valid input")
                    self.switch()
            else:
                print("this is your last pokemon")
                self.switch()   
    

#computer class
class Computer(Player):
    def __init__(self):
        c_names = ['Jerry', 'Jeff', 'Guy Man', 'Dude', 'Cynthia']
        name = c_names[random.randint(0,len(c_names)-1)]
        self.name = name
        self.pokemon = []
        self.current_pokemon = None

#pokemon classes
class Pokemon():
    def __init__(self,name,hp,ap):
        self.name = name
        self.MAX_HEALTH = hp
        self.hp = hp
        self.ap = ap
        self.type = self.set_type()
        self.attacks = self.set_attacks()
    def disp(self):
        return {
            self.name: [self.hp,self.ap]
        }

    def attack(self, enem_poke):
        num = 1
        for i in range(len(self.attacks)):
            print(f'{num}. {list(self.attacks)[i]}: POW:{self.attacks[list(self.attacks)[i]][0]} ACC:{self.attacks[list(self.attacks)[i]][1]}')
            num += 1
        move = input("which attack would you like to use? - ")
        if input_check(move):
            move = int(move) - 1
        else:
            print(f"{move} is not a valid input")
            self.attack()

        for i in range(len(self.attacks)):
            if i == move:
                print(f"{self.name} used {list(self.attacks)[i]}!")
                print('')
                if random.randint(0,100) <= list(self.attacks[list(self.attacks)[i]])[1]:
                    if list(self.attacks[list(self.attacks)[i]])[0] - self.ap > 0:

                        #print(list(self.attacks[list(self.attacks)[i]])[0] - self.ap)
                        enem_poke.hp -= random.randint(self.ap-20, self.ap)
                    else:

                        enem_poke.hp -= random.randint(list(self.attacks[list(self.attacks)[i]])[0]-20,list(self.attacks[list(self.attacks)[i]])[0])
                
                    if enem_poke.hp <= 0:  
                        print(f"{comp.name}'s health: 0")
                        spacing()
                    else:
                        print(f"{comp.name}'s health: {enem_poke.hp}")
                        spacing()
                else:
                    print("your attack missed")
                    spacing()
 
    def c_attack(self, enem_poke):
        move = random.randint(0, 2)
        for i in range(len(self.attacks)):
            if i == move:
                if random.randint(0,100) <= list(self.attacks[list(self.attacks)[i]])[1]:
                    if list(self.attacks[list(self.attacks)[i]])[0] - self.ap > 0:
                        enem_poke.hp -= random.randint(self.ap-20, self.ap)
                    else:
                        enem_poke.hp -= random.randint(list(self.attacks[list(self.attacks)[i]])[0]-20,list(self.attacks[list(self.attacks)[i]])[0])
                    if enem_poke.hp <= 0:
                        
                        print(f"{player.name}'s health: 0")
                    else:
                        print(f"{player.name}'s health: {enem_poke.hp}")
                else:
                    print(f"{comp.name}'s attack missed")
                    spacing()
        
    def heal(self):

        all_pokemon_list = [bulbosaur,bellsprout,oddish,charmander,ninetails,ponyta,squirtle,psyduck,polywag]
        for poke in all_pokemon_list:
            if self == poke:
                if self.hp > self.MAX_HEALTH - 20 and self.hp < self.MAX_HEALTH:
                    if poke == player.current_pokemon:
                        self.hp += self.MAX_HEALTH - self.hp
                        print(f'\nyou healed {self.MAX_HEALTH - self.hp} health!')
                        print(f"your hp: {self.hp}")
                        spacing()
                    else:
                        self.hp += self.MAX_HEALTH - self.hp
                        print(f'\n{comp.name} healed {self.MAX_HEALTH - self.hp} health!')
                        print(f"{comp.name}'s hp: {self.hp}")
                        spacing()
                elif self.hp == self.MAX_HEALTH:
                    if poke == player.current_pokemon:
                        print('your hp is full')
                        spacing()
                        battle()
                    else:
                        comp_battle()
                else:
                    if poke == player.current_pokemon:
                        self.hp += 20
                        print('you healed 20 hp!')
                        print(f"your hp: {self.hp}")
                        spacing()
                    else:
                        self.hp += 20
                        print(f"{comp.name} healed 20 hp!")
                        print(f"{comp.name}'s hp: {self.hp}")
                        spacing()
    
    

#child classes
class WaterType(Pokemon):
    def set_type(self):
        return 'water'
    def set_attacks(self):
        return {
            'Bubble': [30, 100],
            'Hydro Pump': [80, 30],
            'Surf': [45, 90]
        }

class FireType(Pokemon):
    def set_type(self):
        return 'fire'
    def set_attacks(self):
        return {
            'Ember': [45, 90],
            'Fire Punch': [35, 100],
            'Flame Wheel': [55, 95]
        }
        

class GrassType(Pokemon):
    def set_type(self):
        return 'grass'
    def set_attacks(self):
        return {
            'Leaf Storm': [70, 90],
            'Mega Drain': [35, 100],
            'Razor Leaf': [45, 95]
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

def spacing():
    print("")
    input("press ENTER ")
    print("")



#game
def poke_choice(list, list_names):
    am_ls = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range(0, 3):
        num = 1
        for poke in list:
            print(f"{num}. {poke.name} - HP: {poke.hp} - AP: {poke.ap}")
            num += 1 

        c = input(f'select one pokemon to add to your team - ')

        while c not in am_ls:
            print("not a valid pokemon")
            c = input(f'select one pokemon to add to your team - ')
        am_ls.pop(-1)
        c = int(c)
            
        print("")

        player.pokemon.append(list[c-1])
        list.pop(c-1)
        list_names.pop(c-1)
        
        comp.pokemon.append(list[random.randint(0,len(list)-1)])
        am_ls.pop(-1)
        list.pop(list_names.index(comp.pokemon[i].name))
        list_names.pop(list_names.index(comp.pokemon[i].name))
        print(f'{comp.name} chose {comp.pokemon[i].name}!')
        spacing()
    num = 1
    for poke in player.pokemon:
        print(f"{num}. {poke.name} - HP: {poke.hp} - AP: {poke.ap}")
        num += 1
    poke_start = int(input(f"which pokemon do you want to start with? - "))
    print('')
    player.current_pokemon = player.pokemon[poke_start-1]
    comp.current_pokemon = comp.pokemon[random.randint(0, len(comp.pokemon)-1)]

    print(f"You chose {player.current_pokemon.name}!")
    spacing()
    print(f"{comp.name} threw out {comp.current_pokemon.name}!")
    spacing()

dead_comp = []
dead_player = []

def battle():
    
    moves = ['attack', 'heal', 'switch']

    while player.current_pokemon.hp > 0 and comp.current_pokemon.hp > 0:
        
        num = 1
        for i in range(0, len(moves)):
                    print(f"{num}. {moves[i]}")
                    num += 1
        move = input("pick a move - ")
        print('')
        if move == '1':
                player.current_pokemon.attack(comp.current_pokemon)
                if comp.current_pokemon.hp <= 0:
                    dead_comp.append(comp.current_pokemon)
                    
                    comp.pokemon.pop(comp.pokemon.index(comp.current_pokemon))
                    check_for_win()
                    comp.current_pokemon = comp.pokemon[random.randint(0,len(comp.pokemon)-1)]
                    print(f"{comp.name} threw out {comp.current_pokemon.name}!")
                    spacing()
        elif move == '2':
            player.current_pokemon.heal()
        elif move == '3':
            player.switch()
        else:
            print('not a valid input')
            print('')
            battle()
        comp_battle()

def comp_battle():
    c_move = random.randint(0,2)
    if c_move < 1:
        comp.current_pokemon.c_attack(player.current_pokemon)
        if player.current_pokemon.hp <= 0:
                dead_player.append(player.current_pokemon)
                
                player.pokemon.pop(player.pokemon.index(player.current_pokemon))
                check_for_win()
                num = 1
                for poke in player.pokemon:
                    print(f"{num}. {poke.name} - HP: {poke.hp} - AP: {poke.ap}")
                    num += 1
                poke_choice = int(input(f"which pokemon would you like to throw out? - "))
                print('')
                player.current_pokemon = player.pokemon[poke_choice-1]
                print(f"{player.name} threw out {player.current_pokemon.name}!") 
                spacing()
    elif c_move == 1:
        comp.current_pokemon.heal()
    elif c_move == 2:
        if len(comp.pokemon) > 1:
            comp.switch()
        else:
            comp_battle()
                



def check_for_win():
    if len(dead_comp) == 3:
        print('you won')
        i = input("would you like to play again? (y/n) - ")
        if i == 'y':
            game()
        elif i == 'n':
            sys.exit()
    elif len(dead_player) == 3:
        print("you lost")
        i = input("would you like to play again? (y/n) - ")
        if i == 'y':
            game()
        elif i == 'n':
            sys.exit()


#game loop
def game():
    global player
    global comp
    while True:
        #pokemon
        pokemon_list = [bulbosaur,bellsprout,oddish,charmander,ninetails,ponyta,squirtle,psyduck,polywag]
        poke_ls_names = [bulbosaur.name,bellsprout.name,oddish.name,charmander.name,ninetails.name,ponyta.name,squirtle.name,psyduck.name,polywag.name]

        player = Player(input("What is your name? - "))
        spacing()
        comp = Computer()

        print(f"Oh no! {comp.name} wants to fight!")
        spacing()

        poke_choice(pokemon_list,poke_ls_names)

        while True:
            battle()

game()