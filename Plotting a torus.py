import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

%matplotlib inline

def show_torus(R = 2, r = 1, w = 4):
    """
    Display a 3D plot of a torus.

    Parameters
    ----------
    R : float
        The major radius of the torus.
    r : float
        The minor radius of the torus.
    w : float
        The width of the plot.
    """
    u, v = np.meshgrid(np.linspace(0, 2*np.pi, 100), np.linspace(0, 2*np.pi, 100))
    x = (R + r*np.cos(v)) * np.cos(u)
    y = (R + r*np.cos(v)) * np.sin(u)
    z = r * np.sin(v)
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.axis('equal')
    ax.set_xlim(-w, w)
    ax.set_ylim(-w, w)
    ax.set_zlim(-w, w)
    ax.plot_surface(x, y, z, rstride=5, cstride=5)


show_torus(2, 0.5, 3)
