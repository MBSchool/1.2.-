#Project 1.2.5
from turtle import Screen, Turtle
import leaderboard as lb


import random


font_setup = ("Arial", 20, "normal")
score = 0
CURSOR_SIZE = 20
moving_right = True
gamerunning = False


screen = Screen()
screen.setup(600, 700)
screen.title("Rendering")
screen.tracer(False)


mapper = Turtle()
mapper.shape("square")
mapper.hideturtle()
mapper.penup()
mapper.shapesize(stretch_wid=1/CURSOR_SIZE)


score_writer = Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.color("white")
score_writer.goto(0, 300) # x,y set to fit on smaller screen
score_writer.pendown()


rocket_image = "ufo.gif"
screen.addshape(rocket_image)


user = Turtle()
user.color("blue")
user.shape("triangle")
user.penup()
user.goto(-250, -100)


enemyrocket_image = "enemyufo.gif" # Store the file name of your shape
screen.addshape(enemyrocket_image)
follow = Turtle("turtle")
follow.color("red")
follow.penup()
follow.shape(enemyrocket_image)
follow.setposition(-250, -250)


initial_speed = 1  # Starting speed for the follow turtle
speed_increment = 2  # Speed increase every 10 seconds
follow_speed = initial_speed
follow.speed(follow_speed)  # Set initial speed




rocket_right_image = "rocket_right.gif" # Store the file name of your shape
screen.addshape(rocket_right_image)
rocket_left_image = "rocket_left.gif" # Store the file name of your shape
screen.addshape(rocket_left_image)
minion1 = Turtle("turtle")
minion1.speed("fast")
minion1.penup()
minion1.shape(rocket_right_image)
minion1.setposition(-150, -200)




leaderboard_file_name = "a122_leaderboard.txt"
player_name = input("Please enter your name:")


walls = []


#wall collision taken from stack overflow user, cdlane, in their explanation on how to make wall collisions


def increase_follow_speed():
    global follow_speed
    follow_speed += speed_increment
    follow.speed(follow_speed)
    print(follow_speed)
    # Call this function again after 10 seconds
    screen.ontimer(increase_follow_speed, 10000)


def k3():
    user.right(90)


def k2():
    user.left(90)


def k1():
    screen.onkey(None, "w")


    user.forward(15)


    if user.xcor() > 275:
        screen.title("Player wins!")
    elif collision(user):
        screen.title("Collision!")
    else:
        screen.onkey(k1, "w")


def make_wall(turtle, distance):
    turtle.forward(distance / 2)
    clone = turtle.clone()
    clone.color("white")
    clone.shapesize(stretch_len=distance/CURSOR_SIZE)
    clone.showturtle()
    turtle.forward(distance / 2)


    walls.append(clone)


def collision(turtle):
    tx, ty = turtle.position()


    if minion1.distance(turtle) < CURSOR_SIZE / 2:
        update_score()  # Increase score on collision with minion1
        minion1.goto(random.randint(-6,5)*50, random.randint(-5,5)*50)


    if follow.distance(turtle) < CURSOR_SIZE / 2:
        clearer()


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
                clearer()
                return True


        elif heading in [90, 270]:  # vertical wall


            if abs(tx - wx) < CURSOR_SIZE / 2 and abs(ty - wy) < half_length:
                wall.color('red')
                clearer()
                return True


    return False


def level3():
    screen.bgpic("Galaxylvl2.gif")
    mapper.goto(-275,-275)
    make_wall(mapper, 550)
    mapper.left(90)
    make_wall(mapper, 425)
    mapper.forward(125)    
    mapper.left(90)
    make_wall(mapper, 550)
    mapper.left(90)
    make_wall(mapper, 550)


    #starting the vertical rows
#1
    mapper.left(90)
    mapper.forward(50)
    mapper.left(90)
    mapper.forward(50)
    make_wall(mapper, 150)
    mapper.forward(100)
    make_wall(mapper, 150)
    mapper.forward(50)
    make_wall(mapper, 50)
