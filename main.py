from turtle import Screen
import time

from padle import Paddles
from ball import Ball
from score import Score


from client import Network





screen = Screen()
screen.setup(800, 500)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


ball = Ball()
my_paddle = Paddles((350, 0))
other_paddle = Paddles((-350, 0))
score=Score()
network=Network()
pos=network.send(my_paddle.pos())




screen.listen()
screen.onkeypress(my_paddle.go_up, "Up")
screen.onkeypress(my_paddle.go_down, "Down")
screen.onkeypress(other_paddle.go_up, "w")
screen.onkeypress(other_paddle.go_down, "s")








game_on = True
while game_on:
    pos=network.send(my_paddle.pos())
    if pos[1]==0:
        # other_paddle.goto(pos[0][0])
        other_paddle.goto(pos[0])
        network.send(my_paddle.pos())
    if pos[1]==1:
        # my_paddle.goto(pos[0][0])
        my_paddle.goto(pos[0])
        network.send(other_paddle.pos())


    time.sleep(0.1)
    ball.move()
    screen.update()     
    
# ball bouncing of upper and lower wall
    if ball.ycor() > 235 or ball.ycor()<-233:
        ball.bounce_wall()
        
#ball bouncing of my_paddle 
    if ball.xcor()>=320:
          if ball.distance(my_paddle) <= 60: 
            ball.bounce_paddle()
        
# ball bouncing of other_paddle
    if ball.xcor()<=-320: 
        if ball.distance(other_paddle) <= 60:
            ball.bounce_paddle()
           
# score counting and restarting game on miss   
    #when right padle misses
    if ball.xcor() >= 340 :
        ball.restart()
        l_score=score.score_l()
        
     #when left padle misses
    if ball.xcor() <= -340 :
        ball.restart()
        r_score= score.score_r()
        # game_on=False
    

screen.exitonclick()
