import point, random, turtle, pygame

pygame.init()
display = pygame.display.set_mode()


p1 = point.LED(x=100,y=100)

points = []
for p in range(10):
    x = random.randint(0,100)
    y = random.randint(0,100)
    points.append(point.Point("orange"))


pygame.draw.circle(display, p1.color, (p1.rect.x, p1.rect.y),p1.radius)

while True:
    pygame.display.flip()

#p2 = point.Point(3,4, "yellow")

p1.xcoor = 10 

print(p1.xcoor, p1.ycoor, p1.color, type(p1), id(p1))
print(p2.xcoor, p2.ycoor, p2.color, type(p2), id(p2))

points = []
for p in range(10):
    x = random.randint(0,100)
    y = random.randint(0,100)
    points.append(point.Point("orange"))

t = turtle.Turtle()
for p in points:
    p.random_color()
    t.color(p.color)
    t.goto(p.xcoor, p.ycoor)

turtle.Screen().exitonclick()