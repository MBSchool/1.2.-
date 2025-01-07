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

# --- Setting up the drawer --- #
drawer = trtl.Turtle()
drawer.hideturtle()
drawer.penup()

# --- Functions --- #

def draw_apple(active_apple):
    """Draws the apple with the shape and makes it visible."""
    active_apple.shape(apple_image)
    active_apple.showturtle()
    wn.update()

def move_apple():
    """Moves the apple down when the correct key is pressed."""
    apple.goto(apple.xcor(), -150)  # Moving apple straight down
    print(f"Apple moved to: ({apple.xcor()}, {apple.ycor()})")
    reset_apple()

def draw_random():
    """Displays the next letter to press on the screen."""
    global current_letter
    drawer.clear()
    drawer.color("black")
    drawer.goto(-100, 200)
    drawer.write(f"Press: {current_letter}", font=("Arial", 45, "bold"))

def reset_apple():
    """Resets the apple's position and prepares for the next letter."""
    apple.hideturtle()
    randx = rand.randint(-200, 200)  # Adjusted to cover more screen space
    apple.goto(randx, 0)  # Reset apple to new random position at the top
    apple.showturtle()
    set_new_letter()

def set_new_letter():
    """Updates the current letter and binds the corresponding key."""
    global current_letter
    letter_list_used.append(current_letter)
    letter_list.remove(current_letter)
    
    if letter_list:  # Check if there are letters left
        current_letter = rand.choice(letter_list)
        draw_random()
        wn.onkeypress(move_apple, current_letter)
    else:
        drawer.clear()
        drawer.write("You win!", font=("Arial", 45, "bold"))
        wn.onkeypress(None, current_letter)  # Unbinds all key presses

# --- Events --- #

draw_apple(apple)
draw_random()

wn.onkeypress(move_apple, current_letter)  # Initial key binding
wn.listen()
wn.mainloop()

