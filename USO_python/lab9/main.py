import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as si
import scipy.linalg as sl
import scipy as s

def main():
    def ex2():
        # parametry wahadla
        J = 1
        m = 9
        g = 9.81
        d = 0.5
        l = 1
        
        # ustawienia symulacji
        t = np.linspace(0, 15, num=500)
        u0 = 0
        u = 0

        # 2.2
        def ex2_1_odefun(x, t):
            x1, x2 = x
            # 2.1
            dx1dt = x2
            dx2dt = 1/J*u- 1/J*d*x2 - 1/J*m*g*l*np.sin(x1)
            return [dx1dt, dx2dt]

        x0_ex2_1 = [np.pi/4, 0]
        x_ex2_1 = si.odeint(ex2_1_odefun, x0_ex2_1, t)

        plt.figure()
        plt.plot(t, x_ex2_1[:, 0], label="x1 (kat)")
        plt.plot(t, x_ex2_1[:, 1], label="x2 (predkosc katowa)")
        plt.title("nieliniowy")
        plt.legend()
        plt.show()

        # 2.3
        x_lin = np.array([np.pi, 0])
        A = np.array([[0, 1], [-m*g*l/J*np.cos(x_lin[0]), -d/J]])
        B = np.array([[0], [1/J]])

        def ex2_3_odefun(x, t):
            x = x.reshape((2,1))
            dxdt = A@x + B*u0
            return dxdt.flatten()
        
        x_ex2_3 = si.odeint(ex2_3_odefun, [np.pi, 0], t)
        plt.figure()
        plt.plot(t, x_ex2_3[:, 0] , label="x1 (kat)")
        plt.plot(t, x_ex2_3[:, 1] , label="x2 (predkosc katowa)")
        plt.title("linearyzacja")
        plt.legend()
        plt.show()

        # 2.4
        Q = np.eye(2,2)
        R = np.array([[1]])
        P = sl.solve_continuous_are(A,B,Q,R)
        K = np.linalg.inv(R)*B.T@P # R^-1 * B^T * P
        print(f'K={K}')

        def ex2_5_odefun(x, t):
            x = x.reshape((2,1))
            uk = -K@(x - x_lin.reshape((2,1))) + u0
            dxdt = A@x+B@uk

            return dxdt.flatten()

        x_ex2_5 = si.odeint(ex2_5_odefun, [np.pi-0.1, 0], t)
        plt.figure()
        plt.plot(t, x_ex2_5[:, 0], label="x1 (kat)")
        plt.plot(t, x_ex2_5[:, 1], label="x2 (predkosc katowa)")
        plt.title("LQR")
        plt.legend()
        plt.show()

        # 2.6
        x0_ex2_6 = [[np.pi-0.1, 0], [np.pi-0.5, 0], [np.pi-1, 0], [np.pi-2, 0], [0, 0]][0] # tu wybrac
        x_ex2_6 = si.odeint(ex2_5_odefun, x0_ex2_6, t)
        plt.figure()
        plt.plot(t, x_ex2_6[:, 0], label="x1 (kat)")
        plt.plot(t, x_ex2_6[:, 1], label="x2 (predkosc katowa)")
        plt.title(f"LQR dla x0={x0_ex2_6}")
        plt.legend()
        plt.show()

        # 2.7
        def ex2_7_riccati_odefun(P, t, Q, R):
            P = np.asarray(P).reshape((2,2))
            return (-(P@A-P@B@np.linalg.inv(R)@B.T+A.T@P+Q)).flatten()

        t_ricc = np.linspace(1, 0, num=100)
        P = si.odeint(ex2_7_riccati_odefun, [1, 0, 0, 1], t_ricc, args=(Q,R))
        Pfun = np.array([s.interpolate.interp1d(t_ricc, P[:, i], fill_value='extrapolate') for i in range(P.shape[1])]).reshape((2,2))

        def ex2_7_odefun(x, t):
            x = x.reshape((2,1))
            P = np.array([[Pfun[i, j](t) for j in range(Pfun.shape[0])] for i in range(Pfun.shape[1])])
            K = np.linalg.inv(R)*B.T@P
            uk = -K@(x - x_lin.reshape((2,1))) + u0
            dxdt = A@x+B@uk
            return dxdt.flatten()

        x_ex2_7 = si.odeint(ex2_7_odefun, x0_ex2_6, t)
        plt.figure()
        plt.plot(t, x_ex2_7[:, 0], label="x1 (kat)")
        plt.plot(t, x_ex2_7[:, 1], label="x2 (predkosc katowa)")
        plt.title(f"LQR ze skonczonym horyzontem t1=1s")
        plt.legend()
        plt.show()

    ex2()

if __name__ == '__main__':
    main()