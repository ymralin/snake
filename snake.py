from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)


STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        # variable that keeps track if snake changed direction in current game tick
        # to make sure the snake can turn only once in given tick
        self.turned = False
        # variable to keep track if snake sped up after last food
        self.sped_up = False

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle()
            new_segment.pu()
            new_segment.goto(position)
            new_segment.color("white")
            new_segment.shape("square")
            self.segments.append(new_segment)

    def move(self):
        for i in reversed(range(len(self.segments))):
            if i == 0:
                self.segments[i].forward(20)
            else:
                self.segments[i].goto(self.segments[i - 1].pos())

    def go_up(self):
        if not self.turned:
            if self.segments[0].heading() != 270:
                self.segments[0].seth(90)
            self.turned = True

    def go_left(self):
        if not self.turned:
            if self.segments[0].heading() != 0:
                self.segments[0].seth(180)
            self.turned = True

    def go_right(self):
        if not self.turned:
            if self.segments[0].heading() != 180:
                self.segments[0].seth(0)
            self.turned = True

    def go_down(self):
        if not self.turned:
            if self.segments[0].heading() != 90:
                self.segments[0].seth(270)
            self.turned = True

    def add_segment(self):
        new_segment = Turtle()
        new_segment.pu()
        new_segment.color("white")
        new_segment.shape("square")
        new_segment.setpos(self.segments[-1].pos())
        self.segments.append(new_segment)
