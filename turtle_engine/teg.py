from tkinter import *
from tkinter import simpledialog as spd
from tkinter import commondialog as cod
from tkinter import ttk
from tkinter import messagebox as msgb

import os

def runproj():
    os.system(f"python projects/{PROJNAME}.py")

ROOT = Tk()

ROOT.title("turtle engine by @khuDDD")

ROOT.configure(bg="grey12")

tlbl = Label(text="turtle engine by @khuDDD", bg="grey12", fg="white")
tlbl.grid(row=1, column=1)

txtedit = Text(ROOT, width=130, height=40, fg="white", bg="grey10", font=("Consolas", 11, "normal"), insertbackground="white")
txtedit.grid(row=2, column=1)

PROJNAME = spd.askstring("project management", "project name :")

DEFTEXT = \
"""
from turtle import *

WN = Screen()
WN.screensize(600, 600)
WN.tracer(0)
"""

def saveproj():
    with open(f"projects/{PROJNAME}.py", "w") as proj:
        proj.write(txtedit.get("1.0", "end"))

def addsprite(name, col, pcol, shpe, wid, leng):
    txtedit.insert(INSERT,
    f"""
{name} = Turtle()
{name}.color("{col}")
{name}.pencolor("{pcol}")
{name}.shape("{shpe}")
{name}.shapesize(stretch_wid={wid}, stretch_len={leng})
"""
    )
    saveproj()

def adderaser(name, size):
    msgb.showinfo("eraser", f"to use it, just {name}.pd(), {name}.pu() if ur done")
    msgb.showinfo("eraser", f"to change size, just {name}.pensize(size) note, size is whatever u want")
    msgb.showinfo("eraser", f"in your mainloop, plz add {name}.pencolor(WN.bgcolor())")
    txtedit.insert(INSERT,
    f"""
{name} = Turtle()
{name}.pencolor(WN.bgcolor())
{name}.pensize({size})
{name}.ht()
{name}.pu()
"""
    )
    saveproj()

def addmainloop():
    txtedit.insert(END,
    f"""
while True:
    WN.update()

    WN.listen()
"""
    )
    saveproj()

def addupdate():
    txtedit.insert(INSERT,
    "WN.update()"
    )
    saveproj()

def addsplist(name, col, pcol, shpe, wid, leng):
    txtedit.insert(INSERT,
    f"""
{name} = []

def add{name}(con1=True, con2=False):
    global {name}

    {name}l = Turtle()
    {name}l.color("{col}")
    {name}l.pencolor("{pcol}")
    {name}l.shape("{shpe}")
    {name}l.shapesize(stretch_wid={wid}, stretch_len={leng})
    {name}l.cond1 = con1
    {name}l.cond2 = con2

    {name}.append({name}l)
"""
    )
    saveproj()

def addcoli(mode, n1, n2):
    txtadd = ""
    if mode == "sts":
        txtadd = \
        f"""
    if {n1}.distance({n2}) < 20:
        pass
        """
    elif mode == "lts":
        txtadd = \
        f"""
    for nl in {n1}:
        if nl.distance({n2}) < 20:
            pass
        """
    elif mode == "ltl":
        txtadd = \
        f"""
    for nl in {n1}:
        for nm in {n2}:
            if nl.distance(nm) < 20: 
                pass
        """
    txtedit.insert(INSERT,
    txtadd
    )
    saveproj()

def addonclick():
    txtedit.insert(INSERT,
    """WN.onscreenclick(lambda x, y : WN.title(f"{x}, {y}"), btn=1, add=True)"""
    )
    saveproj()

def addondrag(name):
    txtedit.insert(INSERT,
    f"""{name}.ondrag(lambda x, y : {name}.goto(x, y))"""
    )
    saveproj()

def addonspriteclick(name):
    txtedit.insert(INSERT,
    f"""{name}.onclick(lambda x, y : {name}.write("clicked!"))"""
    )
    saveproj()

