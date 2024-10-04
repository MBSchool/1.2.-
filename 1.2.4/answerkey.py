##############################################################################
#   a124_TR_maze4_random.py
#   Example solution 4:
#      Code generates a square, and spirals outward as the foundation of a maze.
#      The spiral now has doors/openings at random intervals.
#      The spiral has barrier walls at random intervals.
#      This code ensures walls and doors do not render on top of each other.
################################################################################
import turtle as trtl
import random as rand

# maze configuration variables
num_sides = 15
path_width = 15 
wall_color = "blue"

# config maze
maze_drawer = trtl.Turtle()
maze_drawer.pensize(5)
maze_drawer.pencolor(wall_color)
maze_drawer.speed("fastest")

# draw maze from the middle out
wall_len = path_width
for w in range(num_sides): 
  wall_len += path_width

  if (w > 4): 
    maze_drawer.left(90)

    # randomize location of doors and barriers in wall
    door = rand.randint(path_width*2, (wall_len - path_width*2))
    barrier = rand.randint(path_width*2, (wall_len - path_width*2))
    # if a door and barrier would be rendered on top of each other, get a new value
    while abs(door - barrier) < path_width:
      # a new value for barrier would also work
      door = rand.randint(path_width*2, (wall_len - path_width*2))

    if (door < barrier):
      # draw door first
      maze_drawer.forward(door)
      maze_drawer.penup()
      maze_drawer.forward(path_width*2)
      maze_drawer.pendown()
      # draw barrier, subtracting door lengths already drawn
      maze_drawer.forward(barrier - door - path_width*2)
      maze_drawer.left(90)
      maze_drawer.forward(path_width*2)
      maze_drawer.backward(path_width*2)
      maze_drawer.right(90)
      # draw remaining wall, subtracting barrier lengths already drawn
      maze_drawer.forward(wall_len - barrier)
    else: 
      # draw barrier first
      maze_drawer.forward(barrier)
      maze_drawer.left(90)
      maze_drawer.forward(path_width*2)
      maze_drawer.backward(path_width*2)
      maze_drawer.right(90)        
       # draw door, subtracting barrier lengths already drawn
      maze_drawer.forward(door - barrier)
      maze_drawer.penup()
      maze_drawer.forward(path_width*2)
      maze_drawer.pendown()
      # draw remaining wall, subtracting the door lengths already drawn
      maze_drawer.forward(wall_len - door - path_width*2)

maze_drawer.hideturtle()

wn = trtl.Screen()
wn.mainloop()