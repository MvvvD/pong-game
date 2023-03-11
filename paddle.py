from turtle import Turtle

POSITION = {'l': (-350, 0), 'r': (350, 0)}


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color('white')
        self.goto(x=POSITION[pos][0], y=POSITION[pos][1])

    def go_up(self):
        self.goto(x=self.xcor(), y=(self.ycor() + 20))

    def go_down(self):
        self.goto(x=self.xcor(), y=(self.ycor() - 20))
