import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    x = np.asarray(x)
    out = 1/(1+ np.exp(-x))


    return out
