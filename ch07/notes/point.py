import random, pygame

class ColorPoint:
    """
    docstring for Point
    """

    def __init__(self, x=0, y=0): 
        #self.xcoor = abs(x)
        #self.ycoor = abs(y)
        self.on = True
        self.rect = pygame.Rect(abs(x), abs(y), 20, 20)
        self.color = self.random_color()


    def random_color(self):
        return (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        
    #no return