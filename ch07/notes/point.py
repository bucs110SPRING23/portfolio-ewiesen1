'''
does stuff
'''
import random, pygame

class ColorPoint:
    """
    docstring for Point
    """

    def __init__(self, x=0, y=0, color = "red"): 
        self.xcoor = abs(x)
        self.ycoor = abs(y)
        self.on = True
        self.rect = pygame.Rect(abs(x), abs(y), 5, 5)
        self.color = color
        self.radius = 5

    def random_color(self):
        colors = ["red", "orange", "yellow", "green", "blue", "purple"]
        self.color = random.choice(colors)
    
    
    
    #no return