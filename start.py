import time
from turtle import Screen
from object import Man
from cars import Cars
from levels import Levels
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Pong Game")
screen.tracer(0)

man = Man()
car = Cars()
levels=Levels()
screen.listen()
screen.onkey(man.go_fd, "Up")
game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_car()
    if man.restart():
        car.level_up()
        levels.level_increment()

    for i in car.all_cars:
        if man.distance(i) < 18:
            levels.game_end()
            game_on = False

screen.exitonclick()