from scipy.integrate import solve_ivp
from scipy.signal import step, TransferFunction, StateSpace, impulse, tf2ss, ss2tf, lsim2, bode
from matplotlib import pyplot as plt
from numpy import arange, linspace

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
    plt.figure()

    plt.plot(t, y)
    # plt.show() # tak, odpowiada

    #2.5
    sys = StateSpace(A, B, C, D)
    t, y = step(sys)
    plt.plot(t, y)
    # plt.show() # taka sama jak wczesniej

    #2.7
    t = arange(0, 15, 0.01)

    #2.8
    sol = solve_ivp(ex2_model_dydt, [min(t), max(t)], [0], dense_output=True)

    #2.9
    plt.plot(t, sol.sol(t).T)
    plt.legend(["1", "2", "3"])
    plt.show() # taka sama

    #2.10
    # wszystkie sa takie same

###############################################

def ex3():
    L = 1 # H
    R = 12 # Ohm
    C = 100 * 10e-6 # F
    
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

def ex4():
    #4.1 na kartce, nizrj implementacja
    m = 1 # kg
    L = 0.5 # kg
    d = 0.1 # Nms
    J = 1/3*m*L**2

    A = [[0, 1], [0, -d/J]]
    B = [[0], [1/J]]
    C = [1, 0]
    D = 0

    sys = StateSpace(A, B, C, D)

    #4.2
    t, y = step(sys)
    plt.plot(t, y)
    plt.show()
    # odpowiedz skokowa - charakter calkujacy z inercja - kreci sie ze stala predkoscia
    
    #4.3
    t = linspace(0, 100) # liniowo narastajacy

    u1 = 1.2 * t
    tout, yout, _ = lsim2(sys, U=u1, T=t)
    plt.plot(tout, yout)
    plt.show()

    u2 = -1.2 * t
    tout, yout, _ = lsim2(sys, U=u2, T=t)
    plt.plot(tout, yout)
    plt.show()

    # widac tam ze coraz szybciej sie obraca a to czy u mialo a>0 definiuje kierunek obrotu

    #4.4
    w, mag, phase = bode(sys)
    plt.figure()
    plt.subplot(1,2,1)
    plt.semilogx(w, mag)
    plt.subplot(1,2,2)
    plt.semilogx(w, phase)
    plt.show()

    # jak najbardziej, zgadza się

if __name__ == "__main__":
    #ex2()
    #ex3()
    ex4()