import turtle as trtl
import random as rand
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)


number_list = []

randnum = rand.randint(1,4)
number_list.append(randnum)

print(randnum)

# Note the usage of the keyword "in" below.
if (4 in number_list):
  temp_turtle = trtl.Turtle()
  temp_turtle.write("4 in list.", font=("Arial", 74, "bold"))
else: 
  temp_turtle = trtl.Turtle()
  temp_turtle.write("4 not in list.", font=("Arial", 74, "bold"))
  

trtl.mainloop()