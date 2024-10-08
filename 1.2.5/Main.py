import turtle as trtl
import random as rand
import Stolencode as mazesetup
# --- Setting up the screen --- #

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)

# --- Setting up the main turtle --- #
main = trtl.Turtle()
main.penup()

# --- Functions --- #






# --- Events --- #

mazesetup.draw_maze()
#countdown()
wn.onkeypress(mazesetup.right,"d")
wn.onkeypress(mazesetup.up,"w")
wn.onkeypress(mazesetup.down,"s")
wn.onkeypress(mazesetup.left,"a")
