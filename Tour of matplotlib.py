import math
import numpy as np
import matplotlib.pyplot as plt

# y = sinx
#np.linspace to generate array xs of 100 equally spaced x values between 0 and 2pi 
xs = np.linspace(0, 2*np.pi, 100)  # x coordinates of points on the graph
ys = np.sin(xs)                    # y coordinates of points on the graph
plt.plot(xs, ys) 
#can use the simple plt.plot 
#OR 
ts = np.linspace(0, 2*np.pi, 629)
ys = np.sin(ts)
fig, ax = plt.subplots()
ax.plot(ts, ys, 
        color = 'orange',       # note the American spelling: color not colour
        linewidth = 2,          # twice as thick as usual
        linestyle = '--',       # dashed line
        label=r'$\sin(\theta)$' # Use r'...' for strings with backslashes
        )
ax.plot(ts, ys * np.sin(20*ts), 'r')
ax.set_xlabel(r'$\theta$') # Use r'...' for strings with backslashes
ax.set_title('A simple plot')
ax.set_xticks(np.linspace(0, 2*np.pi, 5),['0', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'])
ax.spines['bottom'].set_position('zero') # Draw x-axis at y=0 instead of at the bottom of the graph
ax.spines['top'].set_visible(False) # Don't draw top axis
ax.legend() # Without this, the label sin(theta) will not be shown
plt.show()

fig, ax = plt.subplots(2, 2, figsize=(10, 10)) #2x2 array subjects whith 10x10 size
xs = np.linspace(0, 1, 100)
ax[0,0].plot(xs, np.sin(4 * np.pi * xs)) #draw top left subplot 
ax[0,0].set_title('Sinusoid')
ax[0,1].plot(xs, 4 * xs * (1 - xs)) #top right subplot 
ax[0,1].set_title('Parabola')
ax[1,0].plot(xs, np.exp(-(4*xs-2)**2))
ax[1,0].set_title('Gaussian')
ax[1,1].plot(xs, np.exp(-5*xs) * np.sin(50*xs))
ax[1,1].set_title('Damped Sinusoid')
None #avoid printing irrelevant message 

# y = sin(npix) 
fig, ax = plt.subplots(2, 3, figsize=(15, 10)) # Now ax is an array of axes of shape 2 x 3
ax = ax.flatten() # Flatten the array to make it easier to loop through the six axes
                  # now we have ax[0] .. ax[5] instead of ax[0,0] .. ax[1,2]
for i in range(6):
    axi = ax[i]
    m = i + 2
    axi.plot(xs, np.sin(m * np.pi * xs))
    axi.set_title(r'$y=\sin(' + str(m) + r'\pi x$)')
    
#can also do parametric plots, eg the cycloid curve, w para eqn x = t-sin(t) & y=1-cos(t)
ts = np.linspace(0, 8*np.pi, 1000)
xs = ts - np.sin(ts)
ys = 1 - np.cos(ts)
plt.axis('equal')
plt.plot(xs, ys)
plt.hlines(0, 0, 8*np.pi, color='gray', linestyle='--')

# curve para eqn x = 1-t^2/1+t^2 & y = 2t/1+t^2
ts = np.linspace(-8, 8, 1000)
xs = (1 - ts**2) / (1 + ts**2)
ys = 2 * ts / (1 + ts**2)
plt.axis('equal')
plt.plot(xs, ys)

#plot f(x,y) = y^2 - (x^3 - x), plot the curve f(x,y) = 0 which y^2 = x^3 - x (elliptic curve)
xr = np.linspace(-2, 2, 400)
yr = np.linspace(-2, 2, 400)
x, y = np.meshgrid(xr, yr)
z = y**2 - (x**3 - x)
plt.contour(x, y, z, levels=[0], colors='red')

#plot f(x,y) = xsin(x^2+y^") - ycos(x^2+y^2) == u(t) = tsin(t^2) == v(t) = tcos(t^2)
# Setup
fig, ax = plt.subplots(1, 2)
fig.set_size_inches(10, 5)
# Implicit version, using ax[0] = left hand side
def f(x, y):
    return x * np.sin(x**2 + y**2) - y * np.cos(x**2 + y**2)
xr = np.linspace(-5, 5, 1000)
yr = np.linspace(-5, 5, 1000)
x, y = np.meshgrid(xr, yr)
ax[0].axis('equal')
ax[0].contour(x, y, f(x,y), levels=[0], colors=['red'])
# Parametric version, using ax[1] = right hand side
def u(t):
    return t * np.cos(t**2)
def v(t):
    return t * np.sin(t**2)
t = np.linspace(-5, 5, 1000)
ax[1].axis('equal')
ax[1].plot(u(t), v(t))
