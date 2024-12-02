import turtle 
screen = turtle.Screen()
screen.bgcolor("white")
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.speed(2.5)

def draw_star(size):
    my_turtle.color("yellow")
    my_turtle.begin_fill()
    for _ in range(5):
        my_turtle.forward(size)
        my_turtle.right(144)
        my_turtle.forward(size)
        my_turtle.left(72)
    my_turtle.end_fill()

def draw_rectangle(width, height):
    my_turtle.color("red")
    my_turtle.penup()
    my_turtle.goto(-width / 2, height / 2)
    my_turtle.pendown()
    my_turtle.begin_fill()
    for _ in range(2):
        my_turtle.forward(width)
        my_turtle.right(90)
        my_turtle.forward(height)
        my_turtle.right(90)
    my_turtle.end_fill()

reactangle_width = 600
reactangle_height = 400
draw_rectangle(reactangle_width, reactangle_height)

my_turtle.penup()
my_turtle.goto(25, 20)
my_turtle.pendown()
draw_star(100)

my_turtle.hideturtle()
turtle.done()