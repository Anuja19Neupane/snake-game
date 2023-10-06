from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()  # multiple  inheritance ma yo use garna parxa, super() returns a delegate object to a parent class
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # circle ko lagi
        self.color("blue")
        self.speed("fastest")
        self.refresh

    def refresh(self):
        random_x = random.randint(-280, 280)
        # circle ko lagi co-ordinates deko
        # (-300,300) dida circle dekhidaina so aafei  (-280,280) leko.
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
