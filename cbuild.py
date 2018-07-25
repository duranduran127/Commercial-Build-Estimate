import Tkinter as tk
import random
import time

from Tkinter import *

root = tk.Tk()
root.geometry("1600x800+0+0")
root.title("Commercial Building Estimate")

text_input = StringVar()
operator = ""

Tops = Frame(root, width=2000, height=100, relief=SUNKEN)
Tops.pack(side=TOP)

F1 = Frame(root, width=1500, height=1000,  relief=SUNKEN)
F1.pack(side=LEFT)

F2 = Frame(root, width=2000, height=1000,  relief=SUNKEN)
F2.pack(side=RIGHT)


#Time


localtime = time.asctime(time.localtime(time.time()))


#info


lblInfo = Label(Tops, font=('arial', 50, 'bold'), text="Commercial Building Estimate", fg="steel blue", bd=10, anchor="w")
lblInfo.grid(row=10, column=0)
lblDateTime = Label(Tops, font=('arial', 20, 'bold'),text=localtime, fg="steel blue", bd=10, anchor="w")
lblDateTime.grid(row=1, column=0)


#Calculator


def btnclick(numbers):
    global operator
    operator=operator + str(numbers)
    text_input.set(operator)

def btncleardisplay():
    global operator
    operator = ""
    text_input.set("")

def btnequalsinput():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)
    operator = ""

def ref():
    x =random.randint(12908, 50876)
    randomref = str(x)
    rand.set(randomref)

    CoDemo = float(Demo.get())
    CoFraming = float(Framing.get())
    CoElectrical = float(Electrical.get())
    CoPlumbing = float(Plumbing.get())
    CoHvac = float(HVAC.get())
    CoSheetrock = float(Sheetrock.get())
    CoTrim = float(Trim.get())
    CoPaint = float(Paint.get())
    CoDesks_Cabinets = float(Desks_Cabinets.get())
    CoFlooring = float(Flooring.get())
    CoChamhe_fee = float(Change_fee.get())
    CoPermitting = float(Permitting.get())

    Estimate = "$", str(CoDemo + CoFraming + CoElectrical + CoPlumbing + CoHvac + CoSheetrock + CoTrim + CoPaint +
                        CoDesks_Cabinets + CoFlooring + CoChamhe_fee + CoPermitting)

    Total_Estimate.set(Estimate)
def qexit():
    root.destroy()



def reset():
    rand.set("")
    Demo.set("")
    Framing.set("")
    Electrical.set("")
    Plumbing.set("")
    HVAC.set("")
    Sheetrock.set("")
    Trim.set("")
    Paint.set("")
    Desks_Cabinets.set("")
    Flooring.set("")
    Change_fee.set("")
    Permitting.set("")


txtDisplay = Entry(F2, font=('arial', 20, 'bold'), textvariable=text_input, bd=30, insertwidth=4,
                   bg="white", justify='right')
txtDisplay.grid(columnspan=4)

btn7 = Button(F2, padx=16, pady=16, bd=8, fg="black", font=('ariel', 20, 'bold'),
           text="7", bg="white", command=lambda: btnclick(7)).grid(row=2, column=0)

btn8 = Button(F2, padx=16, pady=16, bd=8, fg="black", font=('ariel', 20, 'bold'),
           text="8", bg="white", command=lambda: btnclick(8)).grid(row=2, column=1)

btn9 = Button(F2, padx=16, pady=16, bd=8, fg="black", font=('ariel', 20, 'bold'),
           text="9", bg="white", command=lambda: btnclick(9)).grid(row=2, column=2)

Addition = Button(F2, padx=16, pady=16, bd=8, fg="black", font=('ariel', 20, 'bold'),
           text="+", bg="white", command=lambda: btnclick("+")).grid(row=2, column=3)

btn4 = Button(F2, padx=16, pady=16, bd=8, fg="black", font=('ariel', 20, 'bold'),
           text="4", bg="white", command=lambda: btnclick(4)).grid(row=3, column=0)

btn5 = Button(F2, padx=16, pady=16, bd=8, fg="black", font=('ariel', 20, 'bold'),
           text="5", bg="white", command=lambda: btnclick(5)).grid(row=3, column=1)

