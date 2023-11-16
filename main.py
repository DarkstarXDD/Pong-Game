from turtle import Screen
from screen import CreateScreen
from player import Player
from ball import Ball
from score import Score
import time

screen = Screen()
screen.tracer(0)

scoreA = Score()
scoreB = Score()

create_screen = CreateScreen()
create_screen.dotted_line()

playerA = Player()
playerB = Player()

playerA.create_player(-450, 0)
playerB.create_player(450, 0)

scoreA.player_score(-100, 300)
scoreB.player_score(100, 300)

screen.listen()

screen.onkeypress(playerA.player_move_up, "w")
screen.onkeypress(playerA.player_move_down, "s")
screen.onkeypress(playerB.player_move_up, "Up")
screen.onkeypress(playerB.player_move_down, "Down")

ball = Ball()
ball.create_ball()
ball.starting_dir()

is_game_on = True

while is_game_on:
    time.sleep(0.01)
    screen.update()
    ball.forward(4)
    if ball.ycor() > 400 or ball.ycor() < -400:
        ball.wall_collision()

    if ball.distance(playerA) < 40 or ball.distance(playerB) < 40:
        ball.player_collision()

    if ball.xcor() > 500:
        scoreA.player_score_update()
        ball.starting_dir()

    if ball.xcor() < -500:
        scoreB.player_score_update()
        ball.starting_dir()

    if scoreA.score_val >= 5:
        winner = "Player A"
        is_game_on = False

    if scoreB.score_val >= 5:
        winner = "Player B"
        is_game_on = False


create_screen.game_over(winner)


create_screen.screen.exitonclick()
