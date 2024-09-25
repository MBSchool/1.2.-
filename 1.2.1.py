# a121_catch_a_turtle.py
#-----import statements-----

import turtle as trtl
import random as rand

#-----Adding Turtles-----

wn = trtl.Screen()
s = trtl.Turtle()
counter =  trtl.Turtle()
score_writer = trtl.Turtle()

#-----game configuration----

spot_color = "red"
spot_size = 2
spot_shape = "circle"
spot_speed = 10000

font_setup = ("Arial", 20, "normal")
score = 0

#-----initialize turtle-----


s.speed(spot_speed)
s.shape(spot_shape)
s.shapesize(spot_size)
s.fillcolor(spot_color)
s.penup()

score_writer.penup()
score_writer.hideturtle()
score_writer.goto(0, 400)

timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = "false"

counter.hideturtle()
counter.penup()
counter.goto(-300, 400)


#-----game functions--------

def change_pos():
    ranxpos = rand.randint(-300, 400)
    ranypos = rand.randint(-300, 400)
    s.goto(ranxpos, ranypos)


def update_score():
    global score
    score = score + 1
    print(score)
    score_writer.clear()
    score_writer.write(score, font=font_setup)

def spot_clicked(x,y):
    global timer_up, timer
    change_pos()
    update_score()
    score_writer.goto(0, 400)
    if timer_up == "true":
      s.hideturtle()

def countdown():
  global timer, timer_up
  counter.clear()
  counter.hideturtle()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = "true"
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 
    

#-----events----------------
    

s.onclick(spot_clicked)
countdown()


wn.mainloop()