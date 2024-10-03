#   a123_apple_1.py
import turtle as trtl
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
#-----setup-----
apple = trtl.Turtle()
apple_image = "apple.gif" # Store the file name of your shape

wn.addshape(apple_image)

wn.bgpic("background.gif")

apple.penup()
apple.setheading(270)

#-----functions-----

# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

def move_apple():
 apple.goto(0,-150)
 print("Apple moved to:", apple.ycor())


#-----function calls-----
draw_apple(apple)
wn.onkeypress(move_apple, "a")
wn.listen()
wn.mainloop()

