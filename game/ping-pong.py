#building asimple logic based python game using turtle
#1 main thing is the game loop and game loop is all about the updating the window (play window)
#2.creating Game Objects - any game has the objects to work upon thus this point will allow building them
#3.Functions- to give movement to the objects created we require functions like to move the paddle we will 
#  define a function move
#4 Moving the ball bounce off the paddle as well
#5 Collide with the paddles and bounce back 
#6 Scoring

import turtle    #used to build the background and various other elements to be drawn

import winsound

win = turtle.Screen()
win.title("Ping-pong ball game")
win.bgcolor("black")
win.setup(width=800,height=600)
win.tracer(0)


#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350,0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350,0)



#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.shapesize(stretch_len=1,stretch_wid=1)
ball.penup()
ball.goto(0,0)
ball.dx = 1             #everytime our ball moves it moves by 2 pixel
ball.dy = -1

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A : 0 Player B : 0",align="center", font=("courier",24,"normal"))

#score
score_a = 0
score_b = 0


#Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# def screen_corner():
#     if(paddle_a_up.y>=win.height):
#         y -=20
#key:Listeners
win.listen()
win.onkeypress(paddle_a_up,"w")
win.onkeypress(paddle_a_down,"s")
win.onkeypress(paddle_b_up,"Up")
win.onkeypress(paddle_b_down,"Down")


#Main game loop
while True:
    win.update() 


    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border Checking
    if(ball.ycor() > 290):
        ball.sety(290)
        ball.dy = -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

    if(ball.ycor() < -290):
        ball.sety(-290)
        ball.dy  *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

    if(ball.xcor() > 390):
        ball.goto(0,0)
        ball.dx = -1
        score_a += 1
        pen.clear()
        pen.write("Player A : {} Player B : {}".format(score_a,score_b),align="center", font=("courier",24,"normal"))


    if(ball.xcor() < -390):
        ball.goto(0,0)
        ball.dx  *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A : {} Player B : {}".format(score_a,score_b),align="center", font=("courier",24,"normal"))


    #paddle collision
    if (ball.xcor()>340 and ball.xcor()<350 and (ball.ycor()<paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 50)):
        ball.setx(340)
        ball.dx *= -1 

    if (ball.xcor()<-340 and ball.xcor()>-350 and (ball.ycor()<paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 40)):
        ball.setx(-340)
        ball.dx *= -1 