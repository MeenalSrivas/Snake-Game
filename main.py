from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreborard import Scoreboard

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.bgcolor("black")
game_is_on = True
snake_obj = Snake()
food = Food()
score = Scoreboard()
screen.listen()
screen.onkey(snake_obj.up, "Up")
screen.onkey(snake_obj.down, "Down")
screen.onkey(snake_obj.right, "Right")
screen.onkey(snake_obj.left, "Left")
while game_is_on:
    time.sleep(0.1)
    screen.update()
    snake_obj.move()
    # Detecting collision with food
    if snake_obj.snake_segment[0].distance(food) < 15:
        food.random_location()
        score.writing_score()
        snake_obj.add_segment()
    # detecting collision with a wall
    if snake_obj.snake_segment[0].xcor() > 295 or snake_obj.snake_segment[0].xcor() < -295 or snake_obj.snake_segment[0].ycor() > 295 or snake_obj.snake_segment[0].ycor() < -295:
        game_is_on = False
        score.game_over()

    #detect collision with tail
    new_segments = snake_obj.snake_segment[1:len(snake_obj.snake_segment)]
    for segments in new_segments:
        if snake_obj.head.distance(segments) < 10:
            game_is_on = False
            score.game_over()


screen.exitonclick()
