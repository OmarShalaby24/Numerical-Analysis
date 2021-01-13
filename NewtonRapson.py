import time
from tkinter import *
from sympy.solvers import solvers

from sympy import *


def newtonRaphson(x0, func, epsilon, maxNumIteration):
    start_time = time.time()
    if (epsilon == ""):
        epsilon = 0.00001
    else:
        epsilon = float(epsilon)

    if (maxNumIteration == ""):
        maxNumIteration = 50
    else:
        maxNumIteration = float(maxNumIteration)

    x0 = float(x0)
    step = 1

    x = var('x')
    relativeError = 100
    func = simplify(func)
    derivative = diff(func, x)

    output = list()
    output.append("i\tXi\t\tXi+1\t\trelative error\n")
    print("i\t\tXi\t\t\t\tXi+1\t\t\trelative error")
    while relativeError > epsilon and step < maxNumIteration:

        if derivative.subs(x, x0) == 0.0:
            print('divide by zero error!')
            break

        x_new = x0 - ((func.subs(x, x0)) / (derivative.subs(x, x0)))

        relativeError = abs((x_new - x0) / x_new)

        output.append("%d\t%.6f\t\t%.6f\t\t%.6f\n" % (step, x0, x_new, relativeError))
        print("%d\t\t%.6f\t\t\t\t%.6f\t\t\t%.6f" % (step, x0, x_new, relativeError))

        x0 = x_new
        step += 1

    print("Required root is: %0.8f" % x_new)
    output.append("Required root is: %0.8f\n" % x_new)

    if step < 50:
        output.append("Number of iterations %d\n" % (step - 1))
        print("Number of iterations %d" % (step - 1))
    else:
        output.append("Number of iterations 50\n")

    output.append("Execution time: %s seconds\n" % (time.time() - start_time))
    print("Execution time: %s seconds\n" % (time.time() - start_time))

    return output


def raphson_win():
    def readData():
        f = open("newtonRaphson_file")
        exp = f.readline()
        textEntry.delete(0, END)
        textEntry.insert(0, exp)
        exp = f.readline()
        firstLimit.delete(0, END)
        firstLimit.insert(0, exp)
        exp = f.readline()
        epsilon.delete(0, END)
        epsilon.insert(0, exp)
        exp = f.readline()
        iterations.delete(0, END)
        iterations.insert(0, exp)

    def clickRaphson():
        enteredText = textEntry.get()  # this will get the text from the text entry box
        enteredFirstLimit = firstLimit.get()
        enteredEpsilon = epsilon.get()
        enteredMaxNumIteration = iterations.get()
        # completly clear the box
        output.delete(0.0, END)
        y = list()
        y = newtonRaphson(float(enteredFirstLimit), enteredText, enteredEpsilon, enteredMaxNumIteration)
        for x in range(len(y)):
            output.insert(END, y[x])

    window = Tk()
    window.title("Newton Raphson Method")
    window.configure(bg="#B4CDCD")
    window.geometry("440x580")

    m_label = Label(window, text="Newton Raphson Method", bg="#53868B", fg="white", font=(15))
    m_label.place(x=130, y=20)

    func_label = Label(window, text="1.Enter your function", bg="#B4CDCD", fg="black")
    func_label.place(x=155, y=70)

    textEntry = Entry(window, width=50, bg="white", borderwidth=3)
    textEntry.place(x=65, y=95)

    # # to enter limits
    lowerLimit_label = Label(window, text="2.Enter Xo", bg="#B4CDCD", fg="black")
    lowerLimit_label.place(x=185, y=150)

    firstLimit = Entry(window, width=50, bg="white", borderwidth=3)
    firstLimit.place(x=65, y=175)

    epsilon_label = Label(window, text="3.Enter epsilon", bg="#B4CDCD", fg="black")
    epsilon_label.place(x=175, y=230)

    epsilon = Entry(window, width=50, bg="white", borderwidth=3)
    epsilon.place(x=65, y=255)

    iterations_label = Label(window, text="4.Enter max number of iterations", bg="#B4CDCD", fg="black")
    iterations_label.place(x=120, y=315)

    iterations = Entry(window, width=50, bg="white", borderwidth=3)
    iterations.place(x=65, y=340)

    solve_btn = Button(window, text="Solve", width=20, height=1, bg="#53868B", fg="white", command=clickRaphson)
    solve_btn.place(x=135, y=400)

    file_btn = Button(window, text="Load equation from file", width=20, height=1, bg="#53868B", fg="white",
                      command=readData)
    file_btn.place(x=135, y=440)

    output = Text(window, width=55, height=5.5, wrap=WORD, background="white")
    output.place(x=0, y=480)
