from turtle import Turtle


FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.update_score()

    def update_score(self):
        self.hideturtle()
        self.clear()
        self.penup()
        self.goto(-290, 260)
        self.write(f"Level:{self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_score()

    def restart(self):
        self.level = 1
        self.update_score()
