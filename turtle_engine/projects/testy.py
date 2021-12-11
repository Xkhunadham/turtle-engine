
from turtle import *

import random as rdm

WN = Screen()
WN.screensize(600, 600)
WN.tracer(0)

hama = Turtle()
hama.color("black")
hama.pencolor("black")
hama.shape("classic")
hama.shapesize(stretch_wid=0.5, stretch_len=0.5)
hama.pu()

dee = []

def adddee(con1=True, con2=False):
    global dee

    deel = Turtle()
    deel.color("purple")
    deel.pencolor("lime")
    deel.shape("classic")
    deel.shapesize(stretch_wid=1.2, stretch_len=1.2)
    deel.speed(0)
    deel.cond1 = con1
    deel.cond2 = con2

    dee.append(deel)

edd = Turtle()
edd.pencolor(WN.bgcolor())
edd.pensize(100)
edd.shape("circle")

for i in range(25):
    adddee()

while True:
    WN.update()
    
    for nl in dee:
        nl.fd(rdm.randint(10, 20))
        nl.rt(rdm.randint(10, 20))
        if rdm.randint(1, 440) == 1:
            adddee()
        if rdm.randint(1, 500) == 1:
            nl.ht()
            dee.pop(dee.index(nl))

    hama.clear()
    hama.write(f"population : {len(dee)}", align='center', font=('Terminal', 24, 'normal'))
    
    hama.spd = 15
    WN.onkeypress(lambda : hama.sety(hama.ycor() + hama.spd), "w")
    WN.onkeypress(lambda : hama.sety(hama.ycor() - hama.spd), "s")
    WN.onkeypress(lambda : hama.setx(hama.xcor() + hama.spd), "d")
    WN.onkeypress(lambda : hama.setx(hama.xcor() - hama.spd), "a")

    edd.ondrag(lambda x, y : edd.goto(x, y))

    edd.pencolor(WN.bgcolor())
    
    WN.listen()







