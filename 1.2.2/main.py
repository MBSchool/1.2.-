#   a123_apple_1.py
import turtle as trtl
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
#-----setup-----

# --- Setting up apple --- #
apple = trtl.Turtle()
apple_image = "apple.gif" # Store the file name of your shape
wn.addshape(apple_image)
apple.penup()
apple.setheading(270)

# --- Setting up drawer --- #

drawer = trtl.Turtle()
drawer.hideturtle()
drawer.penup()

# --- Bgpic -- #
wn.bgpic("background.gif")

#-----functions-----

# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

def move_apple():
 draw_A()
 apple.goto(0,-150)
 drawer.goto(0.-150)
 print("Apple moved to:", apple.ycor())
 

def draw_A():
  drawer.color("white")
  drawer.goto(-19,-40)
  drawer.write("A", font=("Arial", 45, "bold")) 




#-----function calls-----
draw_apple(apple)
wn.onkeypress(move_apple, "a")
wn.listen()
wn.mainloop()

