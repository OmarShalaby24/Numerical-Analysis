from tkinter import *
from sympy import Symbol, Derivative, var, sympify
import time


def bisection(a, b, func, epsilon, maxNumIteration):
    start_time = time.time()
    if (epsilon == ""):
        epsilon = 0.00001
    else:
        epsilon = float(epsilon)

    if (maxNumIteration == ""):
        maxNumIteration = 50
    else:
        maxNumIteration = float(maxNumIteration)

    numOfIterations = 0
    # to change from text to function
    x = var('x')
    exp = sympify(func)
    resA = exp.subs(x, a)
    resB = exp.subs(x, b)

    if (resA * resB >= 0):
        print("You have not assumed right a and b\n")
        return "you have not assumed right limits"

    c = a
    i = 0
    cOld = 0

    output = list()
    output.append("i\tXl\t\tXu\t\tXr\t\tf(Xr)\t\trelative error\n")
    while (((b - a) >= epsilon) and i < maxNumIteration):
        numOfIterations += 1

        # Find middle point
        c = (a + b) / 2
        resA = exp.subs(x, a)
        resB = exp.subs(x, b)
        resC = exp.subs(x, c)

        # Check if middle point is root
        if (resC == 0.0):
            break

        # Decide the side to repeat the steps
        if (resC * resA < 0):
            b = c
        else:
            a = c

        i += 1
        if (i > 1):
            relativeError = abs((c - cOld) / c)
            output.append("%d\t%.6f\t\t%.6f\t\t%.6f\t\t%.6f\t\t%.6f\n" % (i, a, b, c, resC, relativeError))
        else:
            output.append("%d\t%.6f\t\t%.6f\t\t%.6f\t\t%.6f\n" % (i, a, b, c, resC))

        cOld = c

    output.append("Required root is: %.8f\n" % c)
    output.append("Number of iterations is: %d\n" % i)
    output.append("Execution time: %s seconds\n" % (time.time() - start_time))

    return output


def bisection_win():
    def readData():
        f = open("bisection_falseReguli_file")
        exp = f.readline()
        textEntry.delete(0, END)
        textEntry.insert(0, exp)
        exp = f.readline()
        firstLimit.delete(0, END)
        firstLimit.insert(0, exp)
        exp = f.readline()
        secondLimit.delete(0, END)
        secondLimit.insert(0, exp)
        exp = f.readline()
        epsilon.delete(0, END)
        epsilon.insert(0, exp)
        exp = f.readline()
        iterations.delete(0, END)
        iterations.insert(0, exp)

    def clickBisection():
        enteredText = textEntry.get()  # this will get the text from the text entry box
        enteredFirstLimit = firstLimit.get()
        enteredSecondLimit = secondLimit.get()
        enteredEpsilon = epsilon.get()
        enteredMaxNumIteration = iterations.get()

        # completly clear the box
        output.delete(0.0, END)
        y = list()
        y = bisection(float(enteredFirstLimit), float(enteredSecondLimit), enteredText, enteredEpsilon,
                      enteredMaxNumIteration)
        for x in range(len(y)):
            output.insert(END, y[x])

    window = Tk()
    window.title("Bisection Method")
    window.configure(bg="#B4CDCD")
    window.geometry("725x650")

    m_label = Label(window, text="Bisection Method", bg="#53868B", fg="white", font=(15))
    m_label.place(x=301, y=20)

    func_label = Label(window, text="1.Enter your function", bg="#B4CDCD", fg="black")
    func_label.place(x=305, y=70)

    textEntry = Entry(window, width=50, bg="white", borderwidth=3)
    textEntry.place(x=215, y=95)

    # # to enter limits
    lowerLimit_label = Label(window, text="2.Enter X lower", bg="#B4CDCD", fg="black")
    lowerLimit_label.place(x=315, y=150)

    firstLimit = Entry(window, width=50, bg="white", borderwidth=3)
    firstLimit.place(x=215, y=175)

    upperLimit_label = Label(window, text="3.Enter X upper", bg="#B4CDCD", fg="black")
    upperLimit_label.place(x=315, y=230)

    secondLimit = Entry(window, width=50, bg="white", borderwidth=3)
    secondLimit.place(x=215, y=255)

    epsilon_label = Label(window, text="4.Enter epsilon", bg="#B4CDCD", fg="black")
    epsilon_label.place(x=320, y=310)

    epsilon = Entry(window, width=50, bg="white", borderwidth=3)
    epsilon.place(x=215, y=335)

    iterations_label = Label(window, text="5.Enter max number of iterations", bg="#B4CDCD", fg="black")
    iterations_label.place(x=275, y=395)

    iterations = Entry(window, width=50, bg="white", borderwidth=3)
    iterations.place(x=215, y=420)

    solve_btn = Button(window, text="Solve", width=20, height=1, bg="#53868B", fg="white", command=clickBisection)
    solve_btn.place(x=285, y=475)

    file_btn = Button(window, text="Load equation from file", width=20, height=1, bg="#53868B", fg="white",
                      command=readData)
    file_btn.place(x=285, y=515)

    output = Text(window, width=90, height=5.5, wrap=WORD, background="white")
    output.place(x=0, y=555)
