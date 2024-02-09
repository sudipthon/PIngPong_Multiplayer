from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.l=0
        self.r=0
        self.update_score()
    def update_score(self):
        self.goto(-200,225)
        self.write(arg=f"{self.l}",align="center",font=("Arial","15","normal"))
        
        self.goto(200,225)
        self.write(arg=f"{self.r}",align="center",font=("Arial","15","normal"))
    def score_l(self):
        self.l+=1
        self.clear()
        self.update_score() 
           
    def score_r(self):
        self.r+=1
        self.clear()
        self.update_score()