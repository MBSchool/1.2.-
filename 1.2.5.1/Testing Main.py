import turtle as trtl
import random as rand
import mazesetup
import testing as movement
import TazerTesting as tazer  # Assuming tazer functionality is in a module named tazer_module

# --- Setting up the screen --- #
wn = trtl.Screen()
wn.setup(600, 600)
wn.title("Maze Runner")
wn.bgpic("image.png")

# --- Setting up the main turtle --- #
runna = trtl.Turtle()
runna.penup()
runna.color("red")
runna.shapesize(19)


# --- Setting up the Following turtle --- #
follow = trtl.Turtle()
follow.speed("fastest")
follow.color("red")
follow.penup()
follow.setposition(-250, -250)

# --- Setting up the Tazer turtle --- #
tazer_trtl = trtl.Turtle()
tazer_trtl.speed("slowest")
tazer_trtl.color("blue")
tazer_trtl.penup()
tazer_trtl.setposition(runna.xcor(), runna.ycor())  # Corrected to use runna's coordinates

# --- Setting up the Target --- #

target = trtl.Turtle()
target.speed(10000000000000000000)
target.color("red")
target.shape("circle")
target.penup()

# --- Variables --- #
CURSOR_SIZE = 20
walls = mazesetup.walls  # Use walls from mazesetup

# --- Functions --- #
def follow_runner():
    follow.setheading(follow.towards(runna))
    follow.forward(1)
    wn.ontimer(follow_runner, 10)

def tazerfollow():
    tazer_trtl.goto(runna.xcor(), runna.ycor())
    wn.ontimer(tazerfollow, 100)

'''def collision(turtle):
    tx, ty = turtle.position()
    for wall in walls:
        if wall.distance(turtle) < CURSOR_SIZE / 2:
            wall.color('red')
            return True

        wx, wy = wall.position()
        heading = wall.heading()
        _, stretch_len, _ = wall.shapesize()
        half_length = stretch_len * (CURSOR_SIZE + 1) / 2

        if heading in [0, 180]:  # Horizontal wall
            if abs(ty - wy) < CURSOR_SIZE / 2 and abs(tx - wx) < half_length:
                wall.color('red')
                return True

        elif heading in [90, 270]:  # Vertical wall
            if abs(tx - wx) < CURSOR_SIZE / 2 and abs(ty - wy) < half_length:
                wall.color('red')
                return True

    return False
'''
# --- Events --- #
wn.onkeypress(lambda: movement.move(runna), "w")
wn.onkeypress(lambda: movement.look_right(runna), "d")
wn.onkeypress(lambda: movement.look_left(runna), "a")

# mazesetup.level1()

follow_runner()
tazerfollow()
tazer.tazer_target(runna, target, tazer_trtl)
# Tazer activation on click
# wn.onclick(lambda x, y: tazer.move_tazer_and_clear(tazer_trtl, follow))

wn.onclick(lambda x, y: tazer.move_tazer_and_clear(tazer_trtl, follow, runna, target))

wn.listen()
wn.tracer(False)
wn.mainloop()
