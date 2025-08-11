from code import interact
import numpy as np
import matplotlib.pyplot as plt
import math

def linear(w,x,b):
    return w*x + b

def logistic(z):
    return 1/(1+math.e**(-z))

def plt_logistic(a, b):
    x = np.linspace(-20,20, 100)
    h = linear(a,x,b)
    y = logistic(h)
    plt.ylim(-5,5)
    plt.xlim(-5,5)
    plt.plot(x,h)
    plt.plot(x,y)
    plt.grid()
    plt.show()

interact(plt_logistic, a = (-10,10,0.1), b = (-10,10,0.1))
while True: linear()