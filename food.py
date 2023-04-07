from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.speed("fastest")
        self.up()
        self.shapesize(0.5, 0.5)
        self.random_location()

    def random_location(self):
        x = randint(-260, 260)
        y = randint(-260, 260)
        self.goto(x, y)
