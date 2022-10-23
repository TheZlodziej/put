import numpy as np

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
    pass

if __name__ == "__main__":
    A = np.array([[0, 2, -3], [1, 0, -2], [0, 1, 0]])
    B = np.array([1, 0, 0]).T
    steerable = kalman_is_steerable(A, B)

    print(steerable)