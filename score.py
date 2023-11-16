from turtle import Turtle

SCORE_SIZE = 50


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_val = 0

    def player_score(self, pos_x, pos_y):
        self.penup()
        self.hideturtle()
        self.goto(pos_x, pos_y)
        self.write(self.score_val, move=False, align="center", font=("Ariel", SCORE_SIZE, "normal"))

    def player_score_update(self):
        self.score_val += 1
        self.clear()
        self.write(self.score_val, move=False, align="center", font=("Ariel", SCORE_SIZE, "normal"))
