import tkinter as tk

MainWindow = tk.Tk()
MainWindow.title("Scientific Calculator")
MainWindow.geometry("217x438")

MainFrame=tk.Frame(MainWindow)
maintext= tk.Text(MainFrame,height=2,width=25).grid(row=0,column=0,columnspan=5,sticky='W')

bHeight=3
bWidth=5
bPadX=5
bPadY=5

def setButtons(bHeight=3,bWidth=5,bPadX=5,bPadY=5):
    bClear=tk.Button(MainFrame,text='C',height=bHeight,width=bWidth).grid(row=1,column=0,sticky='W',padx=0,pady=bPadY)
    bMod=tk.Button(MainFrame,text='%',height=bHeight,width=bWidth).grid(row=1,column=1,padx=bPadX,pady=bPadY)
    bDel=tk.Button(MainFrame,text='Del',height=bHeight,width=bWidth).grid(row=1,column=2,padx=bPadX,pady=bPadY)
    bDiv=tk.Button(MainFrame,text='/',height=bHeight,width=bWidth).grid(row=1,column=3,padx=bPadX,pady=bPadY)
    bFacto=tk.Button(MainFrame,text='!',height=bHeight,width=bWidth).grid(row=1,column=4,padx=bPadX,pady=bPadY)

    b7=tk.Button(MainFrame,text='7',height=bHeight,width=bWidth).grid(row=2,column=0,sticky='W',padx=0,pady=bPadY)
    b8=tk.Button(MainFrame,text='8',height=bHeight,width=bWidth).grid(row=2,column=1,padx=bPadX,pady=bPadY)
    b9=tk.Button(MainFrame,text='9',height=bHeight,width=bWidth).grid(row=2,column=2,padx=bPadX,pady=bPadY)
    bMult=tk.Button(MainFrame,text='x',height=bHeight,width=bWidth).grid(row=2,column=3,padx=bPadX,pady=bPadY)
    bPow=tk.Button(MainFrame,text='^',height=bHeight,width=bWidth).grid(row=2,column=4,padx=bPadX,pady=bPadY)

    b4=tk.Button(MainFrame,text='4',height=bHeight,width=bWidth).grid(row=3,column=0,sticky='W',padx=0,pady=bPadY)
    b5=tk.Button(MainFrame,text='5',height=bHeight,width=bWidth).grid(row=3,column=1,padx=bPadX,pady=bPadY)
    b6=tk.Button(MainFrame,text='6',height=bHeight,width=bWidth).grid(row=3,column=2,padx=bPadX,pady=bPadY)
    bSub=tk.Button(MainFrame,text='-',height=bHeight,width=bWidth).grid(row=3,column=3,padx=bPadX,pady=bPadY)
    bRoot=tk.Button(MainFrame,text='Sqrt',height=bHeight,width=bWidth).grid(row=3,column=4,padx=bPadX,pady=bPadY)

    b1=tk.Button(MainFrame,text='1',height=bHeight,width=bWidth).grid(row=4,column=0,sticky='W',padx=0,pady=bPadY)
    b2=tk.Button(MainFrame,text='2',height=bHeight,width=bWidth).grid(row=4,column=1,padx=bPadX,pady=bPadY)
    b3=tk.Button(MainFrame,text='3',height=bHeight,width=bWidth).grid(row=4,column=2,padx=bPadX,pady=bPadY)
    bAdd=tk.Button(MainFrame,text='+',height=bHeight,width=bWidth).grid(row=4,column=3,padx=bPadX,pady=bPadY)
    bPi=tk.Button(MainFrame,text='PI',height=bHeight,width=bWidth).grid(row=4,column=4,padx=bPadX,pady=bPadY)

    b00=tk.Button(MainFrame,text='00',height=bHeight,width=bWidth).grid(row=5,column=0,sticky='W',padx=0,pady=bPadY)
    b0=tk.Button(MainFrame,text='0',height=bHeight,width=bWidth).grid(row=5,column=1,padx=bPadX,pady=bPadY)
    bDecimal=tk.Button(MainFrame,text='.',height=bHeight,width=bWidth).grid(row=5,column=2,padx=bPadX,pady=bPadY)
    bEqual=tk.Button(MainFrame,text='=',height=bHeight,width=bWidth).grid(row=5,column=3,padx=bPadX,pady=bPadY)
    bEuler=tk.Button(MainFrame,text='e',height=bHeight,width=bWidth).grid(row=5,column=4,padx=bPadX,pady=bPadY)

    bSin=tk.Button(MainFrame,text='Sin',height=bHeight,width=bWidth).grid(row=6,column=0,sticky='W',padx=0,pady=bPadY)
    bCos=tk.Button(MainFrame,text='Cos',height=bHeight,width=bWidth).grid(row=6,column=1,padx=bPadX,pady=bPadY)
    bTan=tk.Button(MainFrame,text='Tan',height=bHeight,width=bWidth).grid(row=6,column=2,padx=bPadX,pady=bPadY)
    bLog=tk.Button(MainFrame,text='Log',height=bHeight,width=bWidth).grid(row=6,column=3,padx=bPadX,pady=bPadY)
    bLn=tk.Button(MainFrame,text='Ln',height=bHeight,width=bWidth).grid(row=6,column=4,padx=bPadX,pady=bPadY)

def bigger():
    MainWindow.resizable(width=False,height=False)
    maintext= tk.Text(MainFrame,height=2,width=32).grid(row=0,column=0,columnspan=5,sticky='W')
    MainWindow.geometry("272x438")

def smaller():
    MainWindow.resizable(width=False,height=False)
    maintext= tk.Text(MainFrame,height=2,width=25).grid(row=0,column=0,columnspan=5,sticky='W')
    MainWindow.geometry("217x372")

setButtons(bHeight=3,bWidth=5,bPadX=5,bPadY=5)

MainFrame.grid(padx=5,pady=5)

menubar=tk.Menu(MainFrame)

# ManuBar 1 :
filemenu = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'File', menu = filemenu)
filemenu.add_command(label = "Standard", command = smaller)
filemenu.add_command(label = "Scientific", command = bigger)
MainWindow.config(menu=menubar)

MainWindow.mainloop()
