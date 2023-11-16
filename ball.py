from turtle import Turtle
import random

BALL_SIZE = 1.2
BALL_SPEED = 1


class Ball(Turtle):

    def __init__(self):
        super().__init__()

    def create_ball(self):
        self.shape("circle")
        self.shapesize(stretch_wid=BALL_SIZE, stretch_len=BALL_SIZE)
        self.color("aquamarine")

    def starting_dir(self):
        self.goto(0, 0)
        directions = [0, 180]
        rand_dir = random.choice(directions)
        self.setheading(rand_dir)

        rand_angle = random.randint(-75, 75)
        self.left(rand_angle)
        self.penup()
        self.speed(BALL_SPEED)

    def wall_collision(self):
        old_angle = self.heading()
        new_angle = 360 - old_angle
        self.setheading(new_angle)

    def player_collision(self):
        old_angle = self.heading()
        new_angle = 180 - old_angle
        self.setheading(new_angle)
