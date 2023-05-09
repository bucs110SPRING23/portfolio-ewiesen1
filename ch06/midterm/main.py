import turtle

def dist(shirt, width):
    """
    This function sets how long the shirt will be and how wide it will be.
    args: shirt, width 
    return: int
    """
    shirt = shirt
    width = width
    return shirt, width

def draw(color,shirt,width):
    """
    This function draws a shirt with turtle.
    args: color, shirt, width
    return: None
    """
    dist(shirt,width)
    sleeve = shirt/4
    sleevewidth = width/4
    screen = turtle.Screen()
    screen.bgcolor("mistyrose")
    turtle1 = turtle.Turtle()
    turtle1.color(color)
    turtle1.shape("circle")
    angle = 90
    measures = [sleeve,sleevewidth, sleeve+width,sleevewidth,sleeve]
    turtle1.fillcolor(color)

    turtle1.begin_fill()
    turtle1.down()

    turtle1.forward(width/2)
    turtle1.left(angle)
    turtle1.forward(shirt)
    turtle1.right(angle)

    for t in range(len(measures)):
        turtle1.forward(measures[t])
        turtle1.left(angle)

    turtle1.right(angle*2)
    turtle1.forward(shirt)
    turtle1.left(angle)
    turtle1.forward(width/2)

    turtle1.end_fill()

    screen.exitonclick()

def main():
    color = str(input("Enter a color for your shirt:"))
    shirt = int(input("Enter length for your shirt:"))
    width = int(input("Enter a width for you shirt:"))
    print(dist(shirt,width))
    draw(color,shirt,width)

    
main()
