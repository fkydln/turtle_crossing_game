import time
import turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.setheading(180)
        self.color(random.choice(COLORS))
        self.shapesize(1, 3)

class CarManager():
    def __init__(self):
        self.cars_list = []
        self.current_speed = 5

    def create_cars(self):
        super().__init__()
        for _ in range(1):
            car = Car()
            car.goto(300, random.randint(-240, 280))
            self.cars_list.append(car)

    def move_cars(self):
        for car in self.cars_list:
            car.forward(self.current_speed)

    def speed_up(self):
        self.current_speed += 10