def addonpress():
    txtedit.insert(INSERT,
    """WN.onkeypress(lambda : WN.title("pressed!"), "space")"""
    )
    saveproj()

def addonkey():
    txtedit.insert(INSERT,
    """WN.onkey(lambda : WN.title("pressed!"), "space")"""
    )
    saveproj()

def addsetwnattrb(bgcolor, tracer, wnwid, wnhigt):
    txtedit.insert(INSERT,
    f"""
    WN.bgcolor("{bgcolor}")
    WN.screensize({wnwid}, {wnhigt})
    WN.tracer({tracer})
    """
    )
    saveproj()

def addpointat(n1, x, y):
    txtedit.insert(INSERT,
    f"""{n1}.setheading({n1}.towards({x}, {y}))"""
    )
    saveproj()

def addwasdctrl(name, speed):
    txtedit.insert(INSERT,
    f"""
    {name}.spd = {speed}
    WN.onkeypress(lambda : {name}.sety({name}.ycor() + {name}.spd), "w")
    WN.onkeypress(lambda : {name}.sety({name}.ycor() - {name}.spd), "s")
    WN.onkeypress(lambda : {name}.setx({name}.xcor() + {name}.spd), "d")
    WN.onkeypress(lambda : {name}.setx({name}.xcor() - {name}.spd), "a")
    """
    )
    saveproj()

def addarrowctrl(name, speed):
    txtedit.insert(INSERT,
    f"""
    {name}.spd = {speed}
    WN.onkeypress(lambda : {name}.sety({name}.ycor() + {name}.spd), "Up")
    WN.onkeypress(lambda : {name}.sety({name}.ycor() - {name}.spd), "Down")
    WN.onkeypress(lambda : {name}.setx({name}.xcor() + {name}.spd), "Right")
    WN.onkeypress(lambda : {name}.setx({name}.xcor() - {name}.spd), "Left")
    """
    )
    saveproj()

def dosomthinginslist(name):
    txtedit.insert(INSERT,
    f"""
for nl in {name}:
    nl.fd(15)
    nl.rt(15)
    """
    )
    saveproj()

def addhpbar(name, max, len, col, bg):
    msgb.showinfo("note", "note : u can also use this for progressbars")
    txtedit.insert(INSERT,
    f"""
{name}.hp = {max}

def {name}hprender(max={max}, len={len}, col="{col}", bg="{bg}"):
    renf = Turtle()
    renf.pu()
    renf.ht()
    nx = {name}.xcor() - len // 2
    ny = {name}.ycor() + 80
    renf.goto(nx, ny)
    renf.pensize(12)
    renf.pencolor(bg)
    renf.pd()
    renf.fd(len)
    renf.pu()
    renf.setx(nx)
    renf.pensize(10)
    renf.pencolor(col)
    wx = ({name}.hp / max) * len
    renf.pd()
    renf.fd(wx)
    renf.pu()
    return renf
"""
    )
    saveproj()

def addloadingskreen(color):
    txtedit.insert(INSERT,
    f"""
couti = Turtle()
couti.shape("turtle")
couti.color("{color}")
couti.pu()
cout = 0
while cout <= 100000:
    cout += 1
    WN.update()
    couti.fd(15)
    couti.rt(15)
couti.ht()
couti = None
"""
    )
    saveproj()

try:
    with open(f"projects/{PROJNAME}.py", "r") as proj:
        txtedit.insert("1.0", proj.read(), "end")
except FileNotFoundError:
    with open(f"projects/{PROJNAME}.py", "w") as proj:
        proj.write(DEFTEXT)
    with open(f"projects/{PROJNAME}.py", "r") as proj:
        txtedit.insert("1.0", proj.read(), "end")

ROOT.title(f"{PROJNAME} - turtle engine")
tlbl.configure(text=f"{PROJNAME} - turtle engine")
ROOT.update()

editcmd = Frame(ROOT, bg="grey11")
editcmd.grid(row=2, column=2, sticky=N)

