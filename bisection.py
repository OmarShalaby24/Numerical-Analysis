from tkinter import *
from sympy import Symbol, Derivative, var, sympify


# Prints root of func(x)
# with error of EPSILON


def bisection(a, b, func, epsilon, maxNumIteration):
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

    print(resA, "   ", resB)
    c = a
    i = 0
    while (((b - a) >= epsilon) and i < maxNumIteration):
        numOfIterations += 1
        # Find middle point
        c = (a + b) / 2
        resA = exp.subs(x, a)
        resB = exp.subs(x, b)
        resC = exp.subs(x, c)
        print("f(a)= ", resA, "   f(b)=  ", resB, "    f(c)=  ", resC)
        # Check if middle point is root
        if (resC == 0.0):
            break

        # Decide the side to repeat the steps
        if (resC * resA < 0):
            b = c
        else:
            a = c

        i += 1

    print("The value of root is : ", "%.4f" % c)
    print("number of iterations is: ", numOfIterations)
    return c


# Driver code
# Initial values assumed
# a = -200
# b = 300
# bisection(a, b)


def bisection_win():
    def clickBisection():
        enteredText = textEntry.get()  # this will get the text from the text entry box
        print(enteredText)
        enteredFirstLimit = firstLimit.get()
        enteredSecondLimit = secondLimit.get()
        enteredEpsilon = epsilon.get()
        enteredMaxNumIteration = iterations.get()
        # completly clear the box
        output.delete(0.0, END)
        output.insert(END, bisection(float(enteredFirstLimit), float(enteredSecondLimit), enteredText,
                                     enteredEpsilon,
                                     enteredMaxNumIteration))

    window = Tk()
    window.title("Bisection Method")
    window.configure(bg="#B4CDCD")
    window.geometry("400x600")

    m_label = Label(window, text="Bisection Method", bg="#53868B", fg="white", font=(15))
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
    lowerLimit_label = Label(window, text="2.Enter your lower limit (negative one)", bg="#E0EEEE", fg="black")
    lowerLimit_label.grid(row=3, column=0, sticky=W)
    lowerLimit_label.place(x=95, y=150)

    firstLimit = Entry(window, width=50, bg="white", borderwidth=3)
    firstLimit.grid(row=4, column=0, sticky=W)
    firstLimit.place(x=50, y=175)

    upperLimit_label = Label(window, text="3.Enter your upper limit", bg="#E0EEEE", fg="black")
    upperLimit_label.grid(row=3, column=0, sticky=W)
    upperLimit_label.place(x=130, y=230)

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

    solve_btn = Button(window, text="Solve", width=20, height=1, bg="#53868B", fg="white", command=clickBisection)
    solve_btn.grid(row=9, column=0, sticky=W)
    solve_btn.place(x=118, y=475)

    output = Text(window, width=75, height=5, wrap=WORD, background="white")
    output.grid(row=12, column=0, columnspan=2, sticky=W)
    output.place(x=0, y=525)
