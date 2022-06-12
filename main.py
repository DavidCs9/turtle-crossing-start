import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


game_is_on = True
while game_is_on:
    screen.listen()
    screen.onkey(player.move_up, "Up")
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # detect if player has hit a car
    for car in car_manager.all_Cars:
        if car.distance(player) < 20:
            game_is_on = False
            time.sleep(1)
            answer = screen.textinput("Game Over", "Do you want to play again? (y/n)")
            if answer == "y":
                player.go_to_start()
                car_manager.delete_cars()
                scoreboard.restart()
                game_is_on = True
            else:
                screen.bye()
    # detect if player has hit the finish line
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()
