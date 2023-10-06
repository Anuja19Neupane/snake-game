from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("day_20,21/data.txt") as data:
            self.high_score = int(data.read())
        self.goto(0, 265)
        self.color("white")
        self.penup()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()  # Clear the previous score display
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("day_20,21/data.txt", mode="w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

