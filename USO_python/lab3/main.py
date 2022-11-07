import numpy as np
import pprint

pp = pprint.PrettyPrinter()


def get_kalman_matrix(A, B):
    # returns K = [B AB A^2*B ... A^n-1*B]
    n = np.size(A, 0)
    K = np.zeros([n, n])
    for i in range(n):
        K[:, i] = np.matmul(np.linalg.matrix_power(A, i), B)
    return K


def kalman_is_steerable(A, B):
    # returns True if rank of kalman matrix is the same as A's rows
    n = np.size(A, 0)
    return n == np.linalg.matrix_rank(get_kalman_matrix(A, B))


def ex1():
    # 1.1
    # Rys. 1.
    # R = 2 Ohm
    # C = 1 F
    # x' = [[-1/2/C/R, 0], [0, -1/2/C/R]]*x + [[1/2/C/R], [1/2/C/R]]*u
    #
    # Rys. 2.
    # R = 1 Ohm
    # C = 1 F
    # x' = [[-1/R/C, 0, 0], [0, -1/2/R/C, 0], [0, 0, -1/3/R/C]]*x + [[1/R/C], [1/2/R/C], [1/3/R/C]]*u
    #
    # Rys. 3.
    # x' = 0
    #
    # Rys. 4.
    # R1 = 2 Ohm,
    # R2 = 1 Ohm,
    # L1 = 0.5 H,
    # L2 = 1 H,
    # C = 2 F
    # x' = [[-R1/L1, 0, -1/L1], [0, R2/L2, 0], [1, -1, -1/R2]]*x + [[1/L1], [0], [0]]*u

    t = np.linspace(0, 50, num=1000)
    u = 5 * np.sin(t)

    def ex1_1():
        # const.
        R = 2  # Ohm
        C = 1  # F

        # x' = Ax + Bu
        A = np.array([[-1/2/C/R, 0], [0, -1/2/C/R]])
        B = np.array([1/2/C/R, 1/2/C/R]).T

        K = get_kalman_matrix(A, B)
        print(f'1.1 sterowalna = {kalman_is_steerable(A, B)}\nmacierz = ')
        pp.pprint(K)
        print()

    def ex1_2():
        # const.
        R = 1  # Ohm
        C = 1  # F

        # x' = Ax + Bu
        A = np.array([[-1/R/C, 0, 0], [0, -1/2/R/C, 0], [0, 0, -1/3/R/C]])
        B = np.array([1/R/C, 1/2/R/C, 1/3/R/C]).T

        K = get_kalman_matrix(A, B)
        print(f'1.2 sterowalna = {kalman_is_steerable(A, B)}\nmacierz =')
        pp.pprint(K)
        print()

    def ex1_3():
        # x' = Ax + Bu
        A = np.array([[0]])
        B = np.array([[0]])

        K = get_kalman_matrix(A, B)
        print(f'1.3 sterowalna = {kalman_is_steerable(A, B)}\nmacierz =')
        pp.pprint(K)
        print()

    def ex1_4():
        # const.
        R1 = 2  # Ohm,
        R2 = 1  # Ohm,
        L1 = 0.5  # H,
        L2 = 1  # H,
        C = 2  # F

        # x' = Ax + Bu
        A = np.array([[-R1/L1, 0, -1/L1], [0, R2/L2, 0], [1, -1, -1/R2]])
        B = np.array([1/L1, 0, 0]).T

        K = get_kalman_matrix(A, B)
        print(f'1.4 sterowalna = {kalman_is_steerable(A, B)}\nmacierz =')
        pp.pprint(K)
        print()

    ex1_1()
    ex1_2()
    ex1_3()
    ex1_4()


if __name__ == "__main__":
    # A = np.array([[0, 2, -3], [1, 0, -2], [0, 1, 0]])
    # B = np.array([1, 0, 0]).T
    # steerable = kalman_is_steerable(A, B)
    # print(steerable)
    ex1()
