import turtle

t = turtle.Turtle()
print(type(t)) #complex
print(type(1)) #primitive

#classes are blueprints for objects
    #functions are stored algorithms
    #class as a stored data type
    #classes are not executable
    #don't put executable code in global scope, definitions are fine

#Point class
    #instance: an object created from a specific class
    #t = turtle.Turtle() ... t is an instance of Turtle
    #instance variable: an internal variable that is part of an instance
        #t.x, t.pos .... x and pos are instance variables
    #Interface: the functions and variables of an object
        #t.forward() ... forward() part of the interface of turtle

#Point - make a class ourself

#def make_Point(x,y)


class Point:
    #classes always start with a capital letter
    #usually, classes go in their own file
    #1 class per file
    #dunders = double underscores on both sides of the name

    def __init__(self): #self is the instance being created
        self.x = 0 # dot operator accesses instance variables of object
        self.x = 0
        self.y = 0
        self.color = ""

### main.py
import point #this error is here because this woudldn't actually work because its in the same file

p1 = point.Point()
p1.x = 10
#state of p1 (x=10, y=0, color = "")

p2 = point.Point()
p2.x = 5
#state of p1 (x=5, y=0, color = "")

p1.color = "red"