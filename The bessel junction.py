import scipy
import numpy as np
import matplotlib.pyplot as plt

def J2(x):
    return scipy.special.jv(2, x)

fig, ax = plt.subplots()
fig.set_size_inches(10, 5)
ax.spines['bottom'].set_position('zero')
xs = np.linspace(-50, 50, 1001)
ys = J2(xs)
ax.plot(xs, ys, 'r')
#the plot shows J2(x) is very close to x^2/8 when x is small 

fig, ax = plt.subplots()
fig.set_size_inches(10, 5)
ax.spines['bottom'].set_position('zero')
xs = np.linspace(-0.6, 0.6, 101)
ys = J2(xs)
ax.plot(xs, ys, 'r', label = r'$J_2(x)$')
ax.plot(xs, (xs ** 2)/8, 'b', label = r'$x^2/8$')
ax.legend()
#the plot shows the envelope of J2(x) is 4x^-1/2/5, so J2(x) oscillates between -4x^-1/2/5 and +4x^-1/2/5

fig, ax = plt.subplots()
fig.set_size_inches(10, 5)
ax.spines['bottom'].set_position('zero')
xs = np.linspace(10, 300, 2000)
ys = J2(xs)
zs = 0.8 * xs ** -0.5
ax.plot(xs, ys, 'r', label = r'$J_2(x)$')
ax.plot(xs, zs, 'b', label = r'$4 x^{-1/2}/5$')
ax.plot(xs,-zs, 'g', label = r'$-4 x^{-1/2}/5$')
ax.legend()
#the plot shows J2(x) oscillates with a pattern very similar to that of sin(x+pi/4) 

fig, ax = plt.subplots()
fig.set_size_inches(10, 5)
ax.spines['bottom'].set_position('zero')
xs = np.linspace(10, 100, 1000)
ys = J2(xs)
zs = np.sin(xs + np.pi/4)
ax.plot(xs, ys, 'r', label = r'$J_2(x)$')
ax.plot(xs, zs, 'b', label = r'$\sin(x+\pi/4)$')
ax.legend()
#the plot shows J2(x) is very close to -4x^-1/2 sin(x+pi/4)/5 as soon as x is reasonably large 

fig, ax = plt.subplots()
fig.set_size_inches(10, 5)
ax.spines['bottom'].set_position('zero')
xs = np.linspace(1, 50, 1000)
ys = J2(xs)
zs = -4/5 * xs ** -0.5 * np.sin(xs + np.pi/4)
ax.plot(xs, ys, 'r', label = r'$J_2(x)$')
ax.plot(xs, zs, 'b', label = r'$-4x^{-1/2}\sin(x+\pi/4)/5$')
ax.legend()
