import tkinter as tk
from tkinter import ttk
import time
import math

MainWindow = tk.Tk()
MainWindow.title("Scientific Calculator")
MainWindow.geometry("220x303")

MainFrame=tk.Frame(MainWindow)
MainWindow.resizable(width=False,height=False)
maintext= ttk.Entry(MainFrame,width=18,font=('Arial',16,'bold'),justify='right')
maintext.grid(row=0,column=0,columnspan=5,sticky='W',padx=0,ipady=5)
maintext.insert(0,'0')

bHeight=11
bWidth=4
bPadX=0
bPadY=0

bStyle=ttk.Style()
bStyle.theme_use('default')
numStyle=ttk.Style()
opStyle=ttk.Style()
scStyle=ttk.Style()
bStyle.configure('base.TButton',font=('Arial',16),borderwidth=0,focusthickness=3,focuscolor='none')
numStyle.configure('num.base.TButton',background="#FFFFFF",foreground='#25265E')
scStyle.configure('sc.base.TButton',background="#f9851f",foreground='#FFFFFF')
scStyle.map('sc.base.TButton',background=[('active','#f99c2d')])

class Ops:
    def __init__(self):
        self.preCalc=0.0
        self.postCalc=0.0
        self.lOps=''
        self.preEqOp=''
        self.pressOp=False
    
    def concat(self,x):
        if maintext.get()=='0' or self.pressOp:
            maintext.delete(0,len(maintext.get()))
            maintext.insert(0,x)
            self.pressOp=False
            return
        maintext.insert(len(maintext.get()),x)
    
    def clear(self):
        maintext.delete(0,len(maintext.get()))
        maintext.insert(0,'0')
        self.preCalc=0
        self.postCalc=0
        self.pressOp=False
        self.lOps=''

    def delete(self):
        maintext.delete(len(maintext.get())-1)
        if(len(maintext.get())<1):
            maintext.insert(0,'0')
    
    def getData(self):
        data=maintext.get()
        try:
            self.preCalc=self.postCalc
            self.postCalc=float(data)
        except ValueError:
            maintext.delete(0,len(maintext.get()))
            maintext.insert(0,'Error')
            #time.sleep(3)
            #maintext.delete(0,5)
            #maintext.insert(0,'0')
    
    def doPrevious(self,now=0):
        preOp=self.lOps if now==0 else self.preEqOp
        dictf={'add':self.add,'sub':self.sub,'mult':self.mult,'div':self.div,'mod':self.mod,'pow':self.power}
        if(not len(preOp)>0):
            return
        if dictf[preOp](now=1) == True:
            self.display(self.preCalc)
    
    def display(self,x):
        maintext.delete(0,len(maintext.get()))
        maintext.insert(0,str(x))

    def mod(self,now=0):
        if(now==1):
            self.preCalc=self.preCalc/100*self.postCalc
            return True
        self.pressOp=True
        self.getData()
        self.doPrevious()
        self.lOps='mod'

    def add(self,now=0):
        if(now==1):
            self.preCalc=self.preCalc+self.postCalc
            return True
        self.pressOp=True
        self.getData()
        self.doPrevious()
        self.lOps='add'

    def sub(self,now=0):
        if(now==1):
            self.preCalc=self.preCalc-self.postCalc
            return True
        self.pressOp=True
        self.getData()
        self.doPrevious()
        self.lOps='sub'

    def mult(self,now=0):
        if(now==1):
            self.preCalc=self.preCalc*self.postCalc
            return True
        self.pressOp=True
        self.getData()
        self.doPrevious()
        self.lOps='mult'

    def div(self,now=0):
        if(now==1):
            try:
                self.preCalc=self.preCalc/self.postCalc
                return True
            except ZeroDivisionError:
                self.display('Zero Division Error')
                return False
        self.pressOp=True
        self.getData()
        self.doPrevious()
        self.lOps='div'

    def power(self,now=0):
        if(now==1):
            self.preCalc=self.preCalc**self.postCalc
            return True
        self.pressOp=True
        self.getData()
        self.doPrevious()
        self.lOps='pow'

    def equal(self):
        if(self.lOps!=''):
            self.getData()
        self.preEqOp=self.lOps if len(self.lOps)>0 else self.preEqOp
        self.lOps=''
        self.doPrevious(now=1)
        self.pressOp=True

    def facto(self):
        self.getData()
        self.preCalc=math.gamma(self.postCalc+1)
        self.display(self.preCalc)
        self.pressOp=True

    def sqrt(self):
        self.getData()
        self.preCalc=math.sqrt(self.postCalc+1)
        self.display(self.preCalc)
        self.pressOp=True

    def sin(self):
        self.getData()
        self.preCalc=math.sin(self.postCalc+1)
        self.display(self.preCalc)
        self.pressOp=True

    def cos(self):
        self.getData()
        self.preCalc=math.cos(self.postCalc+1)
        self.display(self.preCalc)
        self.pressOp=True

    def tan(self):
        self.getData()
        self.preCalc=math.tan(self.postCalc+1)
        self.display(self.preCalc)
        self.pressOp=True

    def log(self):
        self.getData()
        self.preCalc=math.log10(self.postCalc+1)
        self.display(self.preCalc)
        self.pressOp=True

    def ln(self):
        self.getData()
        self.preCalc=math.log(self.postCalc+1)
        self.display(self.preCalc)
        self.pressOp=True

