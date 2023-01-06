# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 19:02:20 2023

@author: ISHITA KAR
"""

from tkinter import *

from tkinter import messagebox
import tkinter.ttk as ttk

root=Tk()
root.title("Data Entry")
root.configure(bg='grey')
root.geometry("1000x1000")

#define style
style=ttk.Style(root)
style.theme_use("default")


#show warning
def popup():
    messagebox.showwarning("Warning","please tick the checkbox")
def click():
    if(var2.get()==0):
        popup()
    else:
        return

#submit window

def open():
    top=Toplevel()
    top.geometry("1000x1000")
    top.title("form submission")
    style=ttk.Style(top)
    style.theme_use("clam")

    
    #Personal details
    l0=ttk.Label(top,text="PERSONAL DETAILS",font=('Times', 16))
    l0.grid(row=0,column=0,padx=20,pady=20)
    l1=ttk.Label(top,text="NAME")
    l10=ttk.Label(top,text="MOBILE NUMBER")
    l10.grid(row=2,column=0,padx=10,pady=10)
    e7=ttk.Entry(top,width=30)
    e7.grid(row=2,column=1,columnspan=100)
    l2=ttk.Label(top,text="ADDRESS(LINE 1)")
    
    l2.grid(row=5,column=0,padx=10,pady=10)
    e=ttk.Entry(top,width=30)
    e1=ttk.Entry(top,width=30)
    l1.grid(row=1,column=0,padx=10,pady=10)
    e.grid(row=1,column=1,columnspan=100)
    e1.grid(row=5,column=1,columnspan=100)
    l3=ttk.Label(top,text="ADDRESS(LINE 2)")
    l3.grid(row=8,column=0,padx=10,pady=10)
    e2=ttk.Entry(top,width=30)
    e2.grid(row=8,column=1,columnspan=100)
    l11=ttk.Label(top,text="STATE")
    l11.grid(row=10,column=0,padx=10,pady=10)
    l13=ttk.Label(top,text="DATE OF BIRTH")
    l13.grid(row=3,column=0,padx=10,pady=10)
    e10=ttk.Entry(top,width=30)
    e10.grid(row=3,column=1,columnspan=100)
    e10.insert(0,"DD/MM/YYYY")
    #dropdown boxes
    var=StringVar()
    drop=ttk.OptionMenu(top,var,"West Bengal","Bihar","Jharkhand")
    drop.grid(row=10,column=1)
    
    
    l4=ttk.Label(top,text="GUARDIAN'S NAME")
    l4.grid(row=11,column=0,padx=10,pady=10)
    e3=ttk.Entry(top,width=30)
    e3.grid(row=11,column=1,columnspan=100)
    l5=ttk.Label(top,text="EMAIL ID")
    l5.grid(row=12,column=0,padx=10,pady=10)
    e4=ttk.Entry(top,width=30)
    e4.grid(row=12,column=1,columnspan=100)
    
    #academic details
    l6=ttk.Label(top,text="ACADEMIC DETAILS",font=('Times', 16))
    l6.grid(row=13,column=0,padx=20,pady=20)
    l7=ttk.Label(top,text="NAME OF COLLEGE")
    l7.grid(row=14,column=0,padx=10,pady=10)
    e5=ttk.Entry(top,width=30)
    e5.grid(row=14,column=1,columnspan=100)
    l8=ttk.Label(top,text="DEPARTMENT")
    l8.grid(row=16,column=0,padx=10,pady=10)
    e6=ttk.Entry(top,width=30)
    e6.grid(row=16,column=1,columnspan=100)
    l9=ttk.Label(top,text="YEAR")
    l9.grid(row=17,column=0,padx=10,pady=10)
    l8=ttk.Label(top,text="COURSE NAME")
    l8.grid(row=15,column=0,padx=10,pady=10)
    e6=ttk.Entry(top,width=30)
    e6.grid(row=15,column=1,columnspan=100)
    
    #dropdown boxes
    var1=StringVar()
    drop=ttk.OptionMenu(top,var1,'1st',"1st","2nd","3rd","4th")
    drop.grid(row=17,column=1)
    
    #checkbox
    global var2
    var2=IntVar()
    c=ttk.Checkbutton(top,text="All the informations furnished above are correct",variable=var2)
    c.grid(row=19,column=0)
    
    
    #submit button
    button_sub=ttk.Button(top,text="SUBMIT",command=click)
    button_sub.grid(row=20,column=1,padx=10,pady=10)
        
        
        
        
# height=3       


#main window
l=ttk.Label(root,text="FORM FILLING UP", font=('Times', 20))
button_1=ttk.Button(root,text="SUBMIT NEW ",width=13,command=open)
button_2=ttk.Button(root,text="VIEW DATA",width=13)
button_1.place(x=200,y=200)
button_2.place(x=500,y=200)
l.pack(padx=200)



root.mainloop()