import turtle as trtl
import random


# --- Setting up the screen --- #
screen = trtl.Screen()


# --- Setting up the player --- #
runna = trtl.Turtle()
runna.hideturtle()
runna.penup()
runna.goto(0, 0)
runna.showturtle()
runna.speed(3)
runna.color("blue")


# --- Setting up the maze turtle --- #
mazey = trtl.Turtle()
mazey.hideturtle()
mazey.speed(0)


# --- Maze parameters --- #
walls = 100  # Number of maze walls
width = 50  # Width of the maze paths
wall_positions = []  # List to store wall coordinates


# --- Timer Setup --- #
timer = 45
counter_interval = 1000
timer_up = False
font_setup = ("Arial", 20, "normal")


counter = trtl.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(-400, 400)
counter.pendown()


# --- Functions --- #
def countdown():
    global timer, timer_up
    counter.clear()
    if timer <= 0:
        counter.write("Time's Up", font=font_setup)
        timer_up = True
    else:
        counter.write("Timer: " + str(timer), font=font_setup)
        timer -= 1
        screen.ontimer(countdown, counter_interval)


def draw_maze():
    mazey.penup()
    mazey.goto(-100, 100)
    mazey.pendown()


    for i in range(walls):
        for t in range(i + 1):
            mazey.forward(width)
            store_wall_position(mazey.position())  # Store the wall's position
            if random.randint(0, 5) == 0:  # Randomly place doors
                doors()
            elif random.randint(0, 5) == 1:  # Randomly place blockers
                blocker()
        mazey.right(90)


def store_wall_position(position):
    """Store the coordinates of the wall segment."""
    wall_positions.append(position)


def doors():
    mazey.penup()
    mazey.forward(width)  # Simulate a door by skipping part of the wall
    mazey.pendown()


def blocker():
    mazey.right(90)
    mazey.forward(width)
    store_wall_position(mazey.position())  # Store the blocker's position
    mazey.backward(width)
    mazey.left(90)


# --- Collision Detection --- #
def is_collision(new_x, new_y):
    """Check if the player's new position would collide with a wall."""
    for wall_x, wall_y in wall_positions:
        # Calculate the distance from the player to the wall
        if abs(new_x - wall_x) < width and abs(new_y - wall_y) < width:
            return True
    return False


# Movement controls with collision detection
def right():
    new_x = runna.xcor() + width
    new_y = runna.ycor()
    if not is_collision(new_x, new_y):
        runna.setheading(0)
        runna.forward(width)


def up():
    new_x = runna.xcor()
    new_y = runna.ycor() + width
    if not is_collision(new_x, new_y):
        runna.setheading(90)
        runna.forward(width)


def left():
    new_x = runna.xcor() - width
    new_y = runna.ycor()
    if not is_collision(new_x, new_y):
        runna.setheading(180)
        runna.forward(width)


def down():
    new_x = runna.xcor()
    new_y = runna.ycor() - width
    if not is_collision(new_x, new_y):
        runna.setheading(270)
        runna.forward(width)


# --- Start listening for user input --- #
screen.listen()
