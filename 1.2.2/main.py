#   a123_apple_1.py
import turtle as trtl
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
#-----setup-----
apple = trtl.Turtle()
apple_image = "apple.gif" # Store the file name of your shape
apple_pressed = "false"

wn.addshape(apple_image)

wn.bgpic("background.gif")

apple.penup()
apple.setheading(270)

#-----functions-----

# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

def apple_called():
  global apple_pressed
  apple_pressed = "true"
  print("Apple called")
  move_apple()

def move_apple():
 apple.forward(1)


#-----function calls-----
draw_apple(apple)

wn.onkeypress(move_apple, "a")

wn.listen()
wn.mainloop()

