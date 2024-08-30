from turtle import Turtle
ALIGNMENT = "center"
FONT = "Aerial", 24, "normal"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,300)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"score = {self.score}", align=ALIGNMENT, font=FONT)

    def increaase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("gameover",align=ALIGNMENT, font=FONT)
