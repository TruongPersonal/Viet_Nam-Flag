from turtle import *

# Screen setup
screen = Screen()
screen.title('Viet Nam Flag')
screen.bgcolor('white')
screen.setup(width=1.0, height=1.0)
screen.cv._rootwindow.resizable(False, False)

# Turtle setup
my_turtle = Turtle()
my_turtle.hideturtle()
my_turtle.shape('turtle')
my_turtle.speed(2.5)

flag_drawn = False

# Calculate scale factor
default_width = 1600  # Default design width
default_height = 1200  # Default design height
screen_width = screen.window_width()
screen_height = screen.window_height()
scale_factor = min(screen_width / default_width, screen_height / default_height)

# Functions
def draw_star(size, shadow=False):
    my_turtle.color('#ba2921' if shadow else '#e9eb4d')
    my_turtle.begin_fill()
    for _ in range(5):
        my_turtle.forward(size)
        my_turtle.right(144)
        my_turtle.forward(size)
        my_turtle.left(72)
    my_turtle.end_fill()

def draw_rectangle(width, height, shadow=False, offset_y=0):
    my_turtle.color('#3b0703' if shadow else '#8d1d14')
    my_turtle.penup()
    offset = -15 * scale_factor if shadow else 0
    my_turtle.goto(-width / 2 + offset, height / 2 + offset_y - offset)
    my_turtle.pendown()
    my_turtle.begin_fill()
    for _ in range(2):
        my_turtle.forward(width)
        my_turtle.right(90)
        my_turtle.forward(height)
        my_turtle.right(90)
    my_turtle.end_fill()

def draw_flagpole(height, width, offset_y=0):
    my_turtle.color('#d6d6d4')
    my_turtle.penup()
    my_turtle.goto(-width / 2 - 20 * scale_factor, height / 2 + offset_y + 40 * scale_factor)
    my_turtle.pendown()
    my_turtle.begin_fill()
    for _ in range(2):
        my_turtle.forward(20 * scale_factor)
        my_turtle.right(90)
        my_turtle.forward(height + 550 * scale_factor)
        my_turtle.right(90)
    my_turtle.end_fill()

    # Draw the base of the flagpole
    base_width = 60 * scale_factor
    base_height = 40 * scale_factor
    my_turtle.color('#a8a8a8')
    my_turtle.goto(-width / 2 - 40 * scale_factor, -height - 270 * scale_factor + offset_y - base_height)
    my_turtle.begin_fill()
    for _ in range(2):
        my_turtle.forward(base_width)
        my_turtle.right(90)
        my_turtle.forward(base_height)
        my_turtle.right(90)
    my_turtle.end_fill()

# Main drawing logic (called on click)
def draw_flag(x, y):
    global flag_drawn
    if flag_drawn:
        return

    my_turtle.showturtle()
    flag_drawn = True

    offset_y = 250 * scale_factor

    # Draw shadow rectangle
    rectangle_width = 600 * scale_factor
    rectangle_height = 400 * scale_factor
    draw_rectangle(rectangle_width, rectangle_height, shadow=True, offset_y=offset_y)

    # Draw rectangle
    draw_rectangle(rectangle_width, rectangle_height, offset_y=offset_y)

    # Draw shadow star
    my_turtle.penup()
    my_turtle.goto(35 * scale_factor, 10 * scale_factor + offset_y)
    my_turtle.pendown()
    draw_star(100 * scale_factor, shadow=True)

    # Draw star
    my_turtle.penup()
    my_turtle.goto(25 * scale_factor, 20 * scale_factor + offset_y)
    my_turtle.pendown()
    draw_star(100 * scale_factor)

    # Draw flagpole
    draw_flagpole(rectangle_height, rectangle_width, offset_y=offset_y)

    # Finish
    my_turtle.hideturtle()

# Set click event
screen.onscreenclick(draw_flag)

# Keep the window open
screen.mainloop()