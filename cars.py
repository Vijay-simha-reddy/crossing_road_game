import random
from turtle import Turtle

colors=["red","blue","orange","yellow","green","purple"]
Distance=5

class Cars():
    def __init__(self):
        self.all_cars=[]
        self.speed_car=Distance

    def create_car(self):
        random_chance=random.randint(1,6)
        if random_chance==1 :
            new_car=Turtle("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(colors))
            random_y=random.randint(-250,250)
            new_car.goto(280,random_y)
            self.all_cars.append(new_car)
    def move_car(self):
        for car in self.all_cars:
            car.backward(self.speed_car)

    def level_up(self):
        self.speed_car+=5
        self.move_car()

