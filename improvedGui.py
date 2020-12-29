# import tkinter as tk
from tkinter import *
import tkinter.font as font

from bisection import *
from falseRegula import *
from Secant import *
from NewtonRapson import *
from FixedPoint import *


# from newtonRaphson import newtonRaphson





#
#
# def clickFalseRegula():
#     enteredText = textEntry.get()  # this will get the text from the text entry box
#     print(enteredText)
#     enteredFirstLimit = FirstLimit.get()
#     enteredSecondLimit = secondLimit.get()
#     enteredEpsilon = epsilon.get()
#     enteredMaxNumIteration = maxNumIteration.get()
#     # completly clear the box
#     output.delete(0.0, END)
#     output.insert(END, regulaFalsi(float(enteredFirstLimit), float(enteredSecondLimit), enteredText, enteredEpsilon,
#                                    enteredMaxNumIteration))


# def clickNewtonRaphson():
#     enteredText = textEntry.get()  # this will get the text from the text entry box
#     print(enteredText)
#     # enteredText2 = textEntry.get()
#     # print(enteredText2)
#     enteredFirstLimit = FirstLimit.get()
#     enteredEpsilon = epsilon.get()
#     enteredMaxNumIteration = maxNumIteration.get()
#     # completly clear the box
#     output.delete(0.0, END)
#     output.insert(END, newtonRaphson(enteredText, float(enteredFirstLimit), enteredEpsilon,
#                                      enteredMaxNumIteration))




root = Tk()

# to enter function

root.configure(bg="#B4CDCD")
root.geometry("400x350")

# btn_font = font.Font(size=10)

label = Label(text="Choose a method for solution", bg="#E0EEEE", fg="black")
label.grid(row=1, column=0, sticky=W)
label.place(x=110, y=20)

bisection_btn = Button(root, text="Bisection", width=20, height=2, bg="#53868B", fg="white", command=bisection_win)
bisection_btn.grid(row=9, column=0, sticky=W)
bisection_btn.place(x=118, y=50)

regulaFalsi_btn = Button(root, text="False Position", width=20, height=2, bg="#53868B", fg="white",command=falseRegula_win)
regulaFalsi_btn.grid(row=9, column=0, sticky=W)
regulaFalsi_btn.place(x=118, y=100)

newtonRaphson_btn = Button(root, text="Newton Raphson", width=20, height=2, bg="#53868B", fg="white",command=raphson_win)
newtonRaphson_btn.grid(row=9, column=0, sticky=W)
newtonRaphson_btn.place(x=118, y=150)

fixedPoint_btn = Button(root, text="Fixed Point", width=20, height=2, bg="#53868B", fg="white" , command = FixedPoint_win)
fixedPoint_btn.grid(row=9, column=0, sticky=W)
fixedPoint_btn.place(x=118, y=200)

secant_btn = Button(root, text="Secant", width=20, height=2, bg="#53868B", fg="white",command=secant_win)
secant_btn.grid(row=9, column=0, sticky=W)
secant_btn.place(x=118, y=250)
# bisection_btn['font'] = btn_font

# func_label = Label(text="Enter Your function", bg="#E0EEEE", fg="black")
# func_label.grid(row=1, column=0, columnspan=3, sticky=W)
# func_label.place(x=10, y=20)
#
# textEntry = Entry(window, width=35, bg="white", borderwidth=5)
# textEntry.grid(row=2, column=0, sticky=W)
# textEntry.place(x=10, y=50)
#
# # # Label(text="enter your derv function", bg="black", fg="white").grid(row=1, column=1, sticky=W)
# # # textEntry2 = Entry(window, width=20, bg="white")
# # # textEntry2.grid(row=2, column=1, sticky=W)
# #
# # # to enter limits
# limits_label = Label(text="Enter your lower limit (negative one)", bg="#E0EEEE", fg="black")
# limits_label.grid(row=3, column=0, sticky=W)
# limits_label.place(x=10, y=90)

# bisection_btn = Button(window, text="Bisection", width=6)
# bisection_btn.grid(row=9, column=0, sticky=W)
# bisection_btn.place(x=10, y=50)

#
# FirstLimit = Entry(window, width=15, bg="white", borderwidth=5)
# FirstLimit.grid(row=4, column=0, sticky=W)
#
# Label(text="enter your upper limit", fg="black").grid(row=3, column=1, sticky=W)
#
# secondLimit = Entry(window, width=15, bg="white", borderwidth=5)
# secondLimit.grid(row=4, column=1, sticky=W)
#
# # to enter epsilon
# Label(text="Enter epsilon", fg="black").grid(row=5, column=0, sticky=W)
#
# epsilon = Entry(window, width=25, bg="white", borderwidth=5)
# epsilon.grid(row=6, column=0, sticky=W)
#
# # to enter max number of iteration
# Label(text="enter max number of iteration", fg="black").grid(row=7, column=0, sticky=W)
#
# maxNumIteration = Entry(window, width=25, bg="white", borderwidth=5)
# maxNumIteration.grid(row=8, column=0, sticky=W)
#
# Button(window, text="Bisection", width=6, command=clickBisection).grid(row=9, column=0, sticky=W)
# Button(window, text="false-Regula", width=10, command=clickFalseRegula).grid(row=9, column=1, sticky=W)
# # Button(window, text="Newton Raphson", width=14, command=clickNewtonRaphson).grid(row=9, column=2, sticky=W)
#
# output = Text(window, width=75, height=5, wrap=WORD, background="#B4CDCD")
# output.grid(row=12, column=0, columnspan=2, sticky=W)

# lazm tt7at 3ashan el window teban
root.mainloop()
