from scipy.optimize import minimize

def f(xy):
    return xy[1] # bez minusa bo uzywamy minimize [-y -> max = y -> min]

# start
xy_start = [0,0]

# constrains
def cstr_fun(xy):
    x = xy[0]
    y = xy[1]

    return (-2*x + y + 4) and ()

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