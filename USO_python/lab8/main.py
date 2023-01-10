import numpy as np
import scipy.integrate as si
import matplotlib.pyplot as plt
import scipy.signal as ss
import control as ctrl

def main():
    def ex2():
        def ex2_1_odeint(z, t):
            z1, z2 = z
            u=1
            dz1dt = z1*np.log(z2)
            dz2dt=-z2*np.log(z1)+z2*u
            return [dz1dt, dz2dt]

        def ex2_2_odeint(x, t):
            x1, x2 = x
            u=1
            dx1dt = x2
            dx2dt = -x1+u
            return [dx1dt, dx2dt]


        t = np.linspace(0, 15, num=200)
        
        #2.1
        x21 = si.odeint(ex2_1_odeint, [1, 1], t)
        plt.figure()
        plt.subplot(3,1,1)
        plt.plot(t, x21[:, 0], label="z1")
        plt.plot(t, x21[:, 1], label="z2")
        plt.legend()
        #plt.show()

        #2.2
        x22 = si.odeint(ex2_2_odeint, [0, 0], t) #2.4 -> x0 = ln(z0) = [0, 0]
        plt.subplot(3,1,2)
        plt.plot(t, x22[:, 0], label="x1")
        plt.plot(t, x22[:, 1], label="x2")
        plt.legend()
        #plt.show()
        # nie jest to samo bo to inny uklad wspolrzednych (znaczy no jest ale w innym ukladzie)

        #2.5
        x26 = np.exp(x22)
        plt.subplot(3,1,3)
        plt.plot(t, x26[:, 0], label="exp(x1)")
        plt.plot(t, x26[:, 1], label="exp(x2)")
        plt.legend()
        plt.show()
        # pokrywaja sie obie zmienne stanu

    def ex5():
        # parametry obiektu
        J = 1 # kg*m^2
        g = 10 # m/s^2
        R = 1 # m
        m = 9 # kg
        d = 0.5 # Nm*s^2/rad^2

        # wymuszenie
        u_idx = 0
        u = [0, 5, 20, 45*np.sqrt(2), 70][u_idx]
        # u = 0
        
        def ex5_1_odeint(x, t):
            x1, x2 = x
            dx1dt = x2
            dx2dt = 1/J*u-d/J*x2-m*g/J*R*np.sin(x1)
            return [dx1dt, dx2dt]

        t = np.linspace(0, 15, num=200)

        # 5.1
        x51 = si.odeint(ex5_1_odeint, [0, 0], t) # u = 0 tutaj
        plt.subplot(2,1,1)
        plt.plot(t, x51[:, 0], label="x1")
        plt.plot(t, x51[:, 1], label="x2")
        plt.legend()

        # 5.2
        x0 = [np.pi/4, 0]
        u0 = np.sqrt(2)*45

        A = np.array([[0, 1], [-m*g*R/J*np.cos(x0[0]), -d/J]])
        B = np.array([[0], [1/J]])
        #C = np.array([[1, 0]])
        #D = 0
        
        # 5.4
        print(f"sterowalny={np.linalg.matrix_rank(ctrl.ctrb(A,B)) == np.linalg.matrix_rank(A)}")

        def ex5_2_odeint(x,t):
            x = x.reshape((2,1))
            dxdt = A@x+B*(u+u0)
            return dxdt.flatten()

        #sys = ss.StateSpace(A,B,C,D)
        #_, _, x52 = ss.lsim2(sys, np.ones_like(t)*u+u0, t, x0)
        x52 = si.odeint(ex5_2_odeint, [0,0], t)

        plt.subplot(2,1,2)
        plt.plot(t, x52[:, 0] + x0[0], label="x1 (lin)")
        plt.plot(t, x52[:, 1] + x0[1], label="x2 (lin)")
        plt.legend()
        plt.show()
        # nie wiem o co chodzi w tym podpunkcie juz

        # 5.7
        u = 0
        x0_5_7 = [np.pi/4, 0] # [0, 0]
        x57 = si.odeint(ex5_1_odeint, x0_5_7, t)
        plt.subplot(2, 1, 1)
        plt.plot(t, x57[:, 0], label="x1")
        plt.plot(t, x57[:, 1], label="x2")
        plt.legend()

        # 5.8
        def x_to_SDC_AB(x):
            x1, _ = x
            A = np.array([[0, 1], [-m*g*R/J*np.sin(x1)/x1, -d/J]])
            B = np.array([[0], [1/J]])
            return A, B

        # 5.9
        def ex5_9_odeint(x, t):
            A, B = x_to_SDC_AB(x)
            x = x.reshape((2,1))
            return (A@x+B*u).flatten()

        x59 = si.odeint(ex5_9_odeint, x0_5_7, t)
        plt.subplot(2, 1, 2)
        plt.plot(t, x59[:, 0], label="x1 SDC")
        plt.plot(t, x59[:, 1], label="x2 SDC")
        plt.legend()
        plt.show()

        # Uzyskane wykresy pokrywają się
        # Na przykład problemem może być dzielenie przez 0 przy liczeniu macierzy jak x0=0 (jak w 5.10)
        # Linearyzacja to dalej przyblizenie wiec moze blad wystepowac

    #ex2()
    ex5()
if __name__ == '__main__':
    main()