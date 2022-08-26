'''
##############
## Lab 0.03 ##
##############

Instructions:
-------------
1.  Finish writing the __add__ method for the time class from the Do Now.

2.  Write a definition for a class named Kangaroo with the following methods:

    An __init__ method that initializes an attribute named pouch_contents to an empty list.

    A method named put_in_pouch that takes an object of any type and adds it to pouch_contents.

    A __str__ method that returns a string representation of the Kangaroo object and the contents of the pouch.



Tips to give students:
----------------------
- This exercise is a cautionary tale about one of the most common, and difficult to find, errors in Python

- TypeError: Can't convert 'list' object to str implicitly

- Use the str() function to convert the list object to a string.

- Test your code by creating two Kangaroo objects

    assign them to variables named kanga and roo

    add roo to the contents of kanga's pouch

class Kangaroo():
    def __init__ (self,name):
        self.name = name
        self.pouch_contents = []
    def put_in_pouch(self,thing):
        self.pouch_contents.append(str(thing))
    def __str__ (self):
        return f"{self.name}'s pouch contents: {self.pouch_contents}"

roo = Kangaroo('roo')
kanga = Kangaroo('kanga')
kanga.put_in_pouch()

print(kanga)

Extra Credit
------------
Return to your Pet class from Lab 7.02. Research the isinstance function to write a method, 
is_friend that will take in another pet and return True if the two pets are friends, and 
false if they are not.

Rules:
------
- If they are both dogs they are friends.

- If the instance is a dog and the other pet is a cat, they are friends.

- If the instance is a cat and the other is a dog they are not friends.

- If they are both cats they are not friends.
'''

class Pet():
    def __init__(self, animal, color, food, noise, name):
        self.animal = animal
        self.color = color
        self.food = food
        self.noise = noise
        self.name = name
    def is_friend(self,pet):
        if isinstance(self, Pet) and isinstance(pet,Pet):
            if self.animal == 'dog' and pet.animal == 'dog':
                print('They are both dogs and they are friends')
            elif self.animal == 'dog' and pet.animal == 'cat':
                print('One is a dog and the other is a cat, not friends')
            elif self.animal == 'cat' and pet.animal == 'dog':
                print('One is a dog and the other is a cat, not friends')
            else:
                print('Both are cats, not friends')
        else:
            print('not a Pet class')

def pet_info(list):
    for i in range(len(list)):
        print(f"{list[i].name} eats {list[i].food}")

dog = Pet('dog','brown','steak','woof','big boy')
dog2 = Pet('dog','red','flesh','WOOF','clifford')
cat = Pet('cat','gray','tuna','meow','death')
fish = Pet('fish','blue','other fish','splash','gideon')

# pet_list = [dog,cat,fish]

# pet_info(pet_list)

cat.is_friend(cat)

