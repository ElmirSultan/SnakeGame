from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"Score: {self.score}",align="center",font=("Courier",16,"normal"))
        self.hideturtle()
        self.update()

    def update(self):
        self.write(f"Score: {self.score}",align="center",font=("Courier",16,"normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over",align="center",font=("Courier",16,"normal"))

    def score_calculate(self):
        self.score += 1
        self.clear()
        self.update()
