import turtle as trtl

# Set up the screen
screen = trtl.Screen()

# "Shooting" the tazer IF HIT: CLear both chaser and tazer
def move_tazer_and_clear(TAZER, CHASER, RUNNER, TARGET):
    TAZER.goto(RUNNER.position())  # Position TAZER on RUNNER
    TAZER.setheading(TAZER.towards(TARGET))  # Set heading towards TARGET

    # Move the TAZER turtle forward
    TAZER.GOTO(TARGET)  
    print("TAZER SHOT")

    # Check for collision with CHASER
    if TAZER.distance(CHASER) < 20:  # Check if they are close enough
        CHASER.hideturtle()  # Hide the CHASER turtle
        TAZER.hideturtle()   # Hide the TAZER turtle
        TAZER.clear()        # Clear the TAZER turtle
        print("CLEAR TURTLE HIT!")


# This is trying to set a clear target for the Tazer to go. Broken?

def tazer_target(RUNNER, TARGET, TAZER):
    runnerY = RUNNER.ycor()
    runnerx = RUNNER.ycor()
    TARGET.goto(runnerx + 5, runnerY + 5)
