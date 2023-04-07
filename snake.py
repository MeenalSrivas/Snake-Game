from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        x = 0
        self.snake_segment = []
        for i in range(3):
            obj = Turtle()
            obj.shape("square")
            obj.color("white")
            obj.up()
            obj.goto(x, 0)
            x -= 20
            self.snake_segment.append(obj)
        self.head = self.snake_segment[0]

    def add_segment(self):
        obj = Turtle()
        obj.shape("square")
        obj.color("white")
        obj.up()
        obj.goto(self.snake_segment[len(self.snake_segment)-1].xcor(),self.snake_segment[len(self.snake_segment)-1].ycor())
        self.snake_segment.append(obj)


    def move(self):
        for seg_num in range(len(self.snake_segment) - 1, 0, -1):
            xcor = self.snake_segment[seg_num - 1].xcor()
            ycor = self.snake_segment[seg_num - 1].ycor()
            self.snake_segment[seg_num].goto(xcor, ycor)
        self.snake_segment[0].forward(MOVE_DISTANCE)

    def down(self):
        if self.snake_segment[0].heading() != UP:
            self.snake_segment[0].setheading(DOWN)

    def up(self):
        if self.snake_segment[0].heading() != DOWN:
            self.snake_segment[0].setheading(UP)

    def right(self):
        if self.snake_segment[0].heading() != RIGHT:
            self.snake_segment[0].setheading(RIGHT)

    def left(self):
        if self.snake_segment[0].heading() != LEFT:
            self.snake_segment[0].setheading(LEFT)


