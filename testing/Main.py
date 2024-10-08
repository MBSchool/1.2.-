import turtle as trtl
import random as rand
import stolencode as mazesetup
import time


# --- Setting up the screen --- #
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)


# --- Setting up the main turtle --- #

main = trtl.Turtle()
main.penup()
main.hideturtle()

# --- Setting up the start button --- #

start_button = trtl.Turtle()
start_button.penup()
start_button.goto(0, 0)
start_button.shapesize(5)
start_button.color("red")
start_button.shape("circle")

# --- Variables --- #
start_true = False


# --- Functions --- #

def start():
    global start_button, start_true
    if start_true:
        start_button.hideturtle()  # Hide the start button after clicking
        mazesetup.draw_maze()  # Call the function to start drawing the maze


def start_clicked(x, y):
    global start_true
    start_true = True
    start()

# --- Events --- #
start_button.onclick(start_clicked)  # Set up event handler for clicking the button
wn.onkeypress(mazesetup.right, "d")
wn.onkeypress(mazesetup.up, "w")
wn.onkeypress(mazesetup.down, "s")
wn.onkeypress(mazesetup.left, "a")


wn.listen()
wn.mainloop()




