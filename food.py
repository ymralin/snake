from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.pu()
        # self.shapesize(0.5,0.5)
        self.goto(random.randint(-13, 13) * 20, random.randint(-13, 12) * 20)

    def move_food(self):
        self.goto(random.randint(-13, 13) * 20, random.randint(-13, 12) * 20)
