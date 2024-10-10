import turtle as trtl
import random

CURSOR_SIZE = 20

screen = trtl.Screen()
screen.setup(600, 600)
screen.title("Rendering")
screen.tracer(False)

mapper = trtl.Turtle()
mapper.shape("square")
mapper.hideturtle()
mapper.penup()
mapper.shapesize(stretch_wid=1/CURSOR_SIZE)

mazey = trtl.Turtle()
mazey.hideturtle()
mazey.speed(0)
mazey.pensize(10)

walls = []  # Export this to be used in main.py

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


def make_wall(turtle, distance):
    turtle.forward(distance / 2)
    clone = turtle.clone()
    clone.shapesize(stretch_len=distance / CURSOR_SIZE)
    clone.showturtle()
    turtle.forward(distance / 2)
    walls.append(clone)


def level1():
    make_wall(mapper, 100)
    mapper.left(90)
    make_wall(mapper, 50)
    mapper.left(180)
    make_wall(mapper, 50)
    mapper.right(90)
    make_wall(mapper, 100)
    mapper.right(90)
    make_wall(mapper, 50)


    mapper.left(90)
    mapper.forward(50)


    make_wall(mapper, 50)
    mapper.right(90)
    make_wall(mapper, 50)
    mapper.left(90)
    make_wall(mapper, 50)


    mapper.forward(50)
    mapper.left(90)


    make_wall(mapper, 100)
    mapper.left(90)
    make_wall(mapper, 50)
    mapper.right(90)
    make_wall(mapper, 50)
    mapper.left(90)
    make_wall(mapper, 50)


    mapper.forward(50)
    mazey.right(90)


    make_wall(mapper, 100)
    mapper.right(90)
    make_wall(mapper, 240)
    mapper.right(90)
    make_wall(mapper, 400)
    mapper.right(90)
    make_wall(mapper, 500)
    mapper.right(90)
    make_wall(mapper, 450)


    mapper.forward(50)
    mapper.right(90)


    make_wall(mapper, 500)
    mapper.right(90)
    make_wall(mazey, 100)
    mapper.right(90)
    make_wall(mapper, 100)
    mapper.right(90)
    make_wall(mapper, 50)
    mapper.left(180)
    make_wall(mapper, 50)


    mapper.forward(100)
    mapper.left(90)


    make_wall(mapper, 50)
    mapper.left(180)
    make_wall(mapper, 100)
    mapper.left(180)
    make_wall(mapper, 150)
    mapper.right(180)
    make_wall(mapper, 150)


    mapper.forward(150)
    mapper.right(90)


    make_wall(mapper, 150)
    mapper.right(90)
    make_wall(mapper, 150)
    mapper.left(90)
    make_wall(mapper, 50)


    mapper.right(180)
    mapper.forward(350)
    mapper.left(90)
    mapper.forward(10)
    mapper.right(90)


    make_wall(mapper, 50)
    mapper.right(90)
    make_wall(mapper, 50)
    mapper.left(90)
    make_wall(mapper, 50)
    mapper.right(90)
    make_wall(mapper, 50)

    
    screen.update()  # Update after drawing walls
