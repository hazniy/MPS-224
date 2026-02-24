import numpy as np
import matplotlib.pyplot as plt

#spiral
ts = np.linspace(0, 5, 1000)
xs = np.cos(10 * ts) / (1 + ts**2)
ys = np.sin(10 * ts) / (1 + ts**2)
plt.axis('equal')
plt.plot(xs, ys)

#big bang
fig, ax = plt.subplots(1, 2)
fig.set_size_inches(10, 5)
ts = np.linspace(0, 2*np.pi, 1000)
ax[0].plot(np.sin(2*ts), np.sin(3*ts))
ax[1].plot(np.sin(6*ts), np.sin(7*ts))

#half circle 
ts = np.linspace(0, 8*np.pi, 1000)
xs = ts - np.sin(ts)
ys = 1 - np.cos(ts)
plt.axis('equal')
plt.plot(xs, ys)
plt.hlines(0, 0, 8*np.pi, color='gray', linestyle='--')

#circle a bit open 
t = np.linspace(-8,8,1000)
x = (1 - t**2)/(1 + t**2)
y = 2*t/(1 + t**2) 
plt.axis('equal')
plt.plot(x,y)

xr = np.linspace(-2, 2, 400)
yr = np.linspace(-2, 2, 400)
x, y = np.meshgrid(xr, yr)
plt.contour(x, y, y**2 - (x**3 - x), levels=[0], colors='red')

xr = np.linspace(-2, 2, 400)
yr = np.linspace(-2, 2, 400)
x, y = np.meshgrid(xr, yr)
plt.contour(x, y, y**2 - (x**3 - x), levels=[0.3,0.4], colors=['red','blue'])

xr = np.linspace(0.4, 0.8, 400)
yr = np.linspace(-0.3, 0.3, 400)
x, y = np.meshgrid(xr, yr)
plt.contour(x, y, y**2 - (x**3 - x), levels=[0.38,0.3848,0.389], colors=['red','green','blue'])

xr = np.linspace(-5, 5, 1000)
yr = np.linspace(-5, 5, 1000)
x, y = np.meshgrid(xr, yr)
r2 = x**2 + y**2
t = np.linspace(-5, 5, 1000)
fig, ax = plt.subplots(1, 2)
fig.set_size_inches(10, 5)
ax[0].axis('equal')
ax[1].axis('equal')
ax[0].contour(x, y, x * np.sin(r2) - y * np.cos(r2), levels=[0], colors=['red'])
ax[1].plot(t * np.cos(t**2), t * np.sin(t**2))

xr = np.linspace(-8, 12, 1000)
yr = np.linspace(-10, 10, 1000)
x, y = np.meshgrid(xr, yr)
u = (x**2+y**2)**2 + 85*(x**2+y**2) - 500 + 18*x*(3*y**2-x**2)
t = np.linspace(0, 2*np.pi, 1000)
xt = 6*np.cos(t) + 8*np.cos(t)**2 - 4
yt = 2*np.sin(t)*(3-4*np.cos(t))
fig, ax = plt.subplots(1, 2)
fig.set_size_inches(10, 5)
ax[0].contour(x, y, u, levels=[0], colors=['red'])
ax[1].plot(xt, yt)
ax[0].set_xlim(-8, 12)
ax[0].set_ylim(-10, 10)
ax[1].set_xlim(-8, 12)
ax[1].set_ylim(-10, 10)
