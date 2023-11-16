from turtle import Screen, Turtle

WIDTH = 800
HEIGHT = 600


class CreateScreen(Turtle):

    def __init__(self):
        super().__init__()

        self.screen = Screen()
        self.screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT)
        self.screen.bgcolor("steel blue")
        self.screen.title("Pong Game")

    def dotted_line(self):
        self.hideturtle()
        self.color("black")
        self.pensize(10)
        self.penup()
        self.goto(x=0, y=-420)
        self.setheading(90)

        for num in range(28):
            self.forward(10)
            self.penup()
            self.forward(20)
            self.pendown()

    def game_over(self, winner):
        self.screen.resetscreen()
        self.clear()
        self.color("black")
        self.write("Game Over.\n", move=False, align="center", font=("Ariel", 20, "normal"))
        self.write(f"\n{winner} Wins!", move=False, align="center", font=("Ariel", 20, "normal"))
