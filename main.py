import random
import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor('gray')
player = Player()
screen.listen()
screen.onkey(player.move_up, "Up")
car_manager = CarManager()
cars_list = []
scoreboard = Scoreboard()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if player.is_reached_top():
        scoreboard.level_up()
        print(scoreboard.current_level)
        car_manager.speed_up()



    if random.randint(0,100) < 30:
        car_manager.create_cars()

    car_manager.move_cars()




