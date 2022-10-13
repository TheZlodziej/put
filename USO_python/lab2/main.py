from scipy.integrate import solve_ivp
from scipy.signal import step, TransferFunction, StateSpace, impulse, tf2ss, ss2tf
from matplotlib import pyplot as plt
from numpy import arange

#2.2
kp = 10
T = 2
A = -1/T
B = kp/T
C = 1
D = 0

def ex2_model_dydt(t, y): # ret y'
    #2.6
    return kp/T - y/T

def ex2():
    #2.3
    tf = TransferFunction(kp, [T, 1])

    #2.4
    t, y = step(tf)
    plt.plot(t, y)
    plt.show() # tak, odpowiada

    #2.5
    sys = StateSpace(A, B, C, D)
    t, y = step(sys)
    plt.plot(t, y)
    plt.show() # taka sama jak wczesniej

    #2.7
    t = arange(0, 15, 0.01)

    #2.8
    sol = solve_ivp(ex2_model_dydt, [0, 15], [0], dense_output=True)

    #2.9
    plt.plot(t, sol.sol(t).T)
    plt.show() # taka sama

    #2.10
    # wszystkie sa takie same

###############################################
L = 1 # H
R = 12 # Ohm
C = 100 * 10e-6 # F

def ex3():
    #3.1
    num = [1, 0]
    den = [L, R, 1/C]
    tf = TransferFunction(num, den)

    #3.2 skokowa
    t, y = step(tf)
    plt.plot(t, y)
    plt.show()

    #3.2 impulsowa
    t, y = impulse(tf)
    plt.plot(t, y)
    plt.show()

    # nie pokrywaja sie bo czemu by mialy

    #3.3
    sys = tf2ss(num, den)

    a = [[0, 1], [-1/L/C, -R/L]]
    b = [[0], [1/L]]
    c = [0, 1]
    d = 0
    tf = ss2tf(a,b,c,d)
    
    print(sys, tf)

    #3.4
    L = 0.15 # H

    sys = tf2ss(num, den) # tf - takie samo, zmienne stanu rozne

    a = [[0, 1], [-1/L/C, -R/L]]
    b = [[0], [1/L]]
    c = [0, 1]
    d = 0
    tf = ss2tf(a, b, c, d)

    print(sys, tf) # tf - takie samo, zmienne stanu rozne

if __name__ == "__main__":
    # ex2()
    ex3()