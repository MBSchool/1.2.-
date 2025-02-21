import turtle as trtl
import random as rand
import mazesetup
import testing as movement

# --- Setting up the screen --- #

wn = trtl.Screen()
wn.setup(600, 600)

# --- Setting up the main turtle --- #

runna = trtl.Turtle()
runna.penup()
runna.color("red")

# --- Setting up the Following turtle --- #

follow = trtl.Turtle()
follow.speed("fastest")
follow.color("red")
follow.penup()
follow.setposition(-250, -250)

# --- Varibles -- #

CURSOR_SIZE = 20
walls = []

# --- Functions --- #

def follow_runner(RUNNER):
    follow.setheading(follow.towards(RUNNER))
    follow.forward(1)
    wn.ontimer(follow_runner, 10)

def collision(turtle):
    tx, ty = turtle.position()


    for wall in walls:


        if wall.distance(turtle) < CURSOR_SIZE / 2:
            wall.color('red')
            return True


        wx, wy = wall.position()
        heading = wall.heading()
        _, stretch_len, _ = wall.shapesize()
        half_length = stretch_len * (CURSOR_SIZE + 1) / 2


        if heading in [0, 180]:  # horizontal wall


            if abs(ty - wy) < CURSOR_SIZE / 2 and abs(tx - wx) < half_length:
                wall.color('red')
                return True


        elif heading in [90, 270]:  # vertical wall


            if abs(tx - wx) < CURSOR_SIZE / 2 and abs(ty - wy) < half_length:
                wall.color('red')
                return True


    return False


# --- Events --- #


'''wn.onkeypress(mazesetup.right,"d")
wn.onkeypress(mazesetup.up,"w")
wn.onkeypress(mazesetup.down,"s")
wn.onkeypress(mazesetup.left,"a")'''


wn.onkeypress(movement.move(runna), "w")
wn.onkeypress(movement.look_right(runna), "d")
wn.onkeypress(movement.look_left(runna), "a")

mazesetup.level1()
follow_runner(runna)

wn.listen()
wn.tracer(True)
wn.title("Maze")
wn.mainloop()
