from tkinter import *
from sympy import *

def newtonRaphson(x0,func , epsilon, maxNumIteration):
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

    print("i\t\tXi\t\t\t\tXi+1\t\t\trelative error")
    while relativeError > epsilon and step < maxNumIteration:

        if derivative.subs(x, x0) == 0.0:
            print('divide by zero error!')
            break

        x_new = x0 - ((func.subs(x, x0)) / (derivative.subs(x, x0)))

        relativeError = abs((x_new - x0) / x_new)

        print("%d\t\t%.6f\t\t\t\t%.6f\t\t\t%.6f" % (step, x0, x_new, relativeError))

        x0 = x_new

        step += 1
    print("Required root is: %0.8f" % x_new)

    if step < 50:
        print("Number of iteration %d" % (step - 1))
    else:
        print("Number of iteration 50")
    return x_new






def raphson_win():

    def clickRaphson():
        enteredText = textEntry.get()  # this will get the text from the text entry box
        print(enteredText)
        enteredFirstLimit = firstLimit.get()
        enteredEpsilon = epsilon.get()
        enteredMaxNumIteration = iterations.get()
        # completly clear the box
        output.delete(0.0, END)
        output.insert(END, newtonRaphson(float(enteredFirstLimit), enteredText,
                                                   enteredEpsilon,
                                                   enteredMaxNumIteration))
    window = Tk()
    window.title("Newton Raphson Method")
    window.configure(bg="#B4CDCD")
    window.geometry("400x600")

    m_label = Label(window, text="Newton Raphson", bg="#53868B", fg="white", font=(15))
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
    lowerLimit_label.place(x=165, y=150)

    firstLimit = Entry(window, width=50, bg="white", borderwidth=3)
    firstLimit.grid(row=4, column=0, sticky=W)
    firstLimit.place(x=50, y=175)


    epsilon_label = Label(window, text="3.Enter epsilon", bg="#E0EEEE", fg="black")
    epsilon_label.grid(row=3, column=0, sticky=W)
    epsilon_label.place(x=150, y=230)

    epsilon = Entry(window, width=50, bg="white", borderwidth=3)
    epsilon.grid(row=4, column=0, sticky=W)
    epsilon.place(x=50, y=255)

    iterations_label = Label(window, text="4.Enter max number of iterations", bg="#E0EEEE", fg="black")
    iterations_label.grid(row=3, column=0, sticky=W)
    iterations_label.place(x=110, y=315)

    iterations = Entry(window, width=50, bg="white", borderwidth=3)
    iterations.grid(row=4, column=0, sticky=W)
    iterations.place(x=50, y=340)

    solve_btn = Button(window, text="Solve", width=20, height=1, bg="#53868B", fg="white", command=clickRaphson)
    solve_btn.grid(row=9, column=0, sticky=W)
    solve_btn.place(x=118, y=475)

    output = Text(window, width=75, height=5, wrap=WORD, background="white")
    output.grid(row=12, column=0, columnspan=2, sticky=W)
    output.place(x=0, y=525)
