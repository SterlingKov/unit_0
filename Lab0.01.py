'''
############
# Lab 0.01 #
############

In this lab we will create a class that will represent colors 
and build a function to combine two colors.


1.  Create a class, Color.
2.  Instantiate at least 3 colors.
3.  Add attributes of r, g, and b to those instances.
4.  Create a function, add_color, which takes in two colors 
    and returns a color that is the sum of the two reds, greens, 
    and blues. Don't forget: the maximum value for R, G, or B is 255.
'''
RED = (255,0,0)
GREEN=(0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)

class Color():
    def __init__(self, color):
        self.color = color
        self.r = self.color[0]
        self.g = self.color[1]
        self.b = self.color[2]
        

color1 = Color(RED)
color2 = Color(GREEN)
color3 = Color(BLUE)

def add_color(c1,c2):
    nc = Color(BLACK)
    if c1.r + c2.r > 255:
        nc.r = 255
    else:
        nc.r = c1.r + c2.r
    if c1.g + c2.g > 255:
        nc.g = 255
    else:
        nc.g = c1.g + c2.g
    if c1.b + c2.b > 255:
        nc.b = 255
    else:
        nc.b = c1.b + c2.b
    nc.color = nc.r,nc.g,nc.b
    return nc


color4 = add_color(color1,color2)

color5 = add_color(color2,color3)

color6 = add_color(color1,color3)

print(color4.r,color4.g,color4.b)
print(color5.r,color5.g,color5.b)
print(color6.r, color6.g,color6.b)