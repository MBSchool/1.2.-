#Project 1.2.5
import turtle as trtl
import random as rand
import mazesetup


wn = trtl.Screen()

def look_right(RUNNER):
    RUNNER.right(90)


def look_left(RUNNER):
    RUNNER.left(90)


def move(RUNNER):
    wn.onkey(None, "w")


    RUNNER.forward(15)


    if RUNNER.xcor() > 250:
        wn.title("Player wins!")
    else:
        wn.onkey(move, "w")
