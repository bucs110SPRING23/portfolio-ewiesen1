

class Rectangle:

    def __init__(self, x, y, h, w): 
        """
        In this function we are setting up our rectangle's location in space
        args: self, x, y, h, w - instance of the class, the dimensions of the rectangle we will be drawing
        return: None
        """
        self.x = abs(x)
        self.y = abs(y)
        self.height = abs(h)
        self.width = abs(w)
    def __str__(self):
        """
        Saving the dimensions of my rectange 
        args: self (type) instance of the class
        return: rect (str) dimentions of rectangle
        """
        
        rect = "(x: {self.x}, y: {self.y}), width: {self.width}, height: {self.height}"
        return rect