import turtle
from time import sleep
# the screen
screen = turtle.Screen()
screen.setup(750, 500)

turtle.bgcolor("black")

# creating the pong ball
ball = turtle.Turtle()
ball.penup()
ball.color("white")
ball.shape("turtle")
velocity_x = 5
velocity_y = 5
def ball_movement():
    ball.setpos((ball.pos()[0]+velocity_x, ball.pos()[1]+velocity_y))

# creating the paddles
class Paddle:
    def __init__(self, right):
        self.right = right
        self.pad = turtle.Turtle()
        self.pad.penup()
        if right == True: self.pad.setpos((300, 0))
        if right == False: self.pad.setpos((-300, 0))
        self.pad.right(90)
        self.pad.shape("square")
        self.pad.shapesize(stretch_len=5, stretch_wid=1)
        self.pad.color("white")
    def move_up(self):
        self.pad.back(20)

    def move_down(self):
        self.pad.forward(20)
    def get_ycor(self):
        return self.pad.ycor()

p_right = Paddle(True)
p_left = Paddle(False)
GAME = True

screen.listen()
while GAME:
    # adding a spin to the ball
    ball.right(5)
    ball_movement()

    # input right paddle
    screen.onkey(p_right.move_up, "Up")
    screen.onkey(p_right.move_down, "Down")

    # input right paddle
    screen.onkey(p_left.move_up, "w")
    screen.onkey(p_left.move_down, "s")

    # barriers
    if ball.pos()[1] <= -225: velocity_y = -velocity_y
    if ball.pos()[1] >= 225: velocity_y = -velocity_y

    # ball bounce from paddles
    if (ball.xcor() > 280  and ball.xcor() < 300) and (ball.ycor() < p_right.get_ycor() + 50 and ball.ycor() > p_right.get_ycor() - 50): velocity_x = -velocity_x
    if (ball.xcor() < -280  and ball.xcor() > -300) and (ball.ycor() < p_left.get_ycor() + 50 and ball.ycor() > p_left.get_ycor() - 50): velocity_x = -velocity_x
    # lose and win statement
    if ball.pos()[0] >= 375: GAME = False
    if ball.pos()[0] <= -375: GAME = False
    screen.update()