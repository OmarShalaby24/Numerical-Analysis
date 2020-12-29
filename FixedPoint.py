from sympy import Symbol, Derivative, var, sympify, simplify, diff
from tkinter import *


def fixedPoint(equation, recurrentEquation, Xo, epsilon, maxIterations):
    if epsilon == "":
        epsilon = 0.00001
    else:
        epsilon = float(epsilon)

    if maxIterations == "":
        maxIterations = 50
    else:
        maxIterations = int(maxIterations)

    Xo = float(Xo)
    xnew = 0

    iterations = 1
    x = var('x')
    xcurrent = Xo
    relativeError = 100
    equation = simplify(equation)
    recurrentEquation = simplify(recurrentEquation)
    divRecEqn = diff(recurrentEquation, x)
    if abs(divRecEqn.subs(x, Xo)) < 1:
        print("i\t\tXi\t\t\t\tXi+1\t\t\trelative error")
        while relativeError > epsilon and iterations < maxIterations:
            xnew = recurrentEquation.subs(x, xcurrent)
            relativeError = abs((xnew - xcurrent) / xnew)
            print("%d\t\t%.6f\t\t%.6f\t\t%.6f" % (iterations, xcurrent, xnew, relativeError))
            xcurrent = xnew
            iterations = iterations + 1
        print("Required root is: %0.8f" % xnew)
        if iterations < 50:
            print("Number of iteration %d" % (iterations - 1))
        else:
            print("Number of iteration 50")
        return xcurrent
    else:
        print("Divergent")
        return "error"


fixedPoint('x*x*x + x*x -1', '1/sqrt(1+x)', '2', '0.00001', '10')


def FixedPoint_win():
    def clickFixedPoint():
        enteredText = textEntry.get()  # this will get the text from the text entry box  (Function)
        print(enteredText)
        enteredText2 = textEntry2.get()  # this will get the text from the text entry box (g(x))
        print(enteredText2)
        enteredFirstLimit = firstLimit.get()
        enteredEpsilon = epsilon.get()
        enteredMaxNumIteration = iterations.get()
        # completly clear the box
        output.delete(0.0, END)
        print("entered first limit")
        print(enteredFirstLimit)
        print("entered Epsilon")
        print(enteredEpsilon)
        print("Max it")
        print(enteredMaxNumIteration)
        output.insert(END,
                      fixedPoint(enteredText, enteredText2, enteredFirstLimit, enteredEpsilon, enteredMaxNumIteration))

    window = Tk()
    window.title("Newton Raphson Method")
    window.configure(bg="#B4CDCD")
    window.geometry("400x600")

    m_label = Label(window, text="Fixed Point Method", bg="#53868B", fg="white", font=(15))
    m_label.grid(row=1, column=0, sticky=W)
    m_label.place(x=130, y=20)

    func_label = Label(window, text="1.Enter your function", bg="#E0EEEE", fg="black")
    func_label.grid(row=1, column=0, sticky=W)
    func_label.place(x=140, y=70)

    textEntry = Entry(window, width=50, bg="white", borderwidth=3)
    textEntry.grid(row=2, column=0, sticky=W)
    textEntry.place(x=50, y=95)

    func2_label = Label(window, text="2.Enter your recurrent function", bg="#E0EEEE", fg="black")
    func2_label.grid(row=3, column=0, sticky=W)
    func2_label.place(x=120, y=150)

    textEntry2 = Entry(window, width=50, bg="white", borderwidth=3)
    textEntry2.grid(row=4, column=0, sticky=W)
    textEntry2.place(x=50, y=175)

    lowerLimit_label = Label(window, text="3.Enter Xo", bg="#E0EEEE", fg="black")
    lowerLimit_label.grid(row=3, column=0, sticky=W)
    lowerLimit_label.place(x=165, y=230)

    firstLimit = Entry(window, width=50, bg="white", borderwidth=3)
    firstLimit.grid(row=4, column=0, sticky=W)
    firstLimit.place(x=50, y=255)

    epsilon_label = Label(window, text="4.Enter epsilon", bg="#E0EEEE", fg="black")
    epsilon_label.grid(row=3, column=0, sticky=W)
    epsilon_label.place(x=155, y=310)

    epsilon = Entry(window, width=50, bg="white", borderwidth=3)
    epsilon.grid(row=4, column=0, sticky=W)
    epsilon.place(x=50, y=335)

    iterations_label = Label(window, text="5.Enter max number of iterations", bg="#E0EEEE", fg="black")
    iterations_label.grid(row=3, column=0, sticky=W)
    iterations_label.place(x=110, y=395)

    iterations = Entry(window, width=50, bg="white", borderwidth=3)
    iterations.grid(row=4, column=0, sticky=W)
    iterations.place(x=50, y=420)

    solve_btn = Button(window, text="Solve", width=20, height=1, bg="#53868B", fg="white", command=clickFixedPoint)
    solve_btn.grid(row=9, column=0, sticky=W)
    solve_btn.place(x=118, y=475)

    output = Text(window, width=75, height=5, wrap=WORD, background="white")
    output.grid(row=12, column=0, columnspan=2, sticky=W)
    output.place(x=0, y=525)
