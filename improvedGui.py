# import tkinter as tk
from tkinter import *
import tkinter.font as font

from bisection import *
from falseRegula import *
from Secant import *
from NewtonRapson import *
from FixedPoint import *

root = Tk()

# to enter function

root.configure(bg="#B4CDCD")
root.title("Numerical Analysis Methods")

root.geometry("400x350")

label = Label(text="Choose a method for solution", bg="#E0EEEE", fg="black")
label.place(x=110, y=20)

bisection_btn = Button(root, text="Bisection", width=20, height=2, bg="#53868B", fg="white", command=bisection_win)
bisection_btn.place(x=118, y=50)

regulaFalsi_btn = Button(root, text="False Position", width=20, height=2, bg="#53868B", fg="white",
                         command=falseRegula_win)
regulaFalsi_btn.place(x=118, y=100)

newtonRaphson_btn = Button(root, text="Newton Raphson", width=20, height=2, bg="#53868B", fg="white",
                           command=raphson_win)
newtonRaphson_btn.place(x=118, y=150)

fixedPoint_btn = Button(root, text="Fixed Point", width=20, height=2, bg="#53868B", fg="white", command=FixedPoint_win)
fixedPoint_btn.place(x=118, y=200)

secant_btn = Button(root, text="Secant", width=20, height=2, bg="#53868B", fg="white", command=secant_win)
secant_btn.place(x=118, y=250)

root.mainloop()
