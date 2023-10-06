from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")  # background_color
screen.title("My snake game")
# tracer lai off gareko ie. 0 means offf.allows you to trace program execution, generate annotated
screen.tracer(0)
# tracer le animation stop garxa.
# square overlap nahos vanera co-ordinatesmention nagareko

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

segments = []

game_is_on = True
while game_is_on:
    screen.update()  # tracer use gareypaxi update garna is compulsory
    # sabei sqaure move garisakeypaxi arko step ko lagi 0.2 sec. le delay garxa
    time.sleep(0.2)  # snake ko speed
    # tracer lai offgareypaxi black screen matra display hunxa,to bring snake back you
    # you should use update.
    snake.move()

    # snake le foodkhako detect garney.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect collision with wall.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()
    # detect collision with tail.
    for segment in snake.segments:
        if segment == snake.head:
            continue
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
