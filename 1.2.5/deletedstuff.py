def right(RUNNER):
  RUNNER.setheading(0)
  RUNNER.forward(width)


def up(RUNNER):
  RUNNER.setheading(90)
  RUNNER.forward(width)


def left(RUNNER):
  RUNNER.setheading(180)
  RUNNER.forward(width)


def down(RUNNER):
  RUNNER.setheading(270)
  RUNNER.forward(width//2)



follow = trtl.Turtle()
follow.speed("fastest")
follow.color("red")
follow.penup()
follow.setposition(-250, -250)


def follow_runner():
    follow.setheading(follow.towards(runna))
    follow.forward(1)
    screen.ontimer(follow_runner, 10)