from tkinter import *;

var = Tk()
var.title("Click ME !")

def leftclick(event):
    tx.delete('1.0','end')
    tx.insert(END, 'Left Click')
    #print("left")

def middleclick(event):
    tx.delete('1.0','end')
    tx.insert(END, 'Middle Click')
    #print("middle")

def rightclick(event):
    tx.delete('1.0','end')
    tx.insert(END, 'Right Click')
    #print("right")

frame = Frame(var, width=300, height=250)

tx=Text(var,height = 1, width = 15, bg = 'light yellow')
tx.pack()

frame.bind("<Button-1>", leftclick)
frame.bind("<Button-2>", middleclick)
frame.bind("<Button-3>", rightclick)
frame.pack()

var.mainloop()