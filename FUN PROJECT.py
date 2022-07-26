from tkinter import *
from random import *

name=Tk()
name.title("HI")
name.geometry("1600x800")

def no():
    X=randint(100,600)
    Y=randint(100,600)
    button2.place(x=X,y=Y)

def yes():
    fool=Tk()
    fool.title("you are fooled")
    fool.geometry("1600x800")

    label2=Label(fool,text="I KNOW THAT !!!",fg="white",bg="black",font=("arailblack",30))
    label2.place(x=500,y=250)
    fool.mainloop()

label=Label(name,text="Are you an Idiot???",fg="white",bg="black",width=20,height=2,font=("arailblack",30),bd=20).pack()

button1=Button(name,text="yes",fg='WHITE',bg="blue",width=5,font=("arailblack",10),command=yes)
button1.place(x=500,y=200)
button2=Button(name,text="no",fg="white",bg="blue",width=5,font=("arailblack",10),command=no)
button2.place(x=800,y=200)

name.mainloop()