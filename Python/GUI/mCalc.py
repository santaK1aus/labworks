import tkinter as tk
import time
import math

MainWindow = tk.Tk()
MainWindow.title("Scientific Calculator")
MainWindow.geometry("217x370")

MainFrame=tk.Frame(MainWindow)
maintext= tk.Entry(MainFrame,width=18,font=('Helvetica',14,'bold'),border=4,justify='right')
maintext.grid(row=0,column=0,columnspan=5,sticky='W')
maintext.insert(0,'0')

bHeight=3
bWidth=5
bPadX=5
bPadY=5

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
            maintext.delete(0,5)
            maintext.insert(0,'0')
    
    def doPrevious(self):
        dictf={'add':self.add,'sub':self.sub,'mult':self.mult,'div':self.div,'mod':self.mod,'pow':self.power}
        if(not len(self.lOps)>0):
            return
        dictf[self.lOps](now=1)
        self.display(self.preCalc)
    
    def display(self,x):
        maintext.delete(0,len(maintext.get()))
        maintext.insert(0,str(x))

    def mod(self,now=0):
        if(now==1):
            self.preCalc=self.preCalc/100*self.postCalc
            return
        self.pressOp=True
        self.getData()
        self.doPrevious()
        self.lOps='mod'

    def add(self,now=0):
        if(now==1):
            self.preCalc=self.preCalc+self.postCalc
            return
        self.pressOp=True
        self.getData()
        self.doPrevious()
        self.lOps='add'

    def sub(self,now=0):
        if(now==1):
            self.preCalc=self.preCalc-self.postCalc
            return
        self.pressOp=True
        self.getData()
        self.doPrevious()
        self.lOps='sub'

    def mult(self,now=0):
        if(now==1):
            self.preCalc=self.preCalc*self.postCalc
            return
        self.pressOp=True
        self.getData()
        self.doPrevious()
        self.lOps='mult'

    def div(self,now=0):
        if(now==1):
            self.preCalc=self.preCalc/self.postCalc
            return
        self.pressOp=True
        self.getData()
        self.doPrevious()
        self.lOps='div'

    def power(self,now=0):
        if(now==1):
            self.preCalc=self.preCalc**self.postCalc
            return
        self.pressOp=True
        self.getData()
        self.doPrevious()
        self.lOps='pow'

    def equal(self):
        self.getData()
        self.doPrevious()
        self.pressOp=True
        self.lOps=''

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

    bClear=tk.Button(MainFrame,text='C',height=bHeight,width=bWidth,command=lambda:op.clear()).grid(row=1,column=0,sticky='W',padx=0,pady=bPadY)
    bMod=tk.Button(MainFrame,text='%',height=bHeight,width=bWidth,command=lambda:op.mod()).grid(row=1,column=1,padx=bPadX,pady=bPadY)
    bDel=tk.Button(MainFrame,text='Del',height=bHeight,width=bWidth,command=lambda:op.delete()).grid(row=1,column=2,padx=bPadX,pady=bPadY)
    bDiv=tk.Button(MainFrame,text='/',height=bHeight,width=bWidth,command=lambda:op.div()).grid(row=1,column=3,padx=bPadX,pady=bPadY)
    bFacto=tk.Button(MainFrame,text='!',height=bHeight,width=bWidth,command=lambda:op.facto()).grid(row=1,column=4,padx=bPadX,pady=bPadY)

    b7=tk.Button(MainFrame,text='7',height=bHeight,width=bWidth,command=lambda:op.concat(7)).grid(row=2,column=0,sticky='W',padx=0,pady=bPadY)
    b8=tk.Button(MainFrame,text='8',height=bHeight,width=bWidth,command=lambda:op.concat(8)).grid(row=2,column=1,padx=bPadX,pady=bPadY)
    b9=tk.Button(MainFrame,text='9',height=bHeight,width=bWidth,command=lambda:op.concat(9)).grid(row=2,column=2,padx=bPadX,pady=bPadY)
    bMult=tk.Button(MainFrame,text='x',height=bHeight,width=bWidth,command=lambda:op.mult()).grid(row=2,column=3,padx=bPadX,pady=bPadY)
    bPow=tk.Button(MainFrame,text='^',height=bHeight,width=bWidth,command=lambda:op.power()).grid(row=2,column=4,padx=bPadX,pady=bPadY)

    b4=tk.Button(MainFrame,text='4',height=bHeight,width=bWidth,command=lambda:op.concat(4)).grid(row=3,column=0,sticky='W',padx=0,pady=bPadY)
    b5=tk.Button(MainFrame,text='5',height=bHeight,width=bWidth,command=lambda:op.concat(5)).grid(row=3,column=1,padx=bPadX,pady=bPadY)
    b6=tk.Button(MainFrame,text='6',height=bHeight,width=bWidth,command=lambda:op.concat(6)).grid(row=3,column=2,padx=bPadX,pady=bPadY)
    bSub=tk.Button(MainFrame,text='-',height=bHeight,width=bWidth,command=lambda:op.sub()).grid(row=3,column=3,padx=bPadX,pady=bPadY)
    bRoot=tk.Button(MainFrame,text='Sqrt',height=bHeight,width=bWidth,command=lambda:op.sqrt()).grid(row=3,column=4,padx=bPadX,pady=bPadY)

    b1=tk.Button(MainFrame,text='1',height=bHeight,width=bWidth,command=lambda:op.concat(1)).grid(row=4,column=0,sticky='W',padx=0,pady=bPadY)
    b2=tk.Button(MainFrame,text='2',height=bHeight,width=bWidth,command=lambda:op.concat(2)).grid(row=4,column=1,padx=bPadX,pady=bPadY)
    b3=tk.Button(MainFrame,text='3',height=bHeight,width=bWidth,command=lambda:op.concat(3)).grid(row=4,column=2,padx=bPadX,pady=bPadY)
    bAdd=tk.Button(MainFrame,text='+',height=bHeight,width=bWidth,command=lambda:op.add()).grid(row=4,column=3,padx=bPadX,pady=bPadY)
    bPi=tk.Button(MainFrame,text='PI',height=bHeight,width=bWidth,command=lambda:op.concat(math.pi)).grid(row=4,column=4,padx=bPadX,pady=bPadY)

    b00=tk.Button(MainFrame,text='00',height=bHeight,width=bWidth,command=lambda:op.concat('00')).grid(row=5,column=0,sticky='W',padx=0,pady=bPadY)
    b0=tk.Button(MainFrame,text='0',height=bHeight,width=bWidth,command=lambda:op.concat(0)).grid(row=5,column=1,padx=bPadX,pady=bPadY)
    bDecimal=tk.Button(MainFrame,text='.',height=bHeight,width=bWidth,command=lambda:op.concat('.')).grid(row=5,column=2,padx=bPadX,pady=bPadY)
    bEqual=tk.Button(MainFrame,text='=',height=bHeight,width=bWidth,command=lambda:op.equal()).grid(row=5,column=3,padx=bPadX,pady=bPadY)
    bEuler=tk.Button(MainFrame,text='e',height=bHeight,width=bWidth,command=lambda:op.concat(math.e)).grid(row=5,column=4,padx=bPadX,pady=bPadY)

    bSin=tk.Button(MainFrame,text='Sin',height=bHeight,width=bWidth,command=lambda:op.sin()).grid(row=6,column=0,sticky='W',padx=0,pady=bPadY)
    bCos=tk.Button(MainFrame,text='Cos',height=bHeight,width=bWidth,command=lambda:op.cos()).grid(row=6,column=1,padx=bPadX,pady=bPadY)
    bTan=tk.Button(MainFrame,text='Tan',height=bHeight,width=bWidth,command=lambda:op.tan()).grid(row=6,column=2,padx=bPadX,pady=bPadY)
    bLog=tk.Button(MainFrame,text='Log',height=bHeight,width=bWidth,command=lambda:op.log()).grid(row=6,column=3,padx=bPadX,pady=bPadY)
    bLn=tk.Button(MainFrame,text='Ln',height=bHeight,width=bWidth,command=lambda:op.ln()).grid(row=6,column=4,padx=bPadX,pady=bPadY)

def bigger():
    MainWindow.resizable(width=False,height=False)
    maintext.config(width=23)
    MainWindow.geometry("272x436")

def smaller():
    MainWindow.resizable(width=False,height=False)
    maintext.config(width=18)
    MainWindow.geometry("217x370")

setButtons(bHeight,bWidth,bPadX,bPadY)

MainFrame.grid(padx=5,pady=5)

menubar=tk.Menu(MainFrame)

# ManuBar 1 :
filemenu = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'File', menu = filemenu)
filemenu.add_command(label = "Standard", command = smaller)
filemenu.add_command(label = "Scientific", command = bigger)
MainWindow.config(menu=menubar)

MainWindow.mainloop()
