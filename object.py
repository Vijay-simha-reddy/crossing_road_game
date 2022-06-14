from turtle import Turtle

class Man(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.goto(0 , -280)
        self.setheading(90)

    def go_fd(self):
        new_y=self.ycor()+10
        self.goto(self.xcor(),new_y)

    def restart(self):
        if self.ycor()>=280:
            self.goto(0,-280)
            return True
