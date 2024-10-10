import turtle as trtl
import mazesetup


wn = trtl.Screen()


def look_right(RUNNER):
    RUNNER.setheading(RUNNER.heading() - 90)  # Corrected usage of heading()


def look_left(RUNNER):
    RUNNER.setheading(RUNNER.heading() + 90)  # Corrected usage of heading()


def move(RUNNER):
    wn.onkey(lambda: move(RUNNER), "w")
    RUNNER.forward(15)
    

