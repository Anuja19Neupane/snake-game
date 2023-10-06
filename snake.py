from turtle import Turtle
STARTING_POSITIONS = [(50, 50), (50, 70), (50, 90)]  # 0,1,2
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        # snake ko head vaneko 0 position ma vako segment ho
        # tuple vanera chinna ko lagi lekheko
        self.head: tuple = self.segments[0]

    def create_snake(self):

        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        # 3 ota square jodera snake jasto banauna khojeko
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head: tuple = self.segments[0]

    def extend(self):
        # add a new segment to snake.
        # in python position -1 means last, -2 means second last
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):  # start,stop,step
            # aba starting ma ie. 3 ota square huda:
            # seg_num: 2 hunxa ani 1 hunxa ani finally 0.
            # yo second last segment ho.
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            # yo last segment ho. last segment lai second last segment ko position ma ja vaneko
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    # segments[0].left(90)
    # 3 ota square sangei vayo so, position 0 ko square lai 20 paces le agadi sarnuparxa for the movement of snake

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
