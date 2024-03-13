import turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.current_level = 0
        self.penup()
        self.hideturtle()
        self.draw_scoreboard()

    def level_up(self):
        self.current_level += 1

    def draw_scoreboard(self):
        self.goto(-250, 250)
        self.write(f"Level: {self.current_level  + 1}", align="center", font=("Arial", 24, 'normal'))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.current_level + 1}", align="center", font=("Arial", 24, 'normal'))

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("Game Over!!", align="center", font=("Arial", 24, 'normal'))
        self.goto(0,-50)
        self.write(f"Score: {self.current_level + 1}", align="center", font=("Arial", 24, 'normal'))
