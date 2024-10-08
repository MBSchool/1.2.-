import turtle as trtl
import random as rand
import Stolencode as mazesetup
import time
# --- Setting up the screen --- #

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)

# --- Setting up the main turtle --- #
main = trtl.Turtle()
main.penup()
main.hideturtle()


start_button = trtl.Turtle()
start_button.showturtle()
start_button.penup()
start_button.goto(0,0)
start_button.shapesize(20)
start_button.color("red")
start_button.shape("circle")


# --- Varibles -- #

start_true = False

# --- Functions --- #

def start():
    global start_button
    global start_ture
if start_true == True:
    mazesetup.draw_maze()


def start_clicked():
    global start_true
    start_true = True
    start()




# --- Events --- #


wn.onclick(start_clicked(start_button), start_button)

wn.onkeypress(mazesetup.right,"d")
wn.onkeypress(mazesetup.up,"w")
wn.onkeypress(mazesetup.down,"s")
wn.onkeypress(mazesetup.left,"a")



wn.listen()

