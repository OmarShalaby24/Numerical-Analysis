from sympy import Symbol, Derivative, var, sympify
from tkinter import *


# An example function whose solution
# is determined using Bisection Method.
# The function is x^3 - x^2 + 2


# Prints root of func(x) in interval [a, b]
def regulaFalsi(a, b, func, epsilon, maxNumIteration):
    if (epsilon == ""):
        epsilon = 0.00001
    else:
        epsilon = float(epsilon)

    if (maxNumIteration == ""):
        maxNumIteration = 50
    else:
        maxNumIteration = float(maxNumIteration)

    numOfIterations = 0
    i = 0

    # to change from text to function
    x = var('x')
    exp = sympify(func)
    resA = exp.subs(x, a)
    resB = exp.subs(x, b)

    if (resA * resB >= 0):
        print("You have not assumed right a and b\n")
        return "you have not assumed right limits"
    c = a  # Initialize result

    while (((b - a) >= epsilon) and i < maxNumIteration):
        numOfIterations += 1
        resA = exp.subs(x, a)
        resB = exp.subs(x, b)
        # Find the point that touches x axis
        c = (a * resB - b * resA) / (resB - resA)
        resC = exp.subs(x, c)
        # Check if the above found point is root
        if resC == 0:
            break

        # Decide the side to repeat the steps
        elif resC * resA < 0:
            b = c
        else:
            a = c
        i += 1
        print("f(a)= ", resA, "   f(b)=  ", resB, "    f(c)=  ", resC, "        ", b - a)
    print("The value of root is : ", '%.4f' % c)
    return c


def falseRegula_win():
    def clickflaseRegula():
        enteredText = textEntry.get()  # this will get the text from the text entry box
        print(enteredText)
        enteredFirstLimit = firstLimit.get()
        enteredSecondLimit = secondLimit.get()
        enteredEpsilon = epsilon.get()
        enteredMaxNumIteration = iterations.get()
        # completly clear the box
        output.delete(0.0, END)
        output.insert(END, regulaFalsi(float(enteredFirstLimit), float(enteredSecondLimit), enteredText,
                                       enteredEpsilon,
                                       enteredMaxNumIteration))

    window = Tk()
    window.title("False Regula Method")
    window.configure(bg="#B4CDCD")
    window.geometry("400x600")

    m_label = Label(window, text="False Regula Method", bg="#53868B", fg="white", font=(15))
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
    lowerLimit_label = Label(window, text="2.Enter X lower", bg="#E0EEEE", fg="black")
    lowerLimit_label.grid(row=3, column=0, sticky=W)
    lowerLimit_label.place(x=150, y=150)

    firstLimit = Entry(window, width=50, bg="white", borderwidth=3)
    firstLimit.grid(row=4, column=0, sticky=W)
    firstLimit.place(x=50, y=175)

    upperLimit_label = Label(window, text="3.Enter X upper", bg="#E0EEEE", fg="black")
    upperLimit_label.grid(row=3, column=0, sticky=W)
    upperLimit_label.place(x=150, y=230)

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

    solve_btn = Button(window, text="Solve", width=20, height=1, bg="#53868B", fg="white", command=clickflaseRegula)
    solve_btn.grid(row=9, column=0, sticky=W)
    solve_btn.place(x=118, y=475)

    output = Text(window, width=75, height=5, wrap=WORD, background="white")
    output.grid(row=12, column=0, columnspan=2, sticky=W)
    output.place(x=0, y=525)

# Driver code to test above function
# Initial values assumed
# a = -200
# b = 300
# regulaFalsi(a, b)
