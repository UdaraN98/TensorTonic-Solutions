import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """

    A = np.array(A)
    # take the dimensions
    m,n = A.shape

    # create a zero matrix for A_T
    A_T = np.zeros((n,m))

    # looping though the items in A and assigning

    for i in range(len(A)):
        for j in range(len(A[i])):
            A_T[j][i] = A[i][j]


    # return the A_T

    return A_T
