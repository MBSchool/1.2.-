#a124_maze_spiral
import turtle as trtl
import random




screen = trtl.Screen()


runna=trtl.Turtle()
runna.hideturtle()
runna.penup()
runna.goto(0,0)
runna.showturtle()
runna.speed=(3)
runna.color("blue")


mazey = trtl.Turtle()
mazey.hideturtle()
mazey.speed(100000000000000)


walls = 45
width = 10


timer = 45
counter_interval = 1000
timer_up = False
font_setup = ("Arial", 20, "normal")


counter =  trtl.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(-400, 400) # x,y set to fit on smaller screen
counter.pendown()
#counter.showturtle()


#-----game functions-----


# countdown function
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True


  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)




def draw_maze():
  for i in range(walls):
    for t in range(i):
     if i <= 4:
      mazey.penup()
     else:
      print(t)
      if t == random.randint(1,t+1):
          doors()
      if t == random.randint(4,t+4):
          blocker()
      else:
          mazey.forward(width)
          mazey.pendown()
    mazey.right(90)


def doors():
  mazey.penup()


def blocker():
  mazey.right(90)
  mazey.forward(2*width)
  mazey.backward(2*width)
  mazey.left(90)
  mazey.forward(width)


def right():
  runna.setheading(0)
  runna.forward(width)


def up():
  runna.setheading(90)
  runna.forward(width)


def left():
  runna.setheading(180)
  runna.forward(width)


def down():
  runna.setheading(270)
  runna.forward(width//2)









screen.listen()


screen.mainloop()