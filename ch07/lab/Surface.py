from Rectangle import Rectangle 

class Surface:
    def __init__(self, filename, x, y, h, w):
        """
        Initializing the rectangle using our code from Rectangle class
        args: self, filename, x,y,h,w --- (type) description
        return: None
        """
        self.image = str(filename)
        self.rect = Rectangle(x,y,h,w)
    def getRect(self):
        """
        general function description
        args: (type) description
        return: self.rect --- (type) description
        """
        return self.rect

