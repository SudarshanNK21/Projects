from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(position)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=('Courier', 20, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()


class HighScore(Turtle):

    def __init__(self, position, name):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(position)
        self.hideturtle()
        self.name = name
        self.high_score()
        self.final_score = 0
        self.high_score_player = ''

    def high_score(self):
        self.score += 1
        self.clear()
        with open("high_score_file.txt", 'r') as f:
            f.seek(0)
            l = f.readlines()
            print(l)
            high_score = l[0]
            self.final_score = high_score
            h_name = l[1]
            self.high_score_player = h_name

        if int(self.score) >= int(high_score[0]):
            with open("high_score_file.txt", 'w') as f:
                self.high_score_player = self.name
                f.seek(0)
                f.write(f'{self.score}\n')
                # f.write('\n')
                f.write(f'{self.high_score_player}')

                self.final_score = self.score
                self.final_score -= 1

        self.write(f"High Score by {self.high_score_player} : {high_score[0]}", align='center',
                   font=('Courier', 10, 'normal'))

    def reduce(self):
        # with open("high_score_file.txt", 'r') as f:
        #     high_score = int(f.read())

        with open("high_score_file.txt", 'w') as f:
            f.seek(0)
            f.write(f'{self.final_score}\n')
            # f.write('\n')
            f.write(f'{self.high_score_player}')
