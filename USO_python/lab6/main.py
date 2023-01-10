from numpy import array, linspace, asarray, eye, append
from scipy.integrate import odeint
from scipy.linalg import solve_continuous_are, inv
from scipy.interpolate import interp1d
from matplotlib.pyplot import plot, figure, show, legend

def main():
    # parametry modelu
    params = dict(R=0.5, L=0.2, C=0.5)

    # model
    A = array([
        [0, 1], 
        [-1/params['L']/params['C'], -params['R']/params['L']]
    ])

    B = array([
        [0],
        [1/params['L']]
    ])

    def ex2():
        # odeint fun (2.2)
        def model_odeint_2_2(x, t, v):
            x = asarray(x).reshape((2,1))
            u = v
            return A@x+B@u

        # odeint fun (2.4)
        def model_odeint_2_4(x, t, K):
            x = asarray(x).reshape((2,1))
            u = -K@x
            return A@x+B@u

        # odeint fun (2.6)
        def model_odeint_2_6(x, t, K, R):
            x = (asarray(x)[0:-1]).reshape((2,1))
            u = -K@x
            dxdt = A@x+B@u
            dJdt = x.T@Q@x+u.T@R@u
            return append(dxdt, dJdt)

        # 2.1
        Q = eye(2,2)
        R = array([[1]])
        P = solve_continuous_are(A,B,Q,R)
        K = inv(R)*B.T@P # R^-1 * B^T * P
        print(f'K={K}')

        # 2.3
        t = linspace(0, 15, num=200)
        x0 = [0, 0]
        x = odeint(model_odeint_2_2, x0, t, args=([1],))
        
        # 2.4
        x0 = [1, 0]
        x_2_4 = odeint(model_odeint_2_4, x0, t, args=(K,)) 
        # figure()
        # plot(t, x_2_4[:, 0])
        # show()

        # 2.5
        # x0 = [1, 2]
        # x_2_5 = odeint(model_odeint_2_4, x0, t, args=(K,)) 
        # figure()
        # plot(t, x_2_5[:, 0])
        # show()        

        # 2.6
        x0 = [0, 1, 0]
        x_2_6 = odeint(model_odeint_2_6, x0, t, args=(K,R))
        J = x_2_6[-1, 2]
        print(f'J={J}')
        # figure()
        # plot(t, x_2_6[:, 0], label='x1')
        # plot(t, x_2_6[:, 2], label='J')
        # legend()
        # show()

    def ex3():

        # rikati
        def ric_odeint(P, t, Q, R):
            P = asarray(P).reshape((2,2))
            return (-(P@A-P@B@inv(R)@B.T+A.T@P+Q)).flatten()

        # parametry regulatora
        Q = eye(2,2)
        R = array([[1]])
        
        # sym
        t1 = 5 # s 
        t = linspace(t1, 0, num=500)
        Pt1 = [1, 0, 0, 1] # S
        P = odeint(ric_odeint, Pt1, t, args=(Q,R))
            
        # plotowanie macierzy P (3.2)
        # figure()
        # plot(t, P[:,0], label="P00")
        # plot(t, P[:,1], label="P01")
        # plot(t, P[:,2], label="P10")
        # plot(t, P[:,3], label="P11")
        # legend()
        # show()

        # funkcja macierzy P (interpolacja)
        Pfun = array([interp1d(t, P[:, i], fill_value='extrapolate') for i in range(P.shape[1])]).reshape((2,2))
        
        # odeint fun 3.4 
        def model_odeint_3_4(x, t, Pfun, R):
            x = asarray(x).reshape((2, 1))
            P = array([[Pfun[i, j](t) for j in range(Pfun.shape[0])] for i in range(Pfun.shape[1])])
            K = inv(R)*B.T@P
            ud = 1 # skok
            u = -K@x + ud
            return (A@x+B*u).flatten()

        x0 = [10, 0]
        t = linspace(0, 15, num=200)
        x = odeint(model_odeint_3_4, x0, t, args=(Pfun, R))

        # wykres odp skokowej (3.6)
        # figure()
        # plot(t, x[:, 0], label="x1")
        # plot(t, x[:, 1], label="x2")
        # legend()
        # show()

        # 3.7
        def model_odeint_3_7(x, t, Pfun, R):
            x = (asarray(x)[0:-1]).reshape((2,1))

            P = array([[Pfun[i, j](t) for j in range(Pfun.shape[0])] for i in range(Pfun.shape[1])])
            K = inv(R)*B.T@P
    
            ud = 1
            u = -K@x + ud
            
            dxdt = A@x+B@u
            dJdt = x.T@Q@x+u.T@R@u
            return append(dxdt.flatten(), dJdt)

        # obliczanie wskaznika jakosci
        x0 = append(x0, 0)
        J = odeint(model_odeint_3_7, x0, t, args=(Pfun, R))[:, -1][-1]
        print(f"J={J}")
        # to nie jest minimalna wartosc wskaznika bo rozwazania byly dla wejscia 0 a teraz nie jest
        # horyzont no to zalezy od t (jest na 15 sek ustawione)

    def ex4():
        def model_odeint_4_1(x, t, K):
            x = asarray(x).reshape((2,1))
            qd = 5
            xd = array([[qd], [0]])
            
            e = xd - x
            u = -(-K@e) + B.T@xd #1/params['C']*qd

            dxdt = A@x + B@u
            return dxdt.flatten()

        # wyznaczanie K, R
        Q = eye(2,2)
        R = array([[1]])
        P = solve_continuous_are(A,B,Q,R)
        K = inv(R)*B.T@P # R^-1 * B^T * P
        print(f'K={K}')

        # 4.5
        t = linspace(0, 15, num=200)
        x0 = [0, 0]
        x_4_5 = odeint(model_odeint_4_1, x0, t, args=(K,))

        figure()
        plot(t, x_4_5[:, 0], label='x1')
        plot(t, x_4_5[:, 1], label='x2')
        legend()
        show()
    
    # wykresy sa zakomentowane
    #ex2()
    #ex3()
    ex4()

if __name__ == '__main__':
    main()