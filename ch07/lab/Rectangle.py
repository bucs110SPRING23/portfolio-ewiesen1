

class Rectangle:

    def __init__(self, x, y, h, w): 
        """
        general function description
        args: (type) description
        return: (type) description
        """
        self.x = abs(x)
        self.y = abs(y)
        self.height = abs(h)
        self.width = abs(w)
    def __str__(self):
        """
        general function description
        args: (type) description
        return: (type) description
        """
        
        rect = "(x: {self.x}, y: {self.y}), width: {self.width}, height: {self.height}"
        return rect