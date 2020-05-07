from tkinter import *
from tkinter import  PhotoImage
from PIL import ImageTk, Image
from tkinter import  messagebox
import turtle
import math

pencolor=["violet","indigo","blue","green","yellow","orange","red"]
x=0
y=0
s=0
r=0

def here(event):
    print("in here")
    obj.penup()
    obj.setpos(-350+event.x,350-event.y)
    global x
    x=(-350 + event.x)
    print(x)
    global y
    y=(350 - event.y)
    print(y)
    obj.pendown()

def white():
    obj.pencolor("white")

def black():
    obj.pencolor("black")

def violet():
    obj.pencolor(pencolor[0])

def indigo():
    obj.pencolor(pencolor[1])

def blue():
    obj.pencolor(pencolor[2])

def green():
    obj.pencolor(pencolor[3])

def yellow():
    obj.pencolor(pencolor[4])

def orange():
    obj.pencolor(pencolor[5])

def red():
    obj.pencolor(pencolor[6])

def setsize():
    obj.pensize(myslider.get())

def random(x,y):
    obj.ondrag(None)
    obj.setheading(obj.towards(x,y))
    obj.goto(x,y)
    obj.ondrag(random)

def draw_curve():
    drawing_space.bind('<Button-1>', here)
    obj.speed(-1)
    obj.ondrag(random)

def clearscr():
    ans=messagebox.askokcancel("Alert","Are you sure you want to clear all?")
    if(ans):
        obj.clear()

def line():
    drawing_space.bind('<Button-1>', here)
    drawing_space.bind('<Button-3>', drawline)

def drawline(line_event):
    obj.pendown()
    r=-350+line_event.x
    s=350-line_event.y
    obj.setpos(r,s)

def radius(eventt):
    print("in rad")
    a=-350+eventt.x
    b=350-eventt.y
    rad=math.sqrt( (a-x)**2 + (b-y)**2)
    obj.setheading(obj.towards(a,b))
    obj.penup()
    obj.setpos(a,b)
    obj.left(90)
    obj.pendown()
    obj.circle(rad,)

def circle():
    print("in circle")
    drawing_space.bind('<Button-1>',here)
    drawing_space.bind('<Button-3>',radius)

def rec():
    drawing_space.bind('<Button-1>', here)
    drawing_space.bind('<Button-3>', drawrec)

def drawrec(rec_event):
    obj.pendown()
    global r
    global s
    r = -350 + rec_event.x
    s = 350 - rec_event.y
    obj.setpos(r,y)
    obj.setpos(r,s)
    obj.setpos(x,s)
    obj.setpos(x,y)

def draw_sq(sq_event):
    obj.pendown()
    global r
    global s
    r = -350 + sq_event.x
    s = 350 - sq_event.y
    obj.setheading(obj.towards(r,s))
    obj.forward(math.sqrt( (r-x)**2 + (s-y)**2 ))
    for i in range(3):
        obj.right(90)
        obj.forward( math.sqrt( (r-x)**2 + (s-y)**2 ) )

def Square():
    drawing_space.bind('<Button-1>', here)
    drawing_space.bind('<Button-3>', draw_sq)

root=Tk()
root.geometry("900x700")
root.title("Paint by Prabhav")

drawing_space=Canvas(root,width=700,height=700)
drawing_space.pack(side=RIGHT)
#img=PhotoImage(file="pizza.JPG")
img = ImageTk.PhotoImage(Image.open("goa.jpg"))
drawing_space.create_image(200,200,anchor=NE,image=img)
r, g, b = img.getpixel((1, 1))

print(r, g, b)
toolbox_space1=Frame(root,width=300,heigh=200)
toolbox_space1.pack(side=TOP,pady=10)

toolbox_space2=Frame(root,width=200,heigh=200)
toolbox_space2.pack(pady=10)

toolbox_space3=Frame(root,width=200,height=200)
toolbox_space3.pack(pady=10)

l1=Label(toolbox_space1,text="Colors",bg="yellow",fg="red")
l1.pack(fill=X)

c1=Button(toolbox_space1,bg="violet",width=1,command=violet)
c1.pack(side=LEFT,anchor="nw")
c2 = Button(toolbox_space1, bg="indigo",width=1,command=indigo)
c2.pack(side=LEFT,anchor="nw")
c3 = Button(toolbox_space1, bg="blue",width=1,command=blue)
c3.pack(side=LEFT,anchor="nw")
c4 = Button(toolbox_space1, bg="green",width=1,command=green)
c4.pack(side=LEFT,anchor="nw")
c5 = Button(toolbox_space1, bg="yellow",width=1,command=yellow)
c5.pack(side=LEFT,anchor="nw")
c6 = Button(toolbox_space1, bg="orange",width=1,command=orange)
c6.pack(side=LEFT,anchor="nw")
c7 = Button(toolbox_space1, bg="red",width=1,command=red)
c7.pack(side=LEFT,anchor="nw")
c8 = Button(toolbox_space1, bg="white",width=1,command=white)
c8.pack(side=LEFT,anchor="nw")
c9 = Button(toolbox_space1, bg="black",width=1,command=black)
c9.pack(side=LEFT,anchor="nw")

l2=Label(toolbox_space2,text="Pencil-Size",bg="yellow",fg="red")
l2.pack(fill=X)

setsize_button=Button(toolbox_space2,text="Setsize",height=2,command=setsize)
setsize_button.pack(side=RIGHT,anchor="ne",padx=2)

myslider=Scale(toolbox_space2,from_= 1,to = 100,orient=HORIZONTAL,length=120,fg="red",bg="white")
myslider.pack(padx=5)

l3=Label(toolbox_space3,text="Shapes",bg="yellow",fg="red")
l3.pack(fill=X)

s1=Button(toolbox_space3,text="Curve",width=4,command=draw_curve)
s1.pack(side=LEFT,anchor="nw")
s2=Button(toolbox_space3,text="Line",width=4,command=line)
s2.pack(side=LEFT,anchor="nw")
s3=Button(toolbox_space3,text="Square",width=4,command=Square)
s3.pack(side=LEFT,anchor="nw")
s4=Button(toolbox_space3,text="Rect",width=4,command=rec)
s4.pack(side=LEFT,anchor="nw")
s5=Button(toolbox_space3,text="Circle",width=4,command=circle)
s5.pack(side=LEFT,anchor="nw")

clear_button=Button(root,text="clear all",command=clearscr)
clear_button.pack()

obj=turtle.RawTurtle(drawing_space)
obj.pensize(myslider.get())
root.mainloop()