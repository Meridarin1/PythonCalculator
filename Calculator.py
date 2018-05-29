from tkinter import *
from tkinter import ttk


class Calculator:

    calcValue = 0
    s = ''
    oldSign = ''
    mathDone = False
    isDot = False
    setEq = False

    def __init__(self, root):

        self.entryValue = StringVar(root, value="0")

        root.title("Calculator")

        root.resizable(width=False, height=False)

        style = ttk.Style()
        style.configure("TButton", padding=10)

        style.configure("TEntry", font="Serif 40", padding=10)

        self.entryField = ttk.Entry(root, textvariable=self.entryValue, width=63)
        self.entryField.grid(row=0, sticky=N, pady=5)

        self.butAc = Button(root, text="AC", command=self.button_ac)
        self.butAc.config(width=10, height=3)
        self.butAc.grid(row=1, column=0, sticky=W, padx=4, pady=4)

        self.but1 = Button(root, text="1", command=lambda: self.button_pressed(1))
        self.but1.config(width=10, height=3)
        self.but1.grid(row=2, sticky=W, padx=4, pady=4)

        self.but2 = Button(root, text="2",command=lambda: self.button_pressed(2))
        self.but2.config(width=10, height=3)
        self.but2.grid(row=2, sticky=W, padx=100, pady=4)

        self.but3 = Button(root, text="3", command=lambda: self.button_pressed(3))
        self.but3.config(width=10, height=3)
        self.but3.grid(row=2, sticky=E, padx=125, pady=4)

        self.but4 = Button(root, text="4", command=lambda: self.button_pressed(4))
        self.but4.config(width=10, height=3)
        self.but4.grid(row=3, sticky=W, padx=4, pady=4)

        self.but5 = Button(root, text="5", command=lambda: self.button_pressed(5))
        self.but5.config(width=10, height=3)
        self.but5.grid(row=3, sticky=W, padx=100, pady=4)

        self.but6 = Button(root, text="6", command=lambda: self.button_pressed(6))
        self.but6.config(width=10, height=3)
        self.but6.grid(row=3, sticky=E, padx=125, pady=4)

        self.but7 = Button(root, text="7", command=lambda: self.button_pressed(7))
        self.but7.config(width=10, height=3)
        self.but7.grid(row=4, sticky=W, padx=4, pady=4)

        self.but8 = Button(root, text="8", command=lambda: self.button_pressed(8))
        self.but8.config(width=10, height=3)
        self.but8.grid(row=4, sticky=W, padx=100, pady=4)

        self.but9 = Button(root, text="9", command=lambda: self.button_pressed(9))
        self.but9.config(width=10, height=3)
        self.but9.grid(row=4, sticky=E, padx=125, pady=4)

        self.but0 = Button(root, text="0", command=lambda: self.button_pressed(0))
        self.but0.config(width=10, height=3)
        self.but0.grid(row=5, sticky=W, padx=100, pady=4)

        self.butAdd = Button(root, text="+", command=lambda: self.sign('+'))
        self.butAdd.config(width=10, height=3)
        self.butAdd.grid(row=2, sticky=E, padx=30, pady=4)

        self.butSub = Button(root, text="-", command=lambda: self.sign('-'))
        self.butSub.config(width=10, height=3)
        self.butSub.grid(row=3, sticky=E, padx=30, pady=4)

        self.butMult = Button(root, text="*", command=lambda: self.sign('*'))
        self.butMult.config(width=10, height=3)
        self.butMult.grid(row=4, sticky=E, padx=30, pady=4)

        self.butDiv = Button(root, text="/", command=lambda: self.sign('/'))
        self.butDiv.config(width=10, height=3)
        self.butDiv.grid(row=5, sticky=E, padx=30, pady=4)

        self.butEq = Button(root, text="=", command=self.eq)
        self.butEq.config(width=10, height=3)
        self.butEq.grid(row=5, sticky=E, padx=125, pady=4)

        self.butDot = Button(root, text=".", command=self.dot)
        self.butDot.config(width=10, height=3)
        self.butDot.grid(row=5, sticky=W, padx=4, pady=4)

    def button_pressed(self, value):

        if self.mathDone:
            self.entryValue.set("")
            self.mathDone = False
            self.isDot = False

        if self.setEq:
            self.calcValue = 0

        if self.entryValue.get() == '0' and value != 0:
            self.entryValue.set("")


        if not (self.entryValue.get() == '0' and value == 0):
            temp = self.entryValue.get()
            temp = temp + str(value)
            self.entryValue.set(temp)


    def button_ac(self):

        self.entryValue.set("0")
        self.s = ''
        self.mathDone = False
        self.isDot = False

    def sign(self, sign):

        if self.s == '':
            self.calcValue = self.entryValue.get()

        else:
            try:
                self.calcValue = eval(str(self.calcValue)+self.s+str(self.entryValue.get()))
                self.entryValue.set(self.calcValue)

            except ZeroDivisionError:
                self.entryValue.set("You can't do division by zero")
                self.s = ''
                self.calcValue = 0

        self.s = sign
        self.mathDone = True
        self.setEq = False

    def eq(self):

        if not self.s == '' and not self.setEq:

            try:
                self.calcValue = eval(str(self.calcValue) + self.s + str(self.entryValue.get()))
                self.entryValue.set(self.calcValue)

            except ZeroDivisionError:
                self.entryValue.set("You can't do division by zero")
                self.calcValue = 0

        self.setEq = True
        self.mathDone = True

    def dot(self):

        if not self.isDot:
            temp = self.entryValue.get()
            temp = temp + '.'
            self.entryValue.set(temp)
            self.isDot = True

