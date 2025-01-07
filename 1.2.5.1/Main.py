import turtle as trtl
import random as rand
import mazesetup
import testing as movement
import asdasd as tazer

# --- Setting up the screen --- #
wn = trtl.Screen()
wn.setup(600, 600)
wn.title("Maze Runner")
wn.bgpic("image.png")
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

tazer_trtl = trtl.Turtle()
tazer_trtl.speed("slowest")
tazer_trtl.color("blue")
tazer_trtl.penup()
tazer_trtl.setposition(runna.ycor, runna.xcor)

# --- Variables -- #
CURSOR_SIZE = 20
walls = mazesetup.walls  # Use walls from mazesetup

# --- Functions --- #
def follow_runner(RUNNER):
    follow.setheading(follow.towards(RUNNER))
    follow.forward(1)
    wn.ontimer(lambda: follow_runner(RUNNER), 10)

def tazerfollow(RUNNER, TAZERTURTLE):
    # Update the heading and position
    TAZERTURTLE.setheading(TAZERTURTLE.towards(RUNNER))
    TAZERTURTLE.goto(RUNNER.xcor(), RUNNER.ycor())
    # Call this function again after a short delay
    wn.ontimer(lambda: tazer(RUNNER, TAZERTURTLE), 100)



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
wn.onkeypress(lambda: movement.move(runna), "w")
wn.onkeypress(lambda: movement.look_right(runna), "d")
wn.onkeypress(lambda: movement.look_left(runna), "a")

mazesetup.level1()
follow_runner(runna)

tazerfollow(runna, tazer_trtl)
wn.onclick(lambda x, y: tazer.move_tazer_and_clear(tazer_trtl, follow))

wn.listen()
wn.tracer(False)
wn.mainloop()
 