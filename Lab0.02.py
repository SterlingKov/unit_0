'''
############
# Lab 0.02 #
############

In this lab, we will create a Pet class that will keep track of the type of animal, 
color, food, noise and name of a given animal.

Create a class called Pet that has the following attributes
Animal (e.g., dog, cat, fish)

Color (e.g., spotted, tabby, gold)

Food (e.g., kibbles, tuna, fish flakes)

Noise (e.g., meow, woof, splash)

Name (e.g., Scooby Doo, Fluffy, Bubbles)

Specifications
--------------
Make sure to use the __init__ method to create these attributes.

Create a list of pets.

Create a function that takes in a list of pets and prints out the name 
and the food attributes.

Test your function with your list of pets.
'''

class Pet():
    def __init__(self, animal, color, food, noise, name):
        self.animal = animal
        self.color = color
        self.food = food
        self.noise = noise
        self.name = name

def pet_info(list):
    for i in range(len(list)):
        print(f"{list[i].name} eats {list[i].food}")

dog = Pet('dog','brown','steak','woof','big boy')
cat = Pet('cat','gray','tuna','meow','death')
fish = Pet('fish','blue','other fish','splash','gideon')

pet_list = [dog,cat,fish]

pet_info(pet_list)