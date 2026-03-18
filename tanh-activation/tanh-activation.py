import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    x = np.array(x)

    # take the positive and nexagive exponentials
    e_x = np.exp(x) # e^x
    e_n_x = np.exp(-x) # e^-x

    return (e_x-e_n_x)/(e_x+e_n_x)