import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def euler(f, a, b, x0, n = 100):
    """
    Solve dx/dt = f(t,x) for t from a to b using n steps

    Return a pair (ts, xs) where ts is the array of values of t
    and xs is the array of corresponding values of x.
    """
    # ts is an array of n+1 equally spaced numbers from a to b
    # There are n+1 numbers, with n gaps between them, each of size (b-a)/n
    ts = np.linspace(a, b, n+1)
    # If x0 is just a scalar, the line below is equivalent to xs = np.zeros(n+1)
    # We use a fancier version for later cases where x0 is a numpy array of arbitrary shape
    xs = np.zeros((n+1,) + np.shape(x0))
    xs[0] = x0
    h = (b-a)/n
    for i in range(n):
        xs[i+1] = xs[i] + h * f(ts[i], xs[i])
    return ts, xs

f0 = lambda t, x: x

plt.figure(figsize=(20, 6))
plt.ylim(0, 3)
ts = np.linspace(0, 1, 101)
plt.plot(ts, np.exp(ts), label='exact' )
for k in range(10,80,10):
    ts, xs = euler(f0, 0, 1, 1, k)
    plt.plot(ts, xs, label=f'{k} steps')
plt.legend()

def midpoint(f, t0, t1, x0, n = 100):
    ts = np.linspace(t0, t1, n+1)
    # If x0 is just a scalar, the line below is equivalent to xs = np.zeros(n+1)
    # We use a fancier version for later cases where x0 is a numpy array of arbitrary shape
    xs = np.zeros((n+1,) + np.shape(x0))
    xs[0] = x0
    h = (t1-t0)/n
    for i in range(n):
        tt = ts[i] + h/2
        xx = xs[i] + h/2 * f(ts[i], xs[i])
        xs[i+1] = xs[i] + h * f(tt, xx)
    return ts, xs

plt.figure(figsize=(20, 6))
plt.ylim(0, 3)
ts = np.linspace(0, 1, 101)
plt.plot(ts, np.exp(ts), label='exact' )
for k in range(3,15,3):
    ts, xs = midpoint(f0, 0, 1, 1, k)
    plt.plot(ts, xs, label=f'{k} steps')
plt.legend()

plt.figure(figsize=(20, 6))
ts = np.linspace(0, 1, 101)
for k in range(3,24,3):
    ts, xs = midpoint(f0, 0, 1, 1, k)
    plt.plot(ts, xs - np.exp(ts), label=f'{k} steps')
plt.legend()

g = lambda t, u: np.array([u[1], -u[0]])

te, ue = euler(g, 0, 20, np.array([1, 0]), 60)
tm, um = midpoint(g, 0, 20, np.array([1, 0]), 60)
xe = ue[:,0]    # same as ue.T[0]
xm = (um.T)[0]  # same as um[:,0]

plt.figure(figsize=(20, 6))
plt.plot(te, xe, color = 'red', label = 'euler' )
plt.plot(tm, xm, color = 'blue', label = 'midpoint' )
plt.legend()
