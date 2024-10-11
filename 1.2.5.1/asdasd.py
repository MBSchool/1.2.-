import turtle

# Set up the screen
screen = turtle.Screen()

# Function to move the tazer turtle forward and check for collision
def move_tazer_and_clear(TAZER, CHASER): # 
    TAZER.forward(1000)  # Move the tazer turtle forward
    print("TAZER SHOT")

    # Check for collision with CLEAR_TURTLE
    if TAZER.distance(CHASER) < 20:  # Check if they are close enough
        CHASER.hideturtle()  # Hide the CLEAR_TURTLE
        TAZER.clear()
        TAZER.hideturtle()
        print("CLEAR TURTLE HIT!")

# Set up a button (using a mouse click)
screen.onclick(lambda x, y: move_tazer_and_clear())

# Keep the window open until closed by the user

