#---Imports---#
import turtle as trtl
import hide
import winsound
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)


font_main = ('Arial', 15, 'normal')
font_to_from = ('Impact', 15, 'normal')
text_color = "white"
sound_file = "halloween-244722.wav"


#---Music---#




def play_song():
    winsound.PlaySound(sound_file, winsound.SND_ASYNC)


play_song()




#-- Setitng up "Draw Card" -- #


drawcard = trtl.Turtle()
hide.hide(drawcard)


#-- Setting up text trtl


text = trtl.Turtle()
hide.hide(text)


#-- Setting up "Pumpkin" -- #


pumpkin_img = "halloween_pumpkin.gif"
pumpkin = trtl.Turtle()
hide.hide(pumpkin)
wn.addshape(pumpkin_img)
pumpkin.shape(pumpkin_img) # Setfontss the pumkin as the shape




#---Setting up Ghost---#
ghost_img = "cute_ghost.gif"
ghost = trtl.Turtle()
hide.hide(ghost)
wn.addshape(ghost_img)
ghost.shape(ghost_img)




#---Images---#


wn.bgpic("Capture2.PNG")


#---Draw Card---#


def card():
    pumpkin.penup()
    pumpkin.goto(0,-800)
    ghost.goto(0,-800)
    drawcard.speed("fastest")
    drawcard.pencolor("white")
    drawcard.fillcolor("indigo")
    drawcard.begin_fill()
    drawcard.pensize(4)
    drawcard.hideturtle()
    drawcard.pencolor("orange")
    drawcard.penup()
    drawcard.goto(-150,-200)
    drawcard.pendown()
    drawcard.setheading(90)
    drawcard.forward(450)
    drawcard.setheading(0)
    drawcard.forward(320)
    drawcard.setheading(270)
    drawcard.forward(450)
    drawcard.setheading(180)
    drawcard.forward(320)
    drawcard.end_fill()


#---Pumpkin Movement---#
   
def pumkin_movement():
    hide.hide(pumpkin)
    pumpkin.goto(0,-200)
    pumpkin.showturtle()
    pumpkin.pendown()


    for i in range(4):
        pumpkin.speed(2)
        pumpkin.setheading(0)
        pumpkin.penup()
        pumpkin.forward(100)
        pumpkin.pendown()
        pumpkin.setheading(180)
        pumpkin.penup()
        pumpkin.forward(100)
        pumpkin.pendown()
   
#---Ghost Movement---#
   
def ghost_movement():
    ghost.goto(1000,0)
    ghost.showturtle()
    ghost.speed(4)
    ghost.goto(400,0)
    for angle in range(0, 360, 60):
       ghost.circle(10)




def user_input():
    global from_user, to_user, user_type, user_text


    # Setup
    user_text = ""


    # Write on screen question and answer in terminal
    from_user = wn.textinput("Who is this from?", "Who is this from? ")
    to_user = wn.textinput("Who is this for?", "Who is this to? ")
    user_type = wn.textinput("Premade or Your Own?", "Would you like to enter your own card message or use a premade one. (mine/pre) ")
    if user_type == "mine": # If they type y ask for input draw card
       user_text = wn.textinput("Your Message", "What would you like the card to say?: ")


    elif user_type == "pre": # If they type n set the varible to the premade and draw card
        user_text = f"Happy Halloween, {to_user}!!! \n {from_user} invited you to the Boo Bash at 7:00 PM. \n Only cute costumes allowed!!!\n Bring a spooky snack!"


       
def format_message(message):
    words = message.split()  # Split the message into individual words
    if user_type == "mine" and len(words) > 5:  # Check if the message has more than 5 words
        return ' '.join(words[:5]) + '\n' + ' '.join(words[5:])  # Add a newline after 5 words
    return message  # Return the original message if it's 5 words or less


# Example usage:
message = "This is an example of a personal message that has more than five words."
formatted_message = format_message(message)
print(formatted_message)



def card_text():
    global user_text, to_user, user_text, font_to_from, font_main
    text.color(text_color)


    text.goto(50,-175) # From: TEXT LOCATION
    text.write(f"From: {from_user}", font=font_to_from) # uses f string to use varibles in write


    text.goto(50,-190) # To: TEXT LOCATION
    text.write(f"To: {to_user}", font=font_to_from)


    text.goto(-125, 150) # MAIN TEXT LOCATION
    text.write(user_text, font=font_main)


# -- Call Functions -- #


user_input()
pumkin_movement()
ghost_movement()
card()
format_message(user_text)
card_text()


wn.listen
wn.mainloop()