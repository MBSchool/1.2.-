# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
wn = trtl.Screen()
s = trtl.Turtle()

#-----game configuration----

spot_color = "red"
spot_size = 2
spot_shape = "circle"
spot_speed = 10000

font_setup = ("Arial", 20, "normal")
#---------------
score = 0
score_writer = trtl.Turtle()

#-----initialize turtle-----


s.speed(spot_speed)
s.shape(spot_shape)
s.shapesize(spot_size)
s.fillcolor(spot_color)
s.penup()


score_writer.penup()
score_writer.hideturtle()
score_writer.goto(0, 400)


#-----game functions--------

def change_pos():
    ranxpos = rand.randint(-300, 400 )
    ranypos = rand.randint(-300, 400)
    s.goto(ranxpos, ranypos)

def spot_clicked(x,y):
    change_pos()
    print("The new pos is",x,y)
    update_score()
    score_writer.goto(0, 400)

    
def update_score():
    global score
    score = score + 1
    print(score)
    score_writer.clear()
    score_writer.write(score, font=font_setup)
    

#-----events----------------
    

s.onclick(spot_clicked)










wn.mainloop()