import math
import numpy as np
import matplotlib.pyplot as plt

def stirling(n):
    """Return Stirling's approximation for n!"""
    return np.sqrt(2*np.pi)* n**(n+1/2)*np.exp(-n)

ns = range(1, 21)
xs = np.linspace(1, 20, 100)
plt.xlim(0, 21)
plt.xticks(range(0, 21, 2))
plt.yscale('log')
plt.plot(xs, stirling(xs), 'r-',label='Stirling')
plt.plot(ns, [math.factorial(n) for n in ns], 'b.', label='n!')
plt.legend()
