from turtle import Turtle

PLAYER_MOVE_AMOUNT = 75


class Player(Turtle):
    def __init__(self):
        super().__init__()

    def create_player(self, start_pos_x, start_pos_y):
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.speed(2)
        self.penup()
        self.goto(x=start_pos_x, y=start_pos_y)

    def player_move_up(self):
        new_y = self.ycor() + PLAYER_MOVE_AMOUNT
        self.goto(self.xcor(), new_y)

    def player_move_down(self):
        new_y = self.ycor() - PLAYER_MOVE_AMOUNT
        self.goto(self.xcor(), new_y)
