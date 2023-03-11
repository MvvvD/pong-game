from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.right = 1
        self.up = 1
        self.r_score = 0
        self.l_score = 0
        self.game_speed = 0.1

    def move(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.up *= -1
        self.goto(self.xcor() + 10 * self.right, self.ycor() + 10 * self.up)

    def reset_pos(self):
        self.game_speed = 0.1
        self.goto(0, 0)
