from numpy import linspace, power, sqrt, clip
from scipy.integrate import odeint
from matplotlib.pyplot import plot, figure, show, title, legend


def main():
    def ex2():
        def odeint_model(_, t):
            return t**2

        t = linspace(0, 10, num=200)
        y0 = [0]
        y_odeint = odeint(odeint_model, y0, t)

        y_anal = 1/3 * power(t, 3) + 0  # c = 0

        # draw result
        figure()
        plot(t, y_odeint, label="odeint")
        plot(t, y_anal, label="analityczna")
        legend()
        show()

        # odp 2.4 - oba rozwiazania pokrywaja sie

        # nwm o co chodzi z tym nizej
        # Jaki rodzaj numerycznego wyznaczania rozwiazania rownania rozniczkowego zostal uzyty?

    def ex3():
        def odeint_model(x, t):
            # parametry modelu
            kp = 2
            w = 4
            ksi = 0.25

            # wymuszenie
            u = 1

            # stan
            x1, x2 = x
            dx1dt = x2
            dx2dt = -2*ksi/w * x2 - 1/w * sqrt(x1) + kp/w * u

            return [dx1dt, dx2dt]

        t = linspace(0, 150, num=500)
        x0 = [0, 0]
        x = odeint(odeint_model, x0, t)
        y = x[:, 0]

        figure()
        plot(t, y, label="y(t)")
        title("odpowiedz skokowa obiektu")
        legend()
        show()

        # odp 3.5 odpowiedz ma charakter oscylacyjny

    def ex4():
        # parametry obiektu
        kp = 2
        T = 2
        k_ob = 4

        def feedback(x, t, z):
            # model
            # z-->( )--e->[kp]-->[saturation]--u-->[plant]--.-->y
            #   - /|\                                       |
            #      |________________________________________|
            #

            # uchyb
            yt = x[-1]
            et = z - yt

            # u(t) zalezne od tego czy saturacja jest on/off
            ut = kp*et
            # ut = clip(kp*et, -0.1, 0.1)  # blok saturacji

            # stan
            # x' = -1/k_ob*x + 1*u
            dxdt = -1/k_ob*x + 1*ut

            return dxdt

        t = linspace(0, 15, num=2000)
        x0 = 0
        xz1 = odeint(feedback, x0, t, args=(1,))
        xz2 = odeint(feedback, x0, t, args=(2,))
        xz3 = odeint(feedback, x0, t, args=(3,))

        # y = k_ob/T*x
        yz1 = k_ob/T * xz1
        yz2 = k_ob/T * xz2
        yz3 = k_ob/T * xz3

        # wyswietlanie
        figure()
        plot(t, yz1, label='z = 1')
        plot(t, yz2, label='z = 2')
        plot(t, yz3, label='z = 3')
        legend()
        show()

    # ex2()
    # ex3()
    ex4()


if __name__ == '__main__':
    main()
