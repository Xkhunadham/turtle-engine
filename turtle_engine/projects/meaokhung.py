
from turtle import *

WN = Screen()
WN.screensize(600, 600)
WN.tracer(0)


khung = Turtle()
khung.color("red")
khung.pencolor("blue")
khung.shape("turtle")
khung.shapesize(stretch_wid=1.3, stretch_len=2.0)


while True:
    WN.update()

    khung.spd = 20
    WN.onkeypress(lambda : khung.sety(khung.ycor() + khung.spd), "Up")
    WN.onkeypress(lambda : khung.sety(khung.ycor() - khung.spd), "Down")
    WN.onkeypress(lambda : khung.setx(khung.xcor() + khung.spd), "Right")
    WN.onkeypress(lambda : khung.setx(khung.xcor() - khung.spd), "Left")

    WN.listen()

