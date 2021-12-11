
from turtle import *

WN = Screen()
WN.screensize(600, 600)
WN.tracer(0)

khunkhung = Turtle()
khunkhung.color("red")
khunkhung.pencolor("blue")
khunkhung.shape("circle")
khunkhung.shapesize(stretch_wid=2, stretch_len=3)

def writename():
    khunkhung.write("khunkhung")
    khunkhung.fd(100)

writename()

while True:
    WN.update()

    khunkhung.ondrag(lambda x, y : khunkhung.goto(x, y))

    WN.onkey(lambda : khunkhung.clear(), "space")

    WN.onkeypress(lambda : writename(), "z")

    WN.onkeypress(lambda : khunkhung.goto(0, 0), "x")
    
    khunkhung.spd = 15
    WN.onkeypress(lambda : khunkhung.sety(khunkhung.ycor() + khunkhung.spd), "Up")
    WN.onkeypress(lambda : khunkhung.sety(khunkhung.ycor() - khunkhung.spd), "Down")
    WN.onkeypress(lambda : khunkhung.setx(khunkhung.xcor() + khunkhung.spd), "Right")
    WN.onkeypress(lambda : khunkhung.setx(khunkhung.xcor() - khunkhung.spd), "Left")
    
    WN.listen()