aspbtn = Button(editcmd, text="add sprite", command=lambda : addsprite(spd.askstring("sprite", "name :"), spd.askstring("sprite", "color :"), spd.askstring("sprite", "pen color :"), spd.askstring("sprite", "shape :"), spd.askfloat("sprite", "width :"), spd.askfloat("sprite", "height :")))
aspbtn.grid(row=0, column=0)

aslbtn = Button(editcmd, text="add sprite list", command=lambda : addsplist(spd.askstring("sprite", "name :"), spd.askstring("sprite", "color :"), spd.askstring("sprite", "pen color :"), spd.askstring("sprite", "shape :"), spd.askfloat("sprite", "width :"), spd.askfloat("sprite", "height :")))
aslbtn.grid(row=1, column=0)

updbtn = Button(editcmd, text="add update at cursor", command=lambda : addupdate())
updbtn.grid(row=2, column=0)

mlpbtn = Button(editcmd, text="add custom mainloop", command=lambda : addmainloop())
mlpbtn.grid(row=3, column=0)

acobtn = Button(editcmd, text="add collision detection", command=lambda : addcoli(spd.askstring("colision", "mode :"), spd.askstring("collision", "object 1 :"), spd.askstring("colision", "object 2 :")))
acobtn.grid(row=4, column=0)

oncbtn = Button(editcmd, text="add onclick", command=lambda : addonclick())
oncbtn.grid(row=5, column=0)

onpbtn = Button(editcmd, text="add onkeypress", command=lambda : addonpress())
onpbtn.grid(row=6, column=0)

onkbtn = Button(editcmd, text="add onkey", command=lambda : addonkey())
onkbtn.grid(row=7, column=0)

ondbtn = Button(editcmd, text="add ondrag", command=lambda : addondrag(spd.askstring("sprite", "name :")))
ondbtn.grid(row=8, column=0)

oscbtn = Button(editcmd, text="add onspriteclick", command=lambda : addonspriteclick(spd.askstring("sprite", "name :")))
oscbtn.grid(row=9, column=0)

wnabtn = Button(editcmd, text="set wn attribute", command=lambda : addsetwnattrb(spd.askstring("window", "bg color :"), spd.askinteger("window", "tracer :"), spd.askinteger("window", "width :"), spd.askinteger("window", "height :")))
wnabtn.grid(row=10, column=0)

patbtn = Button(editcmd, text="point at coord", command=lambda : addpointat(spd.askstring("sprite", "name :"), spd.askinteger("coord", "x :"), spd.askinteger("coord", "y :")))
patbtn.grid(row=11, column=0)

wstbtn = Button(editcmd, text="add wasd control", command=lambda : addwasdctrl(spd.askstring("sprite", "name :"), spd.askinteger("sprite", "speed :")))
wstbtn.grid(row=12, column=0)

wstbtn = Button(editcmd, text="add arrow control", command=lambda : addarrowctrl(spd.askstring("sprite", "name :"), spd.askinteger("sprite", "speed :")))
wstbtn.grid(row=13, column=0)

dslbtn = Button(editcmd, text="do something in sprite list", command=lambda : dosomthinginslist(spd.askstring("sprite", "name :")))
dslbtn.grid(row=14, column=0)

aerbtn = Button(editcmd, text="add eraser", command=lambda : adderaser(spd.askstring("sprite", "name :"), spd.askinteger("eraser", "size :")))
aerbtn.grid(row=15, column=0)

ahpbtn = Button(editcmd, text="add hp", command=lambda : addhpbar(spd.askstring("sprite", "name :"), spd.askinteger("hp", "max :"), spd.askinteger("render hp", "length :"), spd.askstring("bar", "color :"), spd.askstring("bar", "bg :")))
ahpbtn.grid(row=16, column=0)

ldsbtn = Button(editcmd, text="add loading screen", command=lambda : addloadingskreen(spd.askstring("visual design", "color :")))
ldsbtn.grid(row=17, column=0)

ROOT.bind("<Control-s>", lambda event : saveproj())
ROOT.bind("<Control-r>", lambda event : runproj())

ROOT.mainloop()