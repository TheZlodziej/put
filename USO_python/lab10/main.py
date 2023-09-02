import numpy as np
import scipy.integrate as si
import scipy.linalg as sa
import scipy.interpolate as sip
import matplotlib.pyplot as plt

def main():
    d = 0.5
    J = 1
    m = 9 
    g = 9.81
    l = 1

    def ex1():
        def ex1_1_odefun(x, t, u):
            x1, x2 = x
            dx1dt = x2
            dx2dt = -d/J*x2+m*g*l*np.sin(x1)+1/J*u
            return [dx1dt, dx2dt]

        # sym 1.1
        x1_1_lin_pt = [np.pi, 0]
        t1_1 = np.linspace(0, 10, num=200)
        x1_1 = si.odeint(ex1_1_odefun, [x1_1_lin_pt[0] + np.pi/4, 0], t1_1, args=(0,))
        
        plt.figure()
        plt.plot(t1_1, x1_1[:, 0] - x1_1_lin_pt[0], label="x1")
        plt.plot(t1_1, x1_1[:, 1] - x1_1_lin_pt[1], label="x2")
        plt.legend()
        plt.title("1.1 odp ukladu")
        plt.show()
    
    def ex2():
        def A(x):
            x1, _ = x
            return np.array([[0, 1], [m*g*l*np.sin(x1)/x1, -d/J]])

        def B(x):
            return np.array([[0], [1/J]])

        def K(x, Q, R):
            At = A(x)
            Bt = B(x)
            P = sa.solve_continuous_are(At, Bt, Q, R)
            K = np.linalg.inv(R)*Bt.T@P # R^-1 * B^T * P
            return K

        def ex2_1_odefun(x, t, u, Q, R, mod22):
            if mod22:
                Q = np.array([[x[0]**2, 0], [0, x[1]**2]]) # modyfikacja 2.3
            u = -K(x, Q, R)@(x.reshape((2,1)))
            x1, x2 = x
            dx1dt = x2
            dx2dt = -d/J*x2+m*g*l*np.sin(x1)+1/J*u
            return [dx1dt, dx2dt]

        Q2_1 = np.eye(2,2)
        R2_1 = np.array([[1]])

        u2_1 = np.pi/4
        t2_1 = np.linspace(0, 5, num=200)
        x2_1 = si.odeint(ex2_1_odefun, [2*np.pi, 0], t2_1, args=(u2_1, Q2_1, R2_1, False))

        x2_2 = si.odeint(ex2_1_odefun, [2*np.pi, 0], t2_1, args=(u2_1, Q2_1, R2_1, True))

        # plt.figure()

        # plt.subplot(2,1,1)
        # plt.plot(t2_1, x2_1[:, 0], label="x1")
        # plt.plot(t2_1, x2_1[:, 1], label="x2")
        # plt.title("2.2 odp ukladu")
        # plt.legend()

        # plt.subplot(2,1,2)
        # plt.plot(t2_1, x2_2[:, 0], label="x1")
        # plt.plot(t2_1, x2_2[:, 1], label="x2")
        # plt.title("2.3 odp ukladu po modyfikacji Q")
        # plt.legend()
        # plt.show()

        # SKONCZONY HORYZONT
        def K_finite(x, Q, R, ti):
            At = A(x)
            Bt = B(x)

            def ric_odeint(P, t, Q, R):
                P = np.asarray(P).reshape((2,2))
                return (-(P@At-P@Bt@np.linalg.inv(R)@Bt.T+At.T@P+Q)).flatten()
           
            # if ti - 0.001 < 0:
            #     ti = 0.001

            tp = np.linspace(5-ti, 0, num=200)
            Pt1 = [1, 0, 0, 1] # S
            P = (si.odeint(ric_odeint, Pt1, tp, args=(Q,R))[-1, :]).reshape((2,2))

            # Pfun = np.array([sip.interp1d(tp, P[:, -i], fill_value='extrapolate') for i in range(P.shape[1])]).reshape((2,2))
            # P = np.array([[Pfun[i, j](ti) for j in range(Pfun.shape[0])] for i in range(Pfun.shape[1])])
            K = np.linalg.inv(R)*Bt.T@P # R^-1 * B^T * P
            return K

        def ex2_4_odefun(x, t, u, Q, R, mod22):
            if mod22:
                Q = np.array([[x[0]**2, 0], [0, x[1]**2]]) # modyfikacja 2.3
            Kt = K_finite(x, Q, R, t)
            u = -Kt@(x.reshape((2,1)))

            x1, x2 = x
            dx1dt = x2
            dx2dt = -d/J*x2+m*g*l*np.sin(x1)+1/J*u
            return [dx1dt, dx2dt]

        t2_4 = np.linspace(0, 5, num=200)
        x2_4 = si.odeint(ex2_4_odefun, [2*np.pi, 0], t2_4, args=(0, Q2_1, R2_1, False))

        plt.figure()
        plt.plot(t2_4, x2_4[:, 0], label="x1")
        plt.plot(t2_4, x2_4[:, 1], label="x2")
        plt.title("2.4 odp ukladu")
        plt.legend()
        plt.show()
    #ex1()
    ex2()

if __name__== '__main__':
    main()