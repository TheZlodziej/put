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
    t_start = 0
    t_end = 1
    x_t_start = 1
    x_t_end = 3

    def model(_, t, a0, a1, a2, a3):
        xt = a0 + a1*t + a2*t**2 + a3*t**3
        dxt_dt = a1 + 2*a2*t + 3*a3*t**2
        dJ_dt = 24*xt + 2*dxt_dt**2 - 4*t
        return dJ_dt

    def problem_dyn(a):
        t = linspace(t_start, t_end)
        int_0t_J = odeint(model, [0], t, args=a)
        return int_0t_J[-1][0]
        
    def min_a(a):
        return problem_dyn((a[0], a[1], a[2], a[3]))
    
    a_cstr = [
        {
            "type": "eq",
            "fun": lambda a: a[0] + a[1]*t_start + a[2]*t_start**2 + a[3]*t_start**3 - x_t_start # = 0
        },
        {
            "type": "eq",
            "fun": lambda a: a[0] + a[1]*t_end + a[2]*t_end**2 + a[3]*t_end**3 - x_t_end # = 0
        }
    ]

    a0 = [0, 0, 0, 0]
    res = minimize(min_a, a0, constraints=a_cstr, options={"disp":True})
    if res.success:
        print(f"rozw={res.x}")
    else:
        print("nie tym razem")


if __name__ == '__main__':
    # ex2()
    # ex3()
    ex4()
