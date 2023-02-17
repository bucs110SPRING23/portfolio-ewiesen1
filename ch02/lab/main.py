import turtle #1. import modules
import random
import pygame
import math
pygame.init()

#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here
#race 1
x = random.randrange(1,101)

michelangelo.forward(x)
leonardo.forward(x)
michelangelo.up()
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

#race 2

for i in range(1):
    y = random.randrange(1,11)
    z = random.randrange(1,11)
    michelangelo.forward(y)
    leonardo.forward(z)
    michelangelo.goto(-100,20)
    leonardo.goto(-100,-20)

window.exitonclick()

# PART B - complete part B here


window = pygame.display.set_mode()
window.fill("lightblue")
points = []
num_side = [3,4,6,20,100,360]
side_length = 100
#[10, 10, 10, 5, 5, 5]
#side_length = int(side_length)
color = ["pink", "yellow", "green", "purple", "orange", "black"]
xpos = 650
ypos = 400

for s in range(len(num_side)):
    for i in range(num_side[s]):
        angle = 360/num_side[s]
        radians = math.radians(angle*i)
        x = xpos + side_length*math.cos(radians)
        y = ypos +side_length*math.sin(radians)
        points.append([x,y])
pygame.draw.polygon(window, color[s], points, side_length)
pygame.display.flip()
pygame.time.wait(1000)
window.fill("blue")
pygame.display.flip()
points = []
#pygame.time.wait(1000)
    




