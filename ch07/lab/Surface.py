from Rectangle import Rectangle 

class Surface:
    def __init__(self, filename, x, y, h, w):
        """
        Setting my rectangle's appearance
        args: self, filename, x,y,h,w --- the instance of our class, rectangle's dimensions
        return: None
        """
        self.image = str(filename)
        self.rect = Rectangle(x,y,h,w)
    def getRect(self):
        """
        Returning the rectangle's appearance
        args: self --- the instance of our class
        return: self.rect 
        """
        return self.rect