btn6 = Button(F2, padx=16, pady=16, bd=8, fg="black", font=('ariel', 20, 'bold'),
           text="6", bg="white", command=lambda: btnclick(6)).grid(row=3, column=2)

Subtraction = Button(F2, padx=16, pady=16, bd=8, fg="black", font=('ariel', 20, 'bold'),
           text="-", bg="white", command=lambda: btnclick("-")).grid(row=3, column=3)

btn1 = Button(F2, padx=16, pady=16, bd=8, fg="black", font=('ariel', 20, 'bold'),
           text="1", bg="white", command=lambda: btnclick(1)).grid(row=4, column=0)

btn2 = Button(F2, padx=16, pady=16, bd=8, fg="black", font=('ariel', 20, 'bold'),
           text="2", bg="white", command=lambda: btnclick(2)).grid(row=4, column=1)

btn3 = Button(F2, padx=16, pady=16, bd=8, fg="black", font=('ariel', 20, 'bold'),
           text="3", bg="white", command=lambda: btnclick(3)).grid(row=4, column=2)

Multiply = Button(F2, padx=16, pady=16, bd=8, fg="black", font=('ariel', 20, 'bold'),
           text="*", bg="white", command=lambda: btnclick("*")).grid(row=4, column=3)

btn0 = Button(F2, padx=16, pady=16, bd=8, fg="black", font=('ariel', 20, 'bold'),
           text="0", bg="white", command=lambda: btnclick(0)).grid(row=5, column=0)

btnClear = Button(F2, padx=16, pady=16, bd=8, fg="black", font=('ariel', 20, 'bold'),
           text="c", bg="white", command=btncleardisplay).grid(row=5, column=1)

btnEqual = Button(F2, padx=16, pady=16, bd=8, fg="black", font=('ariel', 20, 'bold'),
           text="=", bg="white", command=btnequalsinput).grid(row=5, column=2)

Division = Button(F2, padx=16, pady=16, bd=8, fg="black", font=('ariel', 20, 'bold'),
           text="/", bg="white", command=lambda: btnclick("/")).grid(row=5, column=3)


#Commercial build info


rand = StringVar()
Demo = StringVar()
Framing = StringVar()
Electrical = StringVar()
Plumbing = StringVar()
HVAC = StringVar()
Sheetrock = StringVar()
Trim = StringVar()
Paint = StringVar()
Desks_Cabinets = StringVar()
Flooring = StringVar()
Change_fee = StringVar()
Permitting = StringVar()
Total_Estimate = StringVar()

lblReference = Label(F1, font=('ariel' , 16, 'bold'), text="Reference", bd=16, anchor='w')
lblReference.grid(row=0,column=0)
txtReference = Entry(F1, font=('ariel' , 16, 'bold'), textvariable=rand, bd=10, insertwidth=4,
                     bg="white", justify = 'right')
txtReference.grid(row=0,column=1)


lblDemo = Label(F1, font=('ariel' , 16, 'bold'), text="Demo", bd=16, anchor='w')
lblDemo.grid(row=1,column=0)
txtDemo = Entry(F1, font=('ariel' , 16, 'bold'), textvariable=Demo, bd=10, insertwidth=4,
                     bg="white", justify = 'right')
txtDemo.grid(row=1,column=1)

lblFraming = Label(F1, font=('ariel' , 16, 'bold'), text="Framing", bd=16, anchor='w')
lblFraming.grid(row=2,column=0)
txtFraming = Entry(F1, font=('ariel' , 16, 'bold'), textvariable=Framing, bd=10, insertwidth=4,
                     bg="white", justify = 'right')
txtFraming.grid(row=2,column=1)

lblElectrical = Label(F1, font=('ariel' , 16, 'bold'), text="Electrical", bd=16, anchor='w')
lblElectrical.grid(row=3,column=0)
txtElectrical = Entry(F1, font=('ariel' , 16, 'bold'), textvariable=Electrical, bd=10, insertwidth=4,
                     bg="white", justify = 'right')
txtElectrical.grid(row=3,column=1)

lblPlumbing = Label(F1, font=('ariel' , 16, 'bold'), text="Plumbing", bd=16, anchor='w')
lblPlumbing.grid(row=4,column=0)
txtPlumbing = Entry(F1, font=('ariel' , 16, 'bold'), textvariable=Plumbing, bd=10, insertwidth=4,
                     bg="white", justify = 'right')
