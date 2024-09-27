# a121_catch_a_turtle.py
#-----import statements-----

import turtle as trtl
import random as rand
import leaderboard as lb
#-----Adding Turtles-----

wn = trtl.Screen()
s = trtl.Turtle()
counter =  trtl.Turtle()
score_writer = trtl.Turtle()

# Leader board
leaderboard_file_name = "a122_leaderboard.txt"
player_name = input ("Please enter your name: ")

#-----game configuration----

spot_color = "red"
spot_size = 2
spot_shape = "circle"
spot_speed = 10000

font_setup = ("Arial", 20, "normal")
score = 0

timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = "false"

#-----initialize turtle-----

s.speed(spot_speed)
s.shape(spot_shape)
s.shapesize(spot_size)
s.fillcolor(spot_color)
s.penup()

score_writer.penup()
score_writer.hideturtle()
score_writer.goto(0, 400)


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
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 
    
# Add this function to your game code

# manages the leaderboard for top 5 scorers
def manage_leaderboard():

  global score
  global s

  # get the names and scores from the leaderboard file
  leader_names_list = lb.get_names(leaderboard_file_name)
  leader_scores_list = lb.get_scores(leaderboard_file_name)

  # show the leaderboard with or without the current player
  if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(True, leader_names_list, leader_scores_list, s, score)

  else:
    lb.draw_leaderboard(False, leader_names_list, leader_scores_list, s, score)
#-----events----------------
    

s.onclick(spot_clicked)
countdown()


wn.mainloop()