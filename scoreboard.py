from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, ls, rs):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=200)
        self.write(f"{ls} : {rs}", align='center', font=('arial', 60, 'normal'))

    def score_update(self, ls, rs):
        self.clear()
        self.write(f"{ls} : {rs}", align='center', font=('arial', 60, 'normal'))

    def game_over(self):
        self.color('red')
        self.goto(0, 0)
        self.write(f"GAME OVER", align='center', font=('arial', 60, 'normal'))