txtPlumbing.grid(row=4,column=1)

lblHVAC = Label(F1, font=('ariel' , 16, 'bold'), text="HVAC", bd=16, anchor='w')
lblHVAC.grid(row=5,column=0)
txtHVAC = Entry(F1, font=('ariel' , 16, 'bold'), textvariable=HVAC, bd=10, insertwidth=4,
                     bg="white", justify = 'right')
txtHVAC.grid(row=5,column=1)

lblSheetrock = Label(F1, font=('ariel' , 16, 'bold'), text="Sheetrock", bd=16, anchor='w')
lblSheetrock.grid(row=6,column=0)
txtSheetrock = Entry(F1, font=('ariel' , 16, 'bold'), textvariable=Sheetrock, bd=10, insertwidth=4,
                     bg="white", justify = 'right')
txtSheetrock.grid(row=6,column=1)

lblTrim = Label(F1, font=('ariel' , 16, 'bold'), text="Trim", bd=16, anchor='w')
lblTrim.grid(row=7,column=0)
txtTrim = Entry(F1, font=('ariel' , 16, 'bold'), textvariable=Trim, bd=10, insertwidth=4,
                     bg="white", justify = 'right')
txtTrim.grid(row=7,column=1)

lblPaint = Label(F1, font=('ariel' , 16, 'bold'), text="Paint", bd=16, anchor='w')
lblPaint.grid(row=8,column=0)
txtPaint = Entry(F1, font=('ariel' , 16, 'bold'), textvariable=Paint, bd=10, insertwidth=4,
                     bg="white", justify = 'right')
txtPaint.grid(row=8,column=1)

lblDesks_Cabinets = Label(F1, font=('ariel' , 16, 'bold'), text="Desks and Cabinets", bd=16, anchor='w')
lblDesks_Cabinets.grid(row=9,column=0)
txtDesks_Cabinets = Entry(F1, font=('ariel' , 16, 'bold'), textvariable=Desks_Cabinets, bd=10, insertwidth=4,
                     bg="white", justify = 'right')
txtDesks_Cabinets.grid(row=9,column=1)

lblFlooring = Label(F1, font=('ariel' , 16, 'bold'), text="Flooring", bd=16, anchor='w')
lblFlooring.grid(row=10,column=0)
txtFlooring = Entry(F1, font=('ariel' , 16, 'bold'), textvariable=Flooring, bd=10, insertwidth=4,
                     bg="white", justify = 'right')
txtFlooring.grid(row=10,column=1)

lblChange_fee = Label(F1, font=('ariel' , 16, 'bold'), text="Order Change fee", bd=16, anchor='w')
lblChange_fee.grid(row=11,column=0)
txtChange_fee = Entry(F1, font=('ariel' , 16, 'bold'), textvariable=Change_fee, bd=10, insertwidth=4,
                     bg="white", justify = 'right')
txtChange_fee.grid(row=11,column=1)

lblPermitting = Label(F1, font=('ariel' , 16, 'bold'), text="Permitting", bd=16, anchor='w')
lblPermitting.grid(row=12,column=0)
txtPermitting = Entry(F1, font=('ariel' , 16, 'bold'), textvariable=Permitting, bd=10, insertwidth=4,
                     bg="white", justify = 'right')
txtPermitting.grid(row=12,column=1)

lblTotal_Estimate = Label(F1, font=('ariel' , 16, 'bold'), text="Total Estimate", bd=16, anchor='w')
lblTotal_Estimate.grid(row=0,column=2)
txtTotal_Estimate = Entry(F1, font=('ariel' , 16, 'bold'), textvariable=Total_Estimate, bd=10, insertwidth=4,
                     bg="white", justify = 'right')
txtTotal_Estimate.grid(row=0,column=3)


#Buttons


btnTotal = Button(F1, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=10,
                  text="Total", bg="blue", command=ref).grid(row=13, column=1)

btnreset = Button(F1, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=10,
                  text="Reset", bg="blue", command=reset).grid(row=13, column=2)

btnqexit = Button(F1, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=10,
                  text="Exit", bg="blue", command=qexit).grid(row=13, column=3)


































root.mainloop()