#2
    mapper.right(90)
    mapper.forward(50)
    mapper.right(90)
    mapper.forward(50)
    make_wall(mapper, 50)
    mapper.forward(50)
    make_wall(mapper,50)
    mapper.forward(100)
    make_wall(mapper, 50)
    mapper.forward(100)
    make_wall(mapper, 100)
#3
    mapper.left(90)
    mapper.forward(50)
    mapper.left(90)
    mapper.forward(100)
    make_wall(mapper, 50)
    mapper.forward(100)
    make_wall(mapper, 50)
    mapper.forward(200)
    make_wall(mapper, 50)
#4
    mapper.right(90)
    mapper.forward(50)
    mapper.right(90)
    mapper.forward(200)
    make_wall(mapper, 50)
    mapper.forward(100)
    make_wall(mapper, 100)
    mapper.forward(50)
    make_wall(mapper, 50)
#5
    mapper.left(90)
    mapper.forward(50)
    mapper.left(90)
    make_wall(mapper, 50)
    mapper.forward(200)
    make_wall(mapper, 200)
    mapper.forward(50)
    make_wall(mapper, 50)
#6
    mapper.right(90)
    mapper.forward(50)
    mapper.right(90)
    mapper.forward(100)
    make_wall(mapper, 50)
    mapper.forward(50)
    make_wall(mapper, 150)
    mapper.forward(50)
    make_wall(mapper, 50)
    mapper.forward(100)
#7
    mapper.left(90)
    mapper.forward(50)
    mapper.left(90)
    mapper.forward(100)
    make_wall(mapper, 100)
    mapper.forward(50)
    make_wall(mapper, 50)
    mapper.forward(50)
    make_wall(mapper, 100)
    mapper.forward(50)
    make_wall(mapper, 50)
#8
    mapper.right(90)
    mapper.forward(50)
    mapper.right(90)
    make_wall(mapper, 50)
    mapper.forward(250)
    make_wall(mapper, 50)
    mapper.forward(50)
    make_wall(mapper, 50)
    mapper.forward(50)
    make_wall(mapper, 50)
#9
    mapper.left(90)
    mapper.forward(50)
    mapper.left(90)
    mapper.forward(150)
    make_wall(mapper, 50)
    mapper.forward(100)
    make_wall(mapper, 50)
    mapper.forward(50)
    make_wall(mapper, 100)
    mapper.forward(50)
#10
    mapper.right(90)
    mapper.forward(50)
    mapper.right(90)
    mapper.forward(50)
    make_wall(mapper, 50)
    mapper.forward(150)
    make_wall(mapper, 100)
    mapper.forward(50)
    make_wall(mapper, 50)
    mapper.forward(100)
#11
    mapper.left(90)
    mapper.forward(50)
    mapper.left(90)
    mapper.forward(50)
    make_wall(mapper, 50)
    mapper.forward(150)
    make_wall(mapper, 100)
    mapper.forward(150)
    make_wall(mapper, 50)
#12
    mapper.right(90)
    mapper.forward(50)
    mapper.right(90)
    make_wall(mapper, 350)
    mapper.forward(50)
    make_wall(mapper, 50)
    mapper.forward(50)
    make_wall(mapper, 50)


    #starting the horizontal rows
   
    mapper.left(180)
    mapper.forward(50)
#1
    mapper.left(90)
    mapper.forward(150)
    make_wall(mapper, 150)
    mapper.forward(100)
    make_wall(mapper, 50)
    mapper.forward(150)
#2
    mapper.right(90)
    mapper.forward(50)
    mapper.right(90)
    mapper.forward(150)
    make_wall(mapper, 100)
    mapper.forward(50)
    make_wall(mapper, 50)
    mapper.forward(100)
    make_wall(mapper, 100)
#3    
    mapper.left(90)
    mapper.forward(50)
    mapper.left(90)
    mapper.forward(150)
    make_wall(mapper, 50)
    mapper.forward(200)
    make_wall(mapper, 50)
    mapper.forward(100)
