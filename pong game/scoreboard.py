from turtle import Turtle


class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color('white')
        self.penup()
        self.position = position
        self.goto(position)
        self.hideturtle()
        self.total_score_1 = 0
        self.total_score_2 = 0
        self.winner = ''
        # self.write(self.total_score_1, align='center', font=('Courier',40,'normal'))
        # self.write(self.total_score_2, align='center', font=('Courier', 40, 'normal'))
        self.write(self.winner, align='center', font=('Courier', 80, 'normal'))

    def score_increase_1(self):
        self.total_score_1 += 1
        self.clear()
        self.write(self.total_score_1, align='center', font=('Courier', 40, 'normal'))

    def score_increase_2(self):
        self.total_score_2 += 1
        self.clear()
        self.write(self.total_score_2, align='center', font=('Courier', 40, 'normal'))

    def game_over_1(self):
        self.clear()
        self.winner = "player 1 won"
        self.write(self.winner, align='center', font=('Courier', 40, 'normal'))

    def game_over_2(self):
        self.clear()
        self.winner = "player 2 won"
        self.write(self.winner, align='center', font=('Courier', 80, 'normal'))


