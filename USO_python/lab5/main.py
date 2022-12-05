from numpy import linspace
from scipy.integrate import odeint
from matplotlib.pyplot import plot, show, xlabel, ylabel, title, grid


def main():
    # parametry ukladu
    L1 = 2
    L2 = 0.5
    R1 = 2
    R2 = 5
    C1 = 0.5

    # nastawy PID
    ku = 75.5
    Tu = 1.85

    kp = 0.6*ku
    ki = 1.2*ku*Tu**-1
    kd = 0.075*ku*Tu

    # ================

    def get_dxdt(x, u):
        x1, x2, x3 = x[0], x[1], x[2]
        dx1dt = -R2/L2 * x1 - 1/L2 * x3
        dx2dt = -R1/L1 * x2 + 1/L1 * x3 + 1/L1 * u
        dx3dt = 1/C1 * x1 - 1/C1 * x2
        return dx1dt, dx2dt, dx3dt

    def model_open_loop(x, t):
        # model
        #
        # u->[ model ]->y
        #

        u = 3

        dx1dt, dx2dt, dx3dt = get_dxdt(x, u)

        dxdt = [dx1dt, dx2dt, dx3dt]
        return dxdt

    def model_pid(x, t):
        # model
        #
        # setpoint->( )--e->[ PID ]--u->[ model ]--.-->y
        #         - /|\                            |
        #            |_____________________________|
        #

        setpoint = 3
        x1, x2, _, integral_e = x

        y = x1
        e = setpoint - y
        dedt = 1/C1 * x1 - 1/C1 * x2

        u = kp*e + ki*integral_e + kd*dedt
        dx1dt, dx2dt, dx3dt = get_dxdt(x, u)

        dxdt = [dx1dt, dx2dt, dx3dt, e]
        return dxdt

    def model_pid_QI(x, t):
        # model
        # taki sam jak w model_pid
        #

        setpoint = 3
        x1, x2, _, integral_e, _, _, _, _, _ = x

        y = x1
        e = setpoint - y
        dedt = 1/C1 * x1 - 1/C1 * x2

        u = kp*e + ki*integral_e + kd*dedt
        dx1dt, dx2dt, dx3dt = get_dxdt(x, u)

        I_ISE = e**2
        I_ITSE = t*I_ISE
        I_IAE = abs(e)
        I_ITAE = t*abs(e)
        I_OPT = I_ISE + u**2

        dxdt = [dx1dt, dx2dt, dx3dt, e, I_ISE, I_ITSE, I_IAE, I_ITAE, I_OPT]
        return dxdt

    def select_model(type):
        if type == "pid":
            return model_pid, [0, 0, 0, 0]
        elif type == "openloop":
            return model_open_loop, [0, 0, 0]
        elif type == "QI":
            return model_pid_QI, [0, 0, 0, 0, 0, 0, 0, 0, 0]
        else:
            return (lambda x, _: x), [0]

    model_type = "QI"
    model, x0 = select_model(model_type)
    t = linspace(0, 15, 200)
    x = odeint(model, x0, t)
    y = x[:, 0]  # i2

    plot(t, y)
    xlabel("t [s]")
    ylabel("i2 [A]")
    title("odpowiedź obiektu")
    grid()
    show()

    if model_type == "QI":
        I_ISE, I_ITSE, I_IAE, I_ITAE, I_OPT = tuple(x[-1, 4:])
        print(
            f"I_ISE = {I_ISE}\nI_ITSE = {I_ITSE}\nI_IAE = {I_IAE}\nI_ITAE = {I_ITAE}\nI_OPT = {I_OPT}")


if __name__ == '__main__':
    main()
