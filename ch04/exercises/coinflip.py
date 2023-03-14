import turtle, random

#def is_in_screen 

window = turtle.Screen()
window.bgcolor("grey")

pen = turtle.Turtle()
pen.color("pink")
pen.shape("turtle")

distance = 50
angle = 90
is_in_screen = True

while is_in_screen:
    flip = random.randint(1,2)
    if flip == 1:
        pen.left(angle)
    elif flip:
        pen.right(angle)
    pen.forward(distance)

    turtleX = pen.xcor()
    turtleY = pen.ycor()

    x_range = window.window_width()/2
    y_range = window.window_height()/2

    if abs(turtleX) > x_range or abs(turtleY) > y_range:
        is_in_screen = False

window.exitonclick()
    