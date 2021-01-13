from sympy import *
from tkinter import *
import time


def f(t):
    x = symbols('x')
    eq = x ** 2 - 2
    return eq.subs(x, t)


def Secant(Fx, Xi_1, Xi, Ees, maxNumIteration):
    start_time = time.time()
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

    FXi_1 = exp.subs(x, Xi_1)
    FXi = exp.subs(x, Xi)
    E = 100
    Xi1 = 0
    iterations = 1
    output = list()
    output.append("i\tXi-1\t\tXi\t\tXi+1\t\trelative error\n")
    print("i\tXi-1\t\tXi\t\tXi+1\t\trelative error\n")

    while E > Ees and iterations <= maxNumIteration:
        Xi1 = Xi - (FXi * (Xi_1 - Xi)) / (FXi_1 - FXi)
        E = abs((Xi1 - Xi) / Xi1)
        print(str(Xi_1) + "\t\t\t\t" + str(Xi) + "\t\t\t\t" + str(FXi_1) + "\t\t\t\t" + str(FXi) + "\t\t\t\t" + str(
            Xi1) + "\t\t\t\t" + str(E))
        output.append("%d\t%.6f\t\t%.6f\t\t%.6f\t\t%.6f\n" % (iterations, Xi_1, Xi, Xi1, E))
        iterations += 1
        Xi_1 = Xi
        Xi = Xi1
        FXi_1 = exp.subs(x, Xi_1)
        FXi = exp.subs(x, Xi)

    output.append("Required root is: %.8f\n" % Xi1)
    print("Required root is: %.8f\n" % Xi1)
    if iterations < 50:
        output.append("Number of iterations %d\n" % (iterations - 1))
    else:
        output.append("Number of iterations 50\n")

    output.append("Execution time: %s seconds\n" % (time.time() - start_time))
    return output


#                F(Xi) [Xi-1 - Xi]
#   Xi+1 = Xi - -----------------
#                F(Xi-1) - F(Xi)
#
#   |Xnew - Xold| < Ees


def secant_win():
    def readData():
        f = open("secant_file")
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

    def clickSecant():
        enteredText = textEntry.get()  # this will get the text from the text entry box
        enteredFirstLimit = firstLimit.get()
        enteredSecondLimit = secondLimit.get()
        enteredEpsilon = epsilon.get()
        enteredMaxNumIteration = iterations.get()

        # completly clear the box
        output.delete(0.0, END)
        y = list()
        y = Secant(enteredText, float(enteredFirstLimit), float(enteredSecondLimit), enteredEpsilon,
                   enteredMaxNumIteration)
        for x in range(len(y)):
            output.insert(END, y[x])

    window = Tk()
    window.title("Secant Method")
    window.configure(bg="#B4CDCD")
    window.geometry("600x650")

    m_label = Label(window, text="Secant Method", bg="#53868B", fg="white", font=(15))
    m_label.place(x=240, y=20)

    func_label = Label(window, text="1.Enter your function", bg="#B4CDCD", fg="black")
    func_label.place(x=235, y=70)

    textEntry = Entry(window, width=50, bg="white", borderwidth=3)
    textEntry.place(x=145, y=95)

    # # to enter limits
    lowerLimit_label = Label(window, text="2.Enter Xo", bg="#B4CDCD", fg="black")
    lowerLimit_label.place(x=265, y=150)

    firstLimit = Entry(window, width=50, bg="white", borderwidth=3)
    firstLimit.place(x=145, y=175)

    upperLimit_label = Label(window, text="3.Enter X1", bg="#B4CDCD", fg="black")
    upperLimit_label.place(x=265, y=230)

    secondLimit = Entry(window, width=50, bg="white", borderwidth=3)
    secondLimit.place(x=145, y=255)

    epsilon_label = Label(window, text="4.Enter epsilon", bg="#B4CDCD", fg="black")
    epsilon_label.place(x=250, y=310)

    epsilon = Entry(window, width=50, bg="white", borderwidth=3)
    epsilon.place(x=145, y=335)

    iterations_label = Label(window, text="5.Enter max number of iterations", bg="#B4CDCD", fg="black")
    iterations_label.place(x=205, y=395)

    iterations = Entry(window, width=50, bg="white", borderwidth=3)
    iterations.place(x=145, y=420)

    solve_btn = Button(window, text="Solve", width=20, height=1, bg="#53868B", fg="white", command=clickSecant)
    solve_btn.place(x=215, y=475)

    file_btn = Button(window, text="Load equation from file", width=20, height=1, bg="#53868B", fg="white",
                      command=readData)
    file_btn.place(x=215, y=515)

    output = Text(window, width=95, height=5.5, wrap=WORD, background="white")
    output.place(x=0, y=555)
