import turtle

# Screen setup
screen = turtle.Screen()
screen.title('Viet Nam Flag')
screen.bgcolor('white')
screen_width = screen.window_width()
screen_height = screen.window_height()
screen.setup(width = 1.0, height = 1.0)

# Turtle setup
my_turtle = turtle.Turtle()
my_turtle.hideturtle()
my_turtle.shape('turtle')
my_turtle.speed(2.5)

flag_drawn = False

def draw_star(size, shadow = False):
    my_turtle.color('#ba2921' if shadow else '#e9eb4d')
    my_turtle.begin_fill()
    for _ in range(5):
        my_turtle.forward(size)
        my_turtle.right(144)
        my_turtle.forward(size)
        my_turtle.left(72)
    my_turtle.end_fill()

def draw_rectangle(width, height, shadow = False, offset_y = 0):
    my_turtle.color('#3b0703' if shadow else '#8d1d14')
    my_turtle.penup()
    offset = -15 if shadow else 0
    my_turtle.goto(-width / 2 + offset, height / 2 + offset_y - offset)
    my_turtle.pendown()
    my_turtle.begin_fill()
    for _ in range(2):
        my_turtle.forward(width)
        my_turtle.right(90)
        my_turtle.forward(height)
        my_turtle.right(90)
    my_turtle.end_fill()

def draw_flagpole(height, width, offset_y = 0):
    my_turtle.color('#d6d6d4')
    my_turtle.penup()
    my_turtle.goto(-width / 2 - 20, height / 2 + offset_y + 40)
    my_turtle.pendown()
    my_turtle.begin_fill()
    for _ in range(2):
        my_turtle.forward(20)
        my_turtle.right(90)
        my_turtle.forward(height + 550)
        my_turtle.right(90)
    my_turtle.end_fill()
    
    # my_turtle.penup()
    base_width = 60 
    base_height = 40
    my_turtle.color('#a8a8a8')
    my_turtle.goto(-width / 2 - 40, -height - 270 + offset_y - base_height)
    # my_turtle.pendown()
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

    offset_y = 250

    # Draw shadow rectangle
    rectangle_width = 600
    rectangle_height = 400
    draw_rectangle(rectangle_width, rectangle_height, shadow = True, offset_y = offset_y)

    # Draw rectangle
    draw_rectangle(rectangle_width, rectangle_height, offset_y = offset_y)

    # Draw shadow star
    my_turtle.color('#ba2921')
    my_turtle.penup()
    my_turtle.goto(35, 10 + offset_y)
    my_turtle.pendown()
    draw_star(100, shadow = True)

    # Draw star
    my_turtle.penup()
    my_turtle.goto(25, 20 + offset_y)
    my_turtle.pendown()
    draw_star(100)

    # Draw flagpole
    draw_flagpole(rectangle_height, rectangle_width, offset_y = offset_y)

    # Finish
    my_turtle.hideturtle()

# Set click event
screen.onscreenclick(draw_flag)

# Keep the window open
screen.mainloop()