def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # function to get the gradient f`(x) = 2ax + b
    def gradient(a,b,x):
        grad = 2*a*x + b
        return grad

    # loop untill the total steps = steps while updating the x value

    for _ in range(steps):
        x_i = x0 - lr*gradient(a,b,x0) # update x = x - lr.f`(x)
        x0 = x_i


    return x_i
        
        