import numpy as np
from matplotlib import pyplot as plt


def ex21():
    x1 = 3 ** 15 - 5
    x2 = np.array([2, 0.5]).T \
        * np.array([[1, 4], [-1, 3]]) \
        * np.array([-1, 3]).T
    x3 = np.linalg.solve(np.array([[1, 2], [-1, 0]]), np.array([-1, 2]).T)
    print("[2.1] x1, x2, x3", x1, x2, x3, sep='\n')


def ex22():
    coeffs = [1, 1, -129, 171, 1620]
    x = [46, 14]
    print("[2.2]\ty(x=46, x=14)", np.polyval(coeffs, x))


def ex31():
    coeffs = [1, 1, -129, 171, 1620]
    x = range(-46, 14)
    y = np.polyval(coeffs, x)
    print("[3.1]\tmin, max", min(y), max(y))


def ex32():
    coeffs = [1, 1, -129, 171, 1620]
    dx = 0.01
    x = np.arange(-46, 14, dx)
    y = np.polyval(coeffs, x)
    maxs = []
    mins = []
    for i in range(1, len(y)-1):
        if y[i] > y[i+1] and y[i] > y[i-1]:
            maxs.append(y[i])
        elif y[i] < y[i+1] and y[i] < y[i-1]:
            mins.append(y[i])
    print(f"[3.2]\tmaksyma {maxs}, minima {mins}")


def ex41(coeffs, min, max, dx):  # find max in min in given range of poly fun given by coeffs
    x = np.arange(min, max, dx)
    y = np.polyval(coeffs, x)
    maxs = []
    mins = []
    for i in range(1, len(y)-1):
        if y[i] > y[i+1] and y[i] > y[i-1]:
            maxs.append(y[i])
        elif y[i] < y[i+1] and y[i] < y[i-1]:
            mins.append(y[i])
    return [maxs, mins]


def ex42(coeffs, min, max, dx):  # was supposed to be for any coeffs length but ex41 already is
    return ex41(coeffs, min, max, dx)


def ex51(coeffs, min, max, dx):
    x = np.arange(min, max, dx)
    y = np.polyval(coeffs, x)
    plt.plot(x, y)
    plt.show()


def ex52(coeffs, min, max, dx):
    x = np.arange(min, max, dx)
    y = np.polyval(coeffs, x)
    plt.plot(x, y, 'r*', label='x(i)')
    plt.xlim([min, max])
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.title('przebieg f w [min, max]')
    plt.show()


if __name__ == '__main__':
    ex21()
    ex22()
    ex31()
    ex32()
    print("[4.1]\t[maksyma, minima]", ex41(
        [1, 1, -129, 171, 1620], -46, 14, 0.01))
    print("[4.2]\t[maksyma, minima]", ex41(
        [1, 1, -129], -46, 14, 0.01))
    ex51([1, 1, -129, 171, 1620], -46, 14, 0.01)
    ex52([1, 1, -129, 171, 1620], -46, 14, 0.01)
