from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.writing_score()

    def writing_score(self):
        self.clear()
        x = "Score" + " "+str(self.score)
        self.write(x, align="center",font=("Arial", 12, "normal"))
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center",font=("Arial", 20, "normal"))