op=Ops()

def setButtons(bHeight=3,bWidth=5,bPadX=5,bPadY=5):
    #row1
    bClear=ttk.Button(MainFrame,text='C',style='base.TButton',width=bWidth,command=lambda:op.clear()).grid(row=1,column=0,sticky='W',padx=0,pady=bPadY,ipadx=0,ipady=bHeight)
    bMod=ttk.Button(MainFrame,text='%',style='base.TButton',width=bWidth,command=lambda:op.mod()).grid(row=1,column=1,padx=bPadX,pady=bPadY,ipadx=0,ipady=bHeight)
    bDel=ttk.Button(MainFrame,text='Del',style='base.TButton',width=bWidth,command=lambda:op.delete()).grid(row=1,column=2,padx=bPadX,pady=bPadY,ipadx=0,ipady=bHeight)
    bDiv=ttk.Button(MainFrame,text='/',style='base.TButton',width=bWidth,command=lambda:op.div()).grid(row=1,column=3,padx=bPadX,pady=bPadY,ipadx=0,ipady=bHeight)
    bFacto=ttk.Button(MainFrame,text='!',style='sc.base.TButton',width=bWidth,command=lambda:op.facto()).grid(row=1,column=4,padx=bPadX,pady=bPadY,ipadx=0,ipady=bHeight)
    #row2
    b7=ttk.Button(MainFrame,text='7',style='num.base.TButton',width=bWidth,command=lambda:op.concat(7)).grid(row=2,column=0,sticky='W',padx=0,pady=bPadY,ipadx=0,ipady=bHeight)
    b8=ttk.Button(MainFrame,text='8',style='num.base.TButton',width=bWidth,command=lambda:op.concat(8)).grid(row=2,column=1,padx=bPadX,pady=bPadY,ipadx=0,ipady=bHeight)
    b9=ttk.Button(MainFrame,text='9',style='num.base.TButton',width=bWidth,command=lambda:op.concat(9)).grid(row=2,column=2,padx=bPadX,pady=bPadY,ipadx=0,ipady=bHeight)
    bMult=ttk.Button(MainFrame,text='x',style='base.TButton',width=bWidth,command=lambda:op.mult()).grid(row=2,column=3,padx=bPadX,pady=bPadY,ipadx=0,ipady=bHeight)
    bPow=ttk.Button(MainFrame,text='^',style='sc.base.TButton',width=bWidth,command=lambda:op.power()).grid(row=2,column=4,padx=bPadX,pady=bPadY,ipadx=0,ipady=bHeight)
    #row3
    b4=ttk.Button(MainFrame,text='4',style='num.base.TButton',width=bWidth,command=lambda:op.concat(4)).grid(row=3,column=0,sticky='W',padx=0,pady=bPadY,ipadx=0,ipady=bHeight)
    b5=ttk.Button(MainFrame,text='5',style='num.base.TButton',width=bWidth,command=lambda:op.concat(5)).grid(row=3,column=1,padx=bPadX,pady=bPadY,ipadx=0,ipady=bHeight)
    b6=ttk.Button(MainFrame,text='6',style='num.base.TButton',width=bWidth,command=lambda:op.concat(6)).grid(row=3,column=2,padx=bPadX,pady=bPadY,ipadx=0,ipady=bHeight)
    bSub=ttk.Button(MainFrame,text='-',style='base.TButton',width=bWidth,command=lambda:op.sub()).grid(row=3,column=3,padx=bPadX,pady=bPadY,ipadx=0,ipady=bHeight)
    bRoot=ttk.Button(MainFrame,text='Sqrt',style='sc.base.TButton',width=bWidth,command=lambda:op.sqrt()).grid(row=3,column=4,padx=bPadX,pady=bPadY,ipadx=0,ipady=bHeight)
    #row4
    b1=ttk.Button(MainFrame,text='1',style='num.base.TButton',width=bWidth,command=lambda:op.concat(1)).grid(row=4,column=0,sticky='W',padx=0,pady=bPadY,ipadx=0,ipady=bHeight)
    b2=ttk.Button(MainFrame,text='2',style='num.base.TButton',width=bWidth,command=lambda:op.concat(2)).grid(row=4,column=1,padx=bPadX,pady=bPadY,ipadx=0,ipady=bHeight)
    b3=ttk.Button(MainFrame,text='3',style='num.base.TButton',width=bWidth,command=lambda:op.concat(3)).grid(row=4,column=2,padx=bPadX,pady=bPadY,ipadx=0,ipady=bHeight)
    bAdd=ttk.Button(MainFrame,text='+',style='base.TButton',width=bWidth,command=lambda:op.add()).grid(row=4,column=3,padx=bPadX,pady=bPadY,ipadx=0,ipady=bHeight)
    bPi=ttk.Button(MainFrame,text='PI',style='sc.base.TButton',width=bWidth,command=lambda:op.concat(math.pi)).grid(row=4,column=4,padx=bPadX,pady=bPadY,ipadx=0,ipady=bHeight)
    #ro5
    b00=ttk.Button(MainFrame,text='00',style='num.base.TButton',width=bWidth,command=lambda:op.concat('00')).grid(row=5,column=0,sticky='W',padx=0,pady=bPadY,ipadx=0,ipady=bHeight)
    b0=ttk.Button(MainFrame,text='0',style='num.base.TButton',width=bWidth,command=lambda:op.concat(0)).grid(row=5,column=1,padx=bPadX,pady=bPadY,ipadx=0,ipady=bHeight)
    bDecimal=ttk.Button(MainFrame,text='.',style='base.TButton',width=bWidth,command=lambda:op.concat('.')).grid(row=5,column=2,padx=bPadX,pady=bPadY,ipadx=0,ipady=bHeight)
    bEqual=ttk.Button(MainFrame,text='=',style='base.TButton',width=bWidth,command=lambda:op.equal()).grid(row=5,column=3,padx=bPadX,pady=bPadY,ipadx=0,ipady=bHeight)
    bEuler=ttk.Button(MainFrame,text='e',style='sc.base.TButton',width=bWidth,command=lambda:op.concat(math.e)).grid(row=5,column=4,padx=bPadX,pady=bPadY,ipadx=0,ipady=bHeight)
    #row6
    bSin=ttk.Button(MainFrame,text='Sin',style='sc.base.TButton',width=bWidth,command=lambda:op.sin()).grid(row=6,column=0,sticky='W',padx=0,pady=bPadY,ipadx=0,ipady=bHeight)
    bCos=ttk.Button(MainFrame,text='Cos',style='sc.base.TButton',width=bWidth,command=lambda:op.cos()).grid(row=6,column=1,padx=bPadX,pady=bPadY,ipadx=0,ipady=bHeight)
    bTan=ttk.Button(MainFrame,text='Tan',style='sc.base.TButton',width=bWidth,command=lambda:op.tan()).grid(row=6,column=2,padx=bPadX,pady=bPadY,ipadx=0,ipady=bHeight)
    bLog=ttk.Button(MainFrame,text='Log',style='sc.base.TButton',width=bWidth,command=lambda:op.log()).grid(row=6,column=3,padx=bPadX,pady=bPadY,ipadx=0,ipady=bHeight)
    bLn=ttk.Button(MainFrame,text='Ln',style='sc.base.TButton',width=bWidth,command=lambda:op.ln()).grid(row=6,column=4,padx=bPadX,pady=bPadY,ipadx=0,ipady=bHeight)

def bigger():
    MainWindow.resizable(width=False,height=False)
    maintext.config(width=22)
    maintext.grid(ipadx=3)
    MainWindow.geometry("275x356")

def smaller():
    MainWindow.resizable(width=False,height=False)
    maintext.config(width=18)
    maintext.grid(ipadx=0)
    MainWindow.geometry("220x303")

setButtons(bHeight,bWidth,bPadX,bPadY)
MainFrame.grid(padx=0,pady=0)
menubar=tk.Menu(MainFrame)

# ManuBar 1 :
filemenu = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'File', menu = filemenu)
filemenu.add_command(label = "Standard", command = smaller)
filemenu.add_command(label = "Scientific", command = bigger)
MainWindow.config(menu=menubar)

MainWindow.mainloop()