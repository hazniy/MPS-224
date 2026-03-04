import numpy as np
import matplotlib.pyplot as plt

def runge_kutta(f, a, b, x0, n = 100):
    h = (b - a) / n
    x = x0
    ts = np.linspace(a, b, n + 1)
    xs = np.zeros(n + 1)
    for i in range(n):
        t = ts[i]
        m0 = f(t, x)
        m1 = f(t + h / 2, x + h * m0 / 2)
        m2 = f(t + h / 2, x + h * m1 / 2)
        m3 = f(t + h, x + h * m2)
        m4 = (m0 + 2 * m1 + 2 * m2 + m3) / 6
        x = x + h * m4 
        xs[i] = x
    return (ts, xs)

RKFA = np.array([[        0,          0,          0,         0,      0, 0],
                 [      1/4,          0,          0,         0,      0, 0],
                 [     3/32,       9/32,          0,         0,      0, 0],
                 [1932/2197, -7200/2197,  7296/2197,         0,      0, 0],
                 [  439/216,         -8,   3680/513, -845/4104,      0, 0],
                 [    -8/27,          2, -3544/2565, 1859/4104, -11/40, 0]])
RKFB4 = np.array([25/216, 0,  1408/2565,   2197/4104,  -1/5,    0])
RKFB5 = np.array([16/135, 0, 6656/12825, 28561/56430, -9/50, 2/55])
RKFC = np.array([0,1/4,3/8,12/13,1,1/2])

butcher_tableau = np.zeros((8, 7 ))
butcher_tableau[0:6, 1:7] = RKFA
butcher_tableau[0:6,   0] = RKFC
butcher_tableau[  6, 1:7] = RKFB5
butcher_tableau[  7, 1:7] = RKFB4

print(np.round(butcher_tableau,6))

print(RKFB4.sum() - 1)
print(RKFB5.sum() - 1)
print(RKFA . sum ( axis = 1 ) - RKFC)
print([(j+1) * RKFB4.dot(RKFC ** j) - 1 for j in range(4)])
print([(j+1) * RKFB5.dot(RKFC ** j) - 1 for j in range(5)])

def runge_kutta_fehlberg(f, a, b, x0, h = None, epsilon = 1e-6):
    if h is None:
        h = (b - a) / 10
    x = x0
    ts = [a]
    xs = [x0]
    while (t := ts[-1]) < b:
        m = np.zeros((6,) + np.shape(x))
        for j in range(6):
            m[j] = f(t + RKFC[j] * h, x + np.tensordot(RKFA[j], m, (0,0)) * h)
        dx = np.dot(RKFB4, m) * h
        # estimate the error
        err = np.linalg.norm(np.tensordot(RKFB5 - RKFB4, m, (0,0)) * h)
        # step size ratio
        s = 0.9 * (epsilon / err) ** 0.2
        # If the estimated error is within the tolerance, we assume that 
        # our estimate of dx is OK so we add t + h to our list of t values
        # and x + dx to our list of x values, and use these values for
        # the next iteration. If the estimated error is too big then we
        # do not change t or x, and we do not add anything to our lists.
        # Instead we just proceed to the next line, which reduces the step
        # size, and then we go back to the start of the while loop,
        # recalculating m and dx with the smaller step size.
        if err < epsilon:
            t += h
            x += dx
            ts.append(t)
            xs.append(np.copy(x))

        # We now modify the step size.  If the estimated error is small then 
        # s > 1 and we increase the step size, but we do not increase it by
        # more than a factor of 2, to be on the safe side. If the estimated
        # error is large then s < 1 and we decrease the step size.  We also
        # include b - t in the min() function to ensure that the step size
        # does not take us past t = b, which is where we want to stop.
        h = min(s * h, 2 * h, b - t)
    return (np.array(ts), np.array(xs))

def u(t):
    return np.exp(-2*(t-5)**2)*np.sin(20*t)

def f(t,x):
    return -2*x+u(t)

ts = np.linspace(0,10,1000)
plt.plot(ts, u(ts), label = 'u(t)')
plt.legend()
None

ts, xs = runge_kutta_fehlberg(f, 0, 10, 1)
fig, ax = plt.subplots(1,2)
fig.set_size_inches(10, 5)
ax[0].plot(ts, xs, label = 'x(t)')
ax[0].legend()
ax[1].plot(ts[1:], ts[1:]-ts[:-1],'.', label = 'step sizes')
ax[1].set_ylim(0)
ax[1].legend()

def g(t, u):
    return np.array([u[1], -(1 + u[1]) ** 3 * u[0]])

a = 0.95 # Try varying this from 0.1 to 0.95
ts, us = runge_kutta_fehlberg(g, 0, 4*np.pi, np.array([a, 0]), 0.01, 1e-9)
xs = us[:,0]
vs = us[:,1]
fig, ax = plt.subplots(1,3)
fig.set_size_inches(15, 5)
ax[0].plot(ts, xs, label = r"$x$")
ax[0].plot(ts, vs, label = r"$\dot{x}$")
ax[0].legend()
ax[1].plot(xs, vs, label = r"$(x(t),\dot{x}(t))$")
ax[1].legend()
ax[2].plot(ts[1:], ts[1:]-ts[:-1],'.' ,label = 'step sizes')
ax[2].set_ylim(0)
ax[2].legend()
