import turtle as trtl
import random as rand

# --- Setting up the screen --- #
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
apple_image = "apple.gif"
wn.addshape(apple_image)
wn.bgpic("background.gif")

# --- Initialize apples and letters --- #
apples = []  # List to store the apples (turtles)
letters = ['a', 's', 'd', 'f', 'g']  # Letters to display on apples
apple_positions = [(-200, 200), (-100, 200), (0, 200), (100, 200), (200, 200)]  # Predefined positions for apples

# --- Initialize drawers to display letters on apples --- #
drawers = [trtl.Turtle() for _ in range(5)]
for drawer in drawers:
    drawer.hideturtle()
    drawer.penup()
    drawer.color("white")

# --- Functions --- #

def draw_apples():
    """
    This function draws five apples on the screen at specific positions,
    each apple having a unique letter displayed at its center.
    """
    for i in range(5):
        apples.append(trtl.Turtle())
        apples[i].penup()
        apples[i].shape(apple_image)
        apples[i].goto(apple_positions[i])
        apples[i].showturtle()

        # Display letter on the apple
        drawers[i].goto(apple_positions[i][0] - 15, apple_positions[i][1] - 30)
        drawers[i].write(letters[i], font=("Arial", 30, "bold"))

def drop_apple(letter):
    """
    This function makes the apple corresponding to the typed letter drop
    when the user presses the correct key.
    """
    if letter in letters:  # Check if the pressed letter is in the list of remaining letters
        index = letters.index(letter)
        apples[index].goto(apples[index].xcor(), -150)  # Move apple down
        apples[index].hideturtle()  # Hide apple after it falls
        drawers[index].clear()  # Clear the letter from the screen

        # Remove the letter from the list of available letters
        letters.remove(letter)

        # Check if game is over (no more apples)
        if not letters:
            display_win_message()

def display_win_message():
    """
    This function displays the 'You Win!' message when all apples have fallen.
    """
    win_turtle = trtl.Turtle()
    win_turtle.hideturtle()
    win_turtle.penup()
    win_turtle.color("black")
    win_turtle.goto(0, 0)
    win_turtle.write("You Win!", align="center", font=("Arial", 45, "bold"))

def bind_keys():
    """
    This function binds the letter keys to the corresponding apple drop function.
    """
    for letter in letters:
        wn.onkeypress(lambda l=letter: drop_apple(l), letter)  # Bind each letter to drop its corresponding apple

# --- Main Program Execution --- #
draw_apples()  # Draw the apples on the screen
bind_keys()  # Bind keys for user input

wn.listen()
wn.mainloop()

