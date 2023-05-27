from turtle import Turtle,Screen
from food import Food
from scoreboard import Scoreboard
import time
screen = Screen()
food = Food()
scoreboard = Scoreboard()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
starting_positions = [(0,0), (-20,0), (-40,0)]
move_distance = 20
segments = []
up = 90
down = 270
left = 180
right = 0

class Snake:
    def __init__(self):
        self.segments  = []
        self.create_snake()
        self.head = self.segments[0]
    def create_snake(self):
        for position in starting_positions:
            self.add_segment(position)
    def add_segment(self,position):
        my_turtle = Turtle(shape="square")
        my_turtle.color("white")
        my_turtle.penup()
        my_turtle.goto(position)
        self.segments.append(my_turtle)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            x_cor = self.segments[seg_num -1].xcor()
            y_cor = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(x_cor,y_cor)
        self.segments[0].forward(move_distance)
    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)
    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)
    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)
    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)

snake = Snake()
screen.listen()
screen.onkey(snake.up ,"Up")
screen.onkey(snake.down ,"Down")
screen.onkey(snake.left ,"Left")
screen.onkey(snake.right ,"Right")
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.score_calculate()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()



screen.exitonclick()