from scipy.optimize import minimize
from numpy import Inf

def ex2():
    def f(xy):
        return xy[1] # bez minusa bo uzywamy minimize [-y -> max = y -> min]

    # start
    xy_start = [0,0]

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

    result = minimize(f, xy_start, options={"disp":True}, constraints=cstr)
    if result.success:
        print(f"rozw={result.x}")
    else:
        print("nie tym razem")

def ex3():
    def f(x):
        return x**4 - 4*x**3 - 2*x**2 + 12*x + 9
    
    # start
    x_strart = [0]

    # bounds
    bds = (0, Inf)

    result = minimize(f, x_strart, options={"disp":True}, bounds=bds)
    if result.success:
        print(f"rozw={result.x}")
    else:
        print("nie tym razem")
        
if __name__ == '__main__':
    # ex2()
    ex3()