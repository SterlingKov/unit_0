'''
###############
# Do Now 0.04 #
###############

In your Console
---------------
Type the following:

class Pet():
  def __init__(self, name):
    self.name =  name
  def make_noise(self):
    print("Noise!")

class Dog(Pet):
  dog1 = Dog()
  dog1.make_noise()

In your Notebook
----------------
Respond to the following

1.  What is the output when you run this code?

Continue in the console
-----------------------
Rewrite the code to resolve the error and make this work properly

Continue in your notebook
-------------------------
What happens when you call method make_noise?
'''

class Pet():
  def __init__(self, name):
    self.name =  name
  def make_noise(self):
    print("Noise!")

class Dog(Pet):
  def __init__(self, name):
    super().__init__(name)
dog1 = Dog('bob')
dog1.make_noise()