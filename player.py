import turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280



class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def is_reached_top(self):
        if self.distance(0, FINISH_LINE_Y) < 10:
            self.reset_position()
            return True

    def reset_position(self):
        self.goto(STARTING_POSITION)

