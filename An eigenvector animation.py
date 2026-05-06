import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

%matplotlib inline

A0 = [[2,-4],[-3,1]]
A = np.array(A0)
L, U = np.linalg.eig(A)
print(f"The eigenvectors of the matrix A={A0} are {U[:,0]} and {U[:,1]}, with eigenvalues {L[0]} and {L[1]} respectively.")

N = 200
ts = np.linspace(0,2*np.pi,N)
xs = np.cos(ts)                       # x coordinates of points on the unit circle
ys = np.sin(ts)                       # y coordinates of points on the unit circle
C = np.array([np.cos(ts),np.sin(ts)]) # matrix whose columns are the points on the unit circle
E = A @ C                             # matrix whose columns are points on the ellipse
Axs = E[0]                            # x coordinates of points on the ellipse
Ays = E[1]                            # y coordinates of points on the ellipse

fig, ax = plt.subplots()
ax.axis('equal')
ax.axis('off')
ax.plot(C[0],C[1],color='green')   # draw the unit circle
ax.plot(E[0],E[1],color='orange')  # draw the ellipse
# draw black lines for the eigenvector directions
ax.plot([-L[0] * U[0,0], L[0] * U[0,0]], [-L[0] * U[1,0], L[0] * U[1,0]],'k-')
ax.plot([-L[1] * U[0,1], L[1] * U[0,1]], [-L[1] * U[1,1], L[1] * U[1,1]],'k-')
# The object v_line will be the line joining the origin to the point v on he unit circle
# At this stage we just set v_line to be an empty line.  The first call to repaint()
# will set v_line to be the line from (0,0) to (1,0), and then subsequent calls to
# repaint() will move it around the unit circle.  Similarly, v_blob will be the point
# v, and Av_blob will be the point Av on the ellipse, and Av_line will be the line
# from (0,0) to Av.
v_line,  = ax.plot([], [], 'r-')
v_blob,  = ax.plot([], [], 'ko')
Av_line, = ax.plot([], [], 'b-')
Av_blob, = ax.plot([], [], 'ko')
text = ax.text(3, 3, '0')

def repaint(i):    
    v_line.set_data([0, xs[i]], [0, ys[i]])
    v_blob.set_data([xs[i]], [ys[i]])
    Av_line.set_data([0, Axs[i]], [0, Ays[i]])
    Av_blob.set_data([Axs[i]], [Ays[i]])
    text.set_text(f'{i}')
    # For the animation to work correctly, repaint() needs to return a tuple of the
    # objects that have been changed.
    return (v_line, v_blob, Av_line, Av_blob, text)

anim = None
# For the animation framework to work correctly, the object returned by FuncAnimation()
# must be assigned to a variable, otherwise it will be garbage collected and the animation
# will not work.
anim = FuncAnimation(fig, repaint, frames=N, interval=20, blit=True)


#vector v = red = eigenvector with eigenvalue λ
#unit circle = green 
#vector Av = blue 
#ellipse = orange 
#occasionally Av = λv
#eigenvector directions = black 
