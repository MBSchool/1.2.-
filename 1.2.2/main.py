import turtle as trtl
import random as rand

# --- Setting up the screen --- #
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
apple_image = "apple.gif"
wn.addshape(apple_image)
wn.bgpic("background.gif")

# --- Setting up the apple --- #
apple = trtl.Turtle()
apple.penup()

# --- Setting up letters --- #
letter_list = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
letter_list_used = []
current_letter = rand.choice(letter_list)
randx = rand.randint(-20, 50)

# --- Setting up the drawer --- #
drawer = trtl.Turtle()
drawer.hideturtle()
drawer.penup()

# --- Functions --- #

def draw_apple(active_apple):
    active_apple.shape(apple_image)
    active_apple.showturtle()
    wn.update()

def move_apple():
    apple.goto(randx, -150)
    print("Apple moved to:", apple.ycor(), apple.xcor())
    reset_apple()

def draw_random():
    global current_letter
    drawer.clear()
    drawer.color("black")
    drawer.goto(-100, 200)
    drawer.write(f"Press: {current_letter}", font=("Arial", 45, "bold"))

def reset_apple():
    apple.hideturtle()
    apple.goto(randx, 0)
    apple.showturtle()
    set_new_letter()

def set_new_letter():
    global current_letter
    letter_list_used.append(current_letter)
    letter_list.remove(current_letter)  # Correct removal by value
    if letter_list:  # Check if there are letters left
        current_letter = rand.choice(letter_list)
        draw_random()
        wn.onkeypress(move_apple, current_letter)
    else:
        drawer.clear()
        drawer.write("You win!", font=("Arial", 45, "bold"))

# --- Events --- #

draw_apple(apple)
draw_random()

wn.onkeypress(move_apple, current_letter)  # Initial key binding
wn.listen()
wn.mainloop()

