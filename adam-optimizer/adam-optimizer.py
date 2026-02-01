import numpy as np

def adam_step(param, grad, m, v, t, lr=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
    """
    One Adam optimizer update step.
    Return (param_new, m_new, v_new).
    """
    mt = beta1*m + (1-beta1)*grad
    vt = beta2*v + (1-beta2)*(grad**2)
    mhatt = mt/(1-(beta1**t))
    vhat = vt/(1-(beta2**t))

    update = lr*(mhatt/(np.sqrt(vhat)+eps))
    param_new = param - update

    return (param_new, mt, vt) 