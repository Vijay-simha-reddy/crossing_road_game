from turtle import Turtle

class Levels(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-240,260)
        self.level=1
        with open("store_data.text") as data:
            self.score_level=int(data.read())
        self.write(f"Level-{self.level}", align="center", font=("Courier", 20, "normal"))
        self.update_level()

    def update_level(self):
        self.clear()
        self.goto(-240,260)
        self.write(f"Level-{self.level}", align="center", font=("Courier", 20, "normal"))

    def level_increment(self):
        self.level+=1
        self.score_level=self.level
        with open("store_data.text",mode="w") as data:
            data.write(f"{self.score_level}")
        self.update_level()

    def game_end(self):
        self.goto(0,0)
        self.write("Game_over", align="center", font=("Courier", 20, "normal"))