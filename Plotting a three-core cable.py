import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

%matplotlib inline

def show_cable():
    w = 5
    R = 2
    r = 1
    s = np.sqrt(3)/2 * r
    u, v = np.meshgrid(np.linspace(0, 1, 100), np.linspace(0, 1, 100))
    ua = 2 * np.pi * u
    va = 2 * np.pi * v
    x = 10 * u - 5
    y_sheath   = R * np.cos(va) # edge of the sheath
    z_sheath   = R * np.sin(va) # edge of the sheath
    y0_earth   = r * np.cos(ua)              # centre of the earth core
    z0_earth   = r * np.sin(ua)              # centre of the earth core
    y0_neutral = r * np.cos(ua + 2*np.pi/3)  # centre of the neutral core
    z0_neutral = r * np.sin(ua + 2*np.pi/3)  # centre of the neutral core
    y0_line    = r * np.cos(ua + 4*np.pi/3)  # centre of the line core
    z0_line    = r * np.sin(ua + 4*np.pi/3)  # centre of the line core
    y1_earth   = y0_earth   + s * np.cos(4*ua+va/4)            # first green section of edge of the earth core
    z1_earth   = z0_earth   + s * np.sin(4*ua+va/4)            # first green section of edge of the earth core
    y2_earth   = y0_earth   + s * np.cos(4*ua+va/4+  np.pi/2)  # first yellow section of edge of the earth core
    z2_earth   = z0_earth   + s * np.sin(4*ua+va/4+  np.pi/2)  # first yellow section of edge of the earth core
    y3_earth   = y0_earth   + s * np.cos(4*ua+va/4+  np.pi)    # second green section of edge of the earth core
    z3_earth   = z0_earth   + s * np.sin(4*ua+va/4+  np.pi)    # second green section of edge of the earth core
    y4_earth   = y0_earth   + s * np.cos(4*ua+va/4+3*np.pi/2)  # second yellow section of edge of the earth core
    z4_earth   = z0_earth   + s * np.sin(4*ua+va/4+3*np.pi/2)  # second yellow section of edge of the earth core
    y1_neutral = y0_neutral + s * np.cos(va)                   # edge of the neutral core
    z1_neutral = z0_neutral + s * np.sin(va)                   # edge of the neutral core
    y1_line    = y0_line    + s * np.cos(va)                   # edge of the line core
    z1_line    = z0_line    + s * np.sin(va)                   # edge of the line core

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.axis('equal')
    ax.axis('off')
    ax.set_xlim(-w, w)
    ax.set_ylim(-w, w)
    ax.set_zlim(-w, w)
    ax.plot_wireframe(x, y_sheath, z_sheath,   color='#888888', rstride=5, cstride=5, alpha=0.5)
    ax.plot_surface(x, y1_earth,   z1_earth,   color='#00ff00', rstride=5, cstride=5, alpha = 1)
    ax.plot_surface(x, y2_earth,   z2_earth,   color='#ffff00', rstride=5, cstride=5, alpha = 1)
    ax.plot_surface(x, y3_earth,   z3_earth,   color='#00ff00', rstride=5, cstride=5, alpha = 1)
    ax.plot_surface(x, y4_earth,   z4_earth,   color='#ffff00', rstride=5, cstride=5, alpha = 1)
    ax.plot_surface(x, y1_neutral, z1_neutral, color='#0000ff', rstride=5, cstride=5, alpha = 1)
    ax.plot_surface(x, y1_line,    z1_line,    color='#964b00', rstride=5, cstride=5, alpha = 1)


show_cable()
