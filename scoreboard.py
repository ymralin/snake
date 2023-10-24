from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.score = 0
        self.goto(0, 260)
        self.color("white")
        self.write(f"SCORE: {self.score}", False, align="center", font=("Arial", 16, "bold"))
        self.ht()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align="center", font=("Arial", 24, "bold"))
        self.goto(0, -30)
        self.write("Press ENTER to restart", False, align="center", font=("Arial", 16, "bold"))

    def update_score(self):
        self.clear()
        self.goto(0, 260)
        self.write(f"SCORE: {self.score}", False, align="center", font=("Arial", 16, "bold"))

    def reset_score(self):
        self.clear()
        self.goto(0, 260)
        self.write("SCORE: 0", False, align="center", font=("Arial", 16, "bold"))
