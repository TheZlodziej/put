from scipy.optimize import minimize, LinearConstraint, minimize_scalar
from scipy.integrate import odeint
from numpy import linspace, eye
import numpy as np
import math


def ex2():
    def f2(xy):
        return xy[1]  # bez minusa bo uzywamy minimize [-y -> max = y -> min]

    # start
    xy_start = [0, 0]

    # constrains
    cstr = [
        {
            'type': 'ineq',
            'fun': lambda xy: (xy[0] + xy[1] - 3)
        },
        {
            'type': 'ineq',
            'fun': lambda xy: (-2*xy[0] + xy[1] + 4)
        },
        {
            'type': 'ineq',
            'fun': lambda xy: (xy[1] + 4*xy[0] + 2)
        }
    ]

    result = minimize(f2, xy_start, options={"disp": True}, constraints=cstr)
    if result.success:
        print(f"rozw={result.x}")
    else:
        print("nie tym razem")


def ex3():
    def f3(x):
        return x**4 - 4*x**3 - 2*x**2 + 12*x + 9
    # init. cond.
    x0 = [0]

    # bounds
    bds = [(0, None)]

    # method
    mth = 'Powell'

    result = minimize(f3, x0, bounds=bds,  method=mth, options={
                      'disp': True})

    if result.success:
        print(f"rozw={result.x}")
    else:
        print("nie tym razem")


def ex4():
    def model(y, t, a0, a1, a2, a3):
        return a0 + a1*t + a2*t**2 + a3*t**3

    def problem_dyn(a):
        t = linspace(0, 1)
        xt = odeint(model, [0], t, args=a)
        return xt[-1][0]

    A = (1, 0, 0, 0)

    end_of_interval = problem_dyn(A)
    print(end_of_interval)

    cstr = LinearConstraint(eye(4), 1, 3)
    a0 = [0, 0, 0, 0]
    result = minimize(model, x0=a0, args=A, constraints=cstr,
                      method='trust-constr')


if __name__ == '__main__':
    # ex2()
    ex3()
    # ex4()
