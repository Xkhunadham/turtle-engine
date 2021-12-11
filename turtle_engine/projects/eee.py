
from turtle import *
import time as tm

WN = Screen()
WN.screensize(600, 600)
WN.tracer(0)

couti = Turtle()
couti.shape("turtle")
couti.color("green")
couti.pu()
cout = 0
while cout <= 200:
    cout += 1
    WN.update()
    couti.fd(15)
    couti.rt(15)
    tm.sleep(0.05)
couti.ht()
couti = None

ahamham = []

def addahamham(con1=True, con2=False):
    global ahamham

    ahamhaml = Turtle()
    ahamhaml.color("lime")
    ahamhaml.pencolor("white")
    ahamhaml.shape("circle")
    ahamhaml.shapesize(stretch_wid=1.5, stretch_len=1.5)
    ahamhaml.pu()
    ahamhaml.cond1 = con1
    ahamhaml.cond2 = con2

    ahamham.append(ahamhaml)

littlt = []

def addlittlt(con1=True, con2=False):
    global littlt

    littltl = Turtle()
    littltl.color("blue")
    littltl.pencolor("red")
    littltl.shape("arrow")
    littltl.shapesize(stretch_wid=2.0, stretch_len=2.0)
    littltl.pu()
    littltl.cond1 = con1
    littltl.cond2 = con2

    littlt.append(littltl)

yertle = Turtle()
yertle.color("red")
yertle.pencolor("red")
yertle.shape("turtle")
yertle.shapesize(stretch_wid=1.0, stretch_len=1.0)

yertle.hp = 200

def yertlehprender(max=200, len=120, col="red", bg="white"):
    renf = Turtle()
    renf.pu()
    renf.ht()
    nx = yertle.xcor() - len // 2
    ny = yertle.ycor() + 80
    renf.goto(nx, ny)
    renf.pensize(12)
    renf.pencolor(bg)
    renf.pd()
    renf.fd(len)
    renf.pu()
    renf.setx(nx)
    renf.pensize(10)
    renf.pencolor(col)
    wx = (yertle.hp / max) * len
    renf.pd()
    renf.fd(wx)
    renf.pu()
    return renf

import random as rdm

addlittlt()
addlittlt()
addlittlt()

addahamham()
addahamham()
addahamham()

WN.update()

rended = False

while True:
    WN.update()
    
    if rended:
        rend.clear()

    for nl in littlt:
        nl.fd(25)
        nl.rt(15)
    
    for nl in ahamham:
        nl.fd(35)
        nl.rt(15)
    
    for nl in littlt:
        if nl.distance(yertle) < 20:
            yertle.shapesize(stretch_wid=rdm.randrange(1, 5), stretch_len=1)
            yertle.hp += -10

    for nl in ahamham:
        if nl.distance(yertle) < 20:
            yertle.hp += 10
        
    for nl in littlt:
        for nm in ahamham:
            if nl.distance(nm) < 20: 
                nl.setheading(nl.towards(nm.xcor(), nm.ycor()))

    yertle.ondrag(lambda x, y : yertle.goto(x, y))
    yertle.onclick(lambda x, y : yertle.write("clicked!"))

    WN.onscreenclick(lambda x, y : yertle.setheading(yertle.towards(x, y)), btn=1, add=True)
    
    WN.onkey(lambda : yertle.clear(), "space")
    
    yertle.spd = 20
    WN.onkeypress(lambda : yertle.sety(yertle.ycor() + yertle.spd), "w")
    WN.onkeypress(lambda : yertle.sety(yertle.ycor() - yertle.spd), "s")
    WN.onkeypress(lambda : yertle.setx(yertle.xcor() + yertle.spd), "d")
    WN.onkeypress(lambda : yertle.setx(yertle.xcor() - yertle.spd), "a")
    
    WN.onscreenclick(lambda x, y : yertle.goto(x, y), btn=2, add=True)
    
    rend = yertlehprender()

    rended = True

    WN.bgcolor(rdm.choice(["black", "grey2"]))
    
    WN.listen()








