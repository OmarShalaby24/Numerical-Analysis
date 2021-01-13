from sympy import Symbol, Derivative, var, sympify, simplify, diff
from tkinter import *
import time


def fixedPoint(equation, recurrentEquation, Xo, epsilon, maxIterations):
    start_time = time.time()
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
        iterationOutput = list()

        iterationOutput.append("i\tXi\t\tXi+1\t\trelative error\n")
        print("i\t\tXi\t\t\t\tXi+1\t\t\trelative error")
        while relativeError > epsilon and iterations < maxIterations:
            xnew = recurrentEquation.subs(x, xcurrent)
            relativeError = abs((xnew - xcurrent) / xnew)
            print("%d\t\t%.6f\t\t%.6f\t\t%.6f" % (iterations, xcurrent, xnew, relativeError))
            iterationOutput.append("%d\t%.6f\t\t%.6f\t\t%.6f\n" % (iterations, xcurrent, xnew, relativeError))
            xcurrent = xnew
            iterations = iterations + 1
        print("Required root is: %0.8f" % xnew)
        iterationOutput.append("Required root is: %0.8f\n" % xnew)
        if iterations < 50:
            iterationOutput.append("Number of iterations %d\n" % (iterations - 1))
            print("Number of iterations %d" % (iterations - 1))
        else:
            iterationOutput.append("Number of iteration 50\n")
            print("Number of iteration 50")
        print("Execution time: %s seconds " % (time.time() - start_time))
        iterationOutput.append("Execution time: %s seconds\n" % (time.time() - start_time))
        return iterationOutput
    else:
        print("Divergent")
        return "error"


def FixedPoint_win():
    def readData():
        f = open("fixedPoint_file")
        exp = f.readline()
        textEntry.delete(0, END)
        textEntry.insert(0, exp)
        exp = f.readline()
        textEntry2.delete(0, END)
        textEntry2.insert(0, exp)
        exp = f.readline()
        firstLimit.delete(0, END)
        firstLimit.insert(0, exp)
        exp = f.readline()
        epsilon.delete(0, END)
        epsilon.insert(0, exp)
        exp = f.readline()
        iterations.delete(0, END)
        iterations.insert(0, exp)

    def clickFixedPoint():
        enteredText = textEntry.get()  # this will get the text from the text entry box  (Function)
        enteredText2 = textEntry2.get()  # this will get the text from the text entry box (g(x))
        enteredFirstLimit = firstLimit.get()
        enteredEpsilon = epsilon.get()
        enteredMaxNumIteration = iterations.get()

        # completly clear the box
        output.delete(0.0, END)
        y = list()
        y = fixedPoint(enteredText, enteredText2, enteredFirstLimit, enteredEpsilon, enteredMaxNumIteration)
        for x in range(len(y)):
            output.insert(END, y[x])

    window = Tk()
    window.title("Fixed Point")
    window.configure(bg="#B4CDCD")
    window.geometry("440x650")

    m_label = Label(window, text="Fixed Point Method", bg="#53868B", fg="white", font=(15))
    m_label.place(x=145, y=20)

    func_label = Label(window, text="1.Enter your function", bg="#B4CDCD", fg="black")
    func_label.place(x=155, y=70)

    textEntry = Entry(window, width=50, bg="white", borderwidth=3)
    textEntry.place(x=65, y=95)

    func2_label = Label(window, text="2.Enter your recurrent function", bg="#B4CDCD", fg="black")
    func2_label.place(x=135, y=150)

    textEntry2 = Entry(window, width=50, bg="white", borderwidth=3)
    textEntry2.place(x=65, y=175)

    lowerLimit_label = Label(window, text="3.Enter Xo", bg="#B4CDCD", fg="black")
    lowerLimit_label.place(x=185, y=230)

    firstLimit = Entry(window, width=50, bg="white", borderwidth=3)
    firstLimit.place(x=65, y=255)

    epsilon_label = Label(window, text="4.Enter epsilon", bg="#B4CDCD", fg="black")
    epsilon_label.place(x=175, y=310)

    epsilon = Entry(window, width=50, bg="white", borderwidth=3)
    epsilon.place(x=65, y=335)

    iterations_label = Label(window, text="5.Enter max number of iterations", bg="#B4CDCD", fg="black")
    iterations_label.place(x=130, y=395)

    iterations = Entry(window, width=50, bg="white", borderwidth=3)
    iterations.place(x=65, y=420)

    solve_btn = Button(window, text="Solve", width=20, height=1, bg="#53868B", fg="white", command=clickFixedPoint)
    solve_btn.place(x=145, y=475)

    file_btn = Button(window, text="Load equation from file", width=20, height=1, bg="#53868B", fg="white",
                      command=readData)
    file_btn.place(x=145, y=515)

    output = Text(window, width=55, height=5.5, wrap=WORD, background="white")
    output.place(x=0, y=555)
