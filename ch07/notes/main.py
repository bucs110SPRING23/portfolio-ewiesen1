from point import ColorPoint
import point, random, turtle, pygame
from pygame import Rect



def mainloop(display):
    import pygame
    pygame.init()
    display = pygame.display.set_mode()
    points = []
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                point_deleted = False
                for i, p in enumerate(points):
                    if p.rect.collidepoint(event.pos):
                        del points[i]
                        point_deleted = True
                if not point_deleted:
                    p = point.Point(event.pos[0], event.pos[1]) 
                    #p = point.Point(*event.pos) #can use either one
                    points.append(p)
        display.fill("white")
        for p in points:
            pygame.draw.circle(display,p.color,p.rect.center, p.rect.h/2)
        pygame.display.flip()


def main():
    pygame.init
    display = pygame.display.set_mode()
    mainloop(display)

main()

#skinability - how easy it is to change the visual interface

#p1 = point.LED(x=100,y=100)

#points = []
#for p in range(10):
#    x = random.randint(0,100)
#    y = random.randint(0,100)
#    points.append(point.Point("orange"))



#pygame.draw.circle(display, p1.color, (p1.rect.x, p1.rect.y),p1.radius)

#while True:
#    pygame.display.flip()

#p1.xcoor = 10 

#print(p1.xcoor, p1.ycoor, p1.color, type(p1), id(p1))
#print(p2.xcoor, p2.ycoor, p2.color, type(p2), id(p2))

#points = []
#for p in range(10):
 #   x = random.randint(0,100)
 #   y = random.randint(0,100)
 #   points.append(point.Point("orange"))

#t = turtle.Turtle()
#for p in points:
 #   p.random_color()
  #  t.color(p.color)
  #  t.goto(p.xcoor, p.ycoor)