#4
    mapper.right(90)
    mapper.forward(50)
    mapper.right(90)
    mapper.forward(50)
    make_wall(mapper, 50)
    mapper.forward(50)
    make_wall(mapper, 50)
    mapper.forward(50)
    make_wall(mapper, 100)
    mapper.forward(100)
    make_wall(mapper, 50)
    mapper.forward(50)
#5
    mapper.left(90)
    mapper.forward(50)
    mapper.left(90)
    mapper.forward(100)
    make_wall(mapper, 100)
    mapper.forward(150)
    make_wall(mapper, 150)
    mapper.forward(50)
#6
    mapper.right(90)
    mapper.forward(50)
    mapper.right(90)
    mapper.forward(100)
    make_wall(mapper, 50)
    mapper.forward(100)
    make_wall(mapper, 100)
    mapper.forward(100)
    make_wall(mapper, 50)
    mapper.forward(50)
#7
    mapper.left(90)
    mapper.forward(50)
    mapper.left(90)
    mapper.forward(50)
    make_wall(mapper, 150)
    mapper.forward(150)
    make_wall(mapper, 100)
    mapper.forward(50)
    make_wall(mapper, 50)
#8
    mapper.right(90)
    mapper.forward(50)
    mapper.right(90)
    mapper.forward(50)
    make_wall(mapper, 150)
    mapper.forward(100)
    make_wall(mapper, 50)
    mapper.forward(100)
    make_wall(mapper, 100)
#9
    mapper.left(90)
    mapper.forward(50)
    mapper.left(90)
    mapper.forward(100)
    make_wall(mapper, 100)
    mapper.forward(150)
    make_wall(mapper, 100)
    mapper.forward(100)
#10
    mapper.right(90)
    mapper.forward(50)
    mapper.right(90)
    mapper.forward(50)
    make_wall(mapper, 50)
    mapper.forward(50)
    make_wall(mapper, 50)
    mapper.forward(100)
    make_wall(mapper, 50)
    mapper.forward(100)
    make_wall(mapper, 50)
    mapper.forward(50)
    global gamerunning
    gamerunning == True


def manage_leaderboard():


  global score
  global user


  # get the names and scores from the leaderboard file
  leader_names_list = lb.get_names(leaderboard_file_name)
  leader_scores_list = lb.get_scores(leaderboard_file_name)


  # show the leaderboard with or without the current player
  if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(True, leader_names_list, leader_scores_list, user, score)


  else:
    lb.draw_leaderboard(False, leader_names_list, leader_scores_list, user, score)


def update_score():
  global score
  score = score + 1
  score_writer.clear()
  score_writer.write(score, font=font_setup)




def clearer():
    screen.clear()
    manage_leaderboard()


def stop_game():
    global gamerunning
    gamerunning = False


def follow_runner():
    follow.setheading(follow.towards(user))
    follow.forward(1)
    screen.ontimer(follow_runner, 10)


level3()
screen.title("Maze")
screen.onkey(k1, "w")
screen.onkey(k2, "a")
screen.onkey(k3, "d")
screen.onkey(clearer, "p")


follow_runner()
increase_follow_speed()


screen.listen()
screen.tracer(True)
screen.mainloop()



































LEADERBOARD
# set the levels of scoring
bronze_score = 3
silver_score = 5
gold_score = 7


# return names in the leaderboard file
def get_names(file_name):
  leaderboard_file = open(file_name, "r")  # be sure you have created this


  # use a for loop to iterate through the content of the file, one line at a time
  # note that each line in the file has the format "leader_name,leader_score" for example "Pat,50"
  names = []
  for line in leaderboard_file:
    leader_name = ""
    index = 0


    # TODO 1: use a while loop to read the leader name from the line (format is "leader_name,leader_score")
    while (line[index] != ","):
      leader_name = leader_name + line[index]
      index = index + 1
     
    # TODO 2: add the player name to the names list
    names.append(leader_name)
  print("names:", names)


  leaderboard_file.close()


  #  TODO 6: return the names list in place of the empty list
  return names


 
# return scores from the leaderboard file
def get_scores(file_name):
  leaderboard_file = open(file_name, "r")  # be sure you have created this


  scores = []
  for line in leaderboard_file:
    leader_score = ""    
    index = 0


    # TODO 3: use a while loop to index beyond the comma, skipping the player's name
    while (line[index] != ","):
      index = index + 1
    index = index + 1


    # TODO 4: use a while loop to get the score
    while (line[index] != "\n"):
      leader_score = leader_score + line[index]
      index = index + 1


    # TODO 5: add the player score to the scores list
    scores.append(int(leader_score))
  print("scores:", scores)
   
  leaderboard_file.close()


  # TODO 7: return the scores in place of the empty list
  return scores




# update leaderboard by inserting the current player and score to the list at the correct position
def update_leaderboard(file_name, leader_names, leader_scores,  player_name, player_score):


  '''UPDATED'''
  # TODO 8: loop through all the scores in the existing leaderboard list
  for index in range(len(leader_scores)):
    # TODO 9: check if this is the position to insert new score at
    if (player_score >= leader_scores[index]):
      break
    else:
      index = index + 1


  # TODO 10: insert new player and score
  leader_names.insert(index, player_name)
  leader_scores.insert(index, player_score)
  # TODO 11: keep both lists at 5 elements only (top 5 players)
  if(len(leader_scores)>5):
    leader_scores.pop(5)
    leader_names.pop(5)
  # TODO 12: store the latest leaderboard back in the file
 
 
  leaderboard_file = open(file_name, "w")  # this mode opens the file and erases its contents for a fresh start
 
  # TODO 13 loop through all the leaderboard elements and write them to the the file
  for index in range(len(leader_scores))  :
    leaderboard_file.write(leader_names[index] + "," + str(leader_scores[index]) + "\n")


  leaderboard_file.close()
   
 


# draw leaderboard and display a message to player
def draw_leaderboard(high_scorer, leader_names, leader_scores, turtle_object, player_score):
 
  # clear the screen and move turtle object to (-200, 100) to start drawing the leaderboard
  font_setup = ("Arial", 20, "normal")
  turtle_object.clear()
  turtle_object.penup()
  turtle_object.goto(-160,100)
  turtle_object.hideturtle()
  turtle_object.down()


  # loop through the lists and use the same index to display the corresponding name and score, separated by a tab space '\t'
  for index in range(len(leader_names)):
    turtle_object.write(str(index + 1) + "\t" + leader_names[index] + "\t" + str(leader_scores[index]), font=font_setup)
    turtle_object.penup()
    turtle_object.goto(-160,int(turtle_object.ycor())-50)
    turtle_object.down()
 
  # move turtle to a new line
  turtle_object.penup()
  turtle_object.goto(-160,int(turtle_object.ycor())-50)
  turtle_object.pendown()


  # TODO 14: display message about player making/not making leaderboard
  if high_scorer:
    turtle_object.write("Congratulations!\nYou made the leaderboard!", font=font_setup)
  else:
    turtle_object.write("Sorry!\nYou didn't make the leaderboard.\nMaybe next time!", font=font_setup)
 


  # move turtle to a new line
  turtle_object.penup()
  turtle_object.goto(-160,int(turtle_object.ycor())-50)
  turtle_object.pendown()
 
  # TODO 15: Display a gold/silver/bronze message if player earned a gold/silver/or bronze medal; display nothing if no medal
  if player_score < bronze_score:
    turtle_object.write("You suck!", font=font_setup)
  elif player_score < silver_score:
    turtle_object.write("You earned a bronze medal!", font=font_setup)
  elif player_score < gold_score:
    turtle_object.write("You earned a silver medal!", font=font_setup)
  elif player_score >= gold_score:
    turtle_object.write("You earned a gold medal!", font=font_setup)
 


