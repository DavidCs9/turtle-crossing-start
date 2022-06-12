from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.all_Cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        r = random.randint(1, 6)
        if r == 1:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            random_y = random.randint(-230, 250)
            new_car.goto(300, random_y)
            self.all_Cars.append(new_car)

    def move_cars(self):
        for car in self.all_Cars:
            car.backward(self.speed)

    def level_up(self):
        self.speed += MOVE_INCREMENT

    def delete_cars(self):
        for car in self.all_Cars:
            car.hideturtle()

        self.all_Cars = []

        self.speed = STARTING_MOVE_DISTANCE
