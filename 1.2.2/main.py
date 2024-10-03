#   a123_apple_1.py
import turtle as trtl
import random as rand
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
#-----setup-----

# --- Setting up apple --- #

apple = trtl.Turtle()
apple_image = "apple.gif" # Store the file name of your shape
wn.addshape(apple_image)
apple.penup()

# --- Setting Up list --- #

letter_list = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
letter_list_used = []
randletter = rand.choice(letter_list)
currentletter = ""

# --- Setting up drawer --- #

drawer = trtl.Turtle()
drawer.hideturtle()
drawer.penup()

# --- Bgpic -- #

wn.bgpic("background.gif")

#-----functions-----

def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

def move_apple():
 apple.goto(0,-150)
 print("Apple moved to:", apple.ycor())
 reset_apple()
 

def draw_random():
  global randletter
  drawer.color("Black")
  drawer.goto(-20,200)
  drawer.write(f"Press :", {randletter}, font=("Arial", 45, "bold")) 


def reset_apple():
  apple.hideturtle()
  apple.goto(0,0)
  apple.showturtle()
  drawer.clear()
  draw_random()
  used_letter_setter()

def used_letter_setter():
  global randletter
  letter_list_used.append(randletter)
  letter_list.pop(randletter)

#-----function calls-----
  
draw_apple(apple)
draw_random()
print(randletter)
wn.onkeypress(move_apple, randletter)
apple.showturtle()
wn.listen()
wn.mainloop()

