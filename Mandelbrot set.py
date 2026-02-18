import numpy as np
import matplotlib.pyplot as plt

def mandelbrot_test_a(c, maxiter=100):
    """
    Test if a point c is in the Mandelbrot set.  Return 1 if it is, 0 otherwise.
    """
    z = 0
    for k in range(maxiter):
        z = z**2 + c
        if abs(z) > 2:
            return 0
    return 1
# testing a single point

def mandelbrot_test_b(c, maxiter=100):
    """
    Test if a point c is in the Mandelbrot set.  
    Return an array of zeros and ones values, where one means that the point is in the set.
    """
    z = 0
    for k in range(maxiter):
        z = z**2 + c
    return (abs(z) <= 2) * 1
#the entries in the array z get very large, and will usually cause an overflow error eventually. 

def mandelbrot_test(c, maxiter=100):
    """
    Test if a point c is in the Mandelbrot set.  Return 1 if it is, 0 otherwise.
    The function maps efficiently over numpy arrays.
    """
    z = 0 * c  # array of zeros of the same shape as c
    m = z + 1  # array of ones of the same shape as c
    for k in range(maxiter):
        # Throughout this loop, m is an array of 1s and 0s and z is an array of complex numbers
        # An entry in m is 1 if the iteration starting with the corresponding c has 
        # not yet escaped from the circle of radius 2, and 0 otherwise.
        # The corresponding entry in z is the current value of the iteration if m = 1,
        # and 10 if m = 0.
        z = m * (z**2 + c) + 10 * (1 - m)
        m = (abs(z) <= 2)*1
    return m
# set cs to be an 1000 × 1000 matrix of evenly spaced points in C

n = 1000
xs = np.linspace(-2.0, 0.4, n+1).reshape(1, n+1) # row vector of real parts
ys = np.linspace(-1.2, 1.2, n+1).reshape(n+1, 1) # column vector of imaginary parts
cs = xs + 1j*ys # broadcast sum gives a matrix of complex numbers
ms = mandelbrot_test(cs, 100)
plt.imshow(ms, extent=(-2, 2, -2, 2), cmap='Purples')
