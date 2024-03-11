FONT = ("Courier", 24, "normal")


class Scoreboard():
    def __init__(self):
        self.current_level = 0

    def level_up(self):
        self.current_level += 1
