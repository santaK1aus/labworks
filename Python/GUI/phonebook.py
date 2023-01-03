from tkinter import *
import tkinter
master = Tk()
master.geometry('500x500')
master.title('Test Window')

def bigger():
    master.geometry("1200x1200")

def smaller():
    master.geometry("200x200")

var1 = IntVar()
Checkbutton(master, text='male', variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(master, text='female', variable=var2).grid(row=1, sticky=W)

bBig=tkinter.Button(master,text='Set Big', command=bigger).grid(row=0,column=1,sticky=W)
bBig=tkinter.Button(master,text='Set Small', command=smaller).grid(row=1,column=1,sticky=W)

master.mainloop()