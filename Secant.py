from sympy import *
from tkinter import *

def f(t):
    x = symbols('x')
    eq = x**2-2
    return eq.subs(x,t)

def Secant(Fx,Xi_1,Xi,Ees,maxNumIteration):
    if (Ees == ""):
        Ees = 0.00001
    else:
        Ees = float(Ees)

    if (maxNumIteration == ""):
        maxNumIteration = 50
    else:
        maxNumIteration = float(maxNumIteration)

    x = var('x')
    exp = sympify(Fx)
    Xi_1 = 1
    Xi = 1.5
    FXi_1 = exp.subs(x, Xi_1)
    FXi = exp.subs(x, Xi)
    Ees = 0.01
    #print("Xi-1\t\t\t\t\t\t\t\tXi\t\t\t\t\t\t\t\tF(Xi-1)\t\t\t\t\t\t\t\tF(Xi)\t\t\t\t\t\t\t\tXi+1\t\t\t\t\t\t\t\tE")
    while True:
        Xi1 = Xi - (FXi*(Xi_1 - Xi))/(FXi_1 - FXi)
        E = abs(Xi1 - Xi)
        #print(str(Xi_1)+"\t\t\t\t"+str(Xi)+"\t\t\t\t"+str(FXi_1)+"\t\t\t\t"+str(FXi)+"\t\t\t\t"+str(Xi1)+"\t\t\t\t"+str(E))

        Xi_1 = Xi
        Xi = Xi1
        FXi_1 = exp.subs(x, Xi_1)
        FXi = exp.subs(x, Xi)
        if(E < Ees):
            break
    return Xi1

#                F(Xi) [Xi-1 - Xi]
#   Xi+1 = Xi - -----------------
#                F(Xi-1) - F(Xi)
#
#   |Xnew - Xold| < Ees


def secant_win():

    def clickSecant():
        enteredText = textEntry.get()  # this will get the text from the text entry box
        print(enteredText)
        enteredFirstLimit = firstLimit.get()
        enteredSecondLimit = secondLimit.get()
        enteredEpsilon = epsilon.get()
        enteredMaxNumIteration = iterations.get()
        # completly clear the box
        output.delete(0.0, END)
        output.insert(END, Secant(float(enteredFirstLimit), float(enteredSecondLimit), enteredText,
                                                   enteredEpsilon,
                                                   enteredMaxNumIteration))
    window = Tk()
    window.title("Secant Method")
    window.configure(bg="#B4CDCD")
    window.geometry("400x600")

    m_label = Label(window, text="Secant Method", bg="#53868B", fg="white", font=(15))
    m_label.grid(row=1, column=0, sticky=W)
    m_label.place(x=130, y=20)

    func_label = Label(window, text="1.Enter your function", bg="#E0EEEE", fg="black")
    func_label.grid(row=1, column=0, sticky=W)
    func_label.place(x=135, y=70)

    textEntry = Entry(window, width=50, bg="white", borderwidth=3)
    textEntry.grid(row=2, column=0, sticky=W)
    textEntry.place(x=50, y=95)

    #
    # # to enter limits
    lowerLimit_label = Label(window, text="2.Enter Xo", bg="#E0EEEE", fg="black")
    lowerLimit_label.grid(row=3, column=0, sticky=W)
    lowerLimit_label.place(x=160, y=150)

    firstLimit = Entry(window, width=50, bg="white", borderwidth=3)
    firstLimit.grid(row=4, column=0, sticky=W)
    firstLimit.place(x=50, y=175)

    upperLimit_label = Label(window, text="3.Enter X1", bg="#E0EEEE", fg="black")
    upperLimit_label.grid(row=3, column=0, sticky=W)
    upperLimit_label.place(x=160, y=230)

    secondLimit = Entry(window, width=50, bg="white", borderwidth=3)
    secondLimit.grid(row=4, column=0, sticky=W)
    secondLimit.place(x=50, y=255)

    epsilon_label = Label(window, text="4.Enter epsilon", bg="#E0EEEE", fg="black")
    epsilon_label.grid(row=3, column=0, sticky=W)
    epsilon_label.place(x=150, y=310)

    epsilon = Entry(window, width=50, bg="white", borderwidth=3)
    epsilon.grid(row=4, column=0, sticky=W)
    epsilon.place(x=50, y=335)

    iterations_label = Label(window, text="5.Enter max number of iterations", bg="#E0EEEE", fg="black")
    iterations_label.grid(row=3, column=0, sticky=W)
    iterations_label.place(x=110, y=395)

    iterations = Entry(window, width=50, bg="white", borderwidth=3)
    iterations.grid(row=4, column=0, sticky=W)
    iterations.place(x=50, y=420)

    solve_btn = Button(window, text="Solve", width=20, height=1, bg="#53868B", fg="white", command=clickSecant)
    solve_btn.grid(row=9, column=0, sticky=W)
    solve_btn.place(x=118, y=475)

    output = Text(window, width=75, height=5, wrap=WORD, background="white")
    output.grid(row=12, column=0, columnspan=2, sticky=W)
    output.place(x=0, y=525)

