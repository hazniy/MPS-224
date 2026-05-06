#Task 1: The dodecahedron
#golden ratio : Γ0 
#its reciprocal : Γ1

#Euclidean distance
np.linalg.norm(vi - vj)

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

%matplotlib inline

import numpy as np

def make_dodecahedron():
    phi = (np.sqrt(5) + 1) / 2      # Γ0
    psi = (np.sqrt(5) - 1) / 2      # Γ1

    vertices = []

    # (±1, ±1, ±1)
    for x in [-1, 1]:
        for y in [-1, 1]:
            for z in [-1, 1]:
                vertices.append([x, y, z])

    # (±Γ0, ±Γ1, 0)
    for x in [-phi, phi]:
        for y in [-psi, psi]:
            vertices.append([x, y, 0])

    # (0, ±Γ0, ±Γ1)
    for y in [-phi, phi]:
        for z in [-psi, psi]:
            vertices.append([0, y, z])

    # (±Γ1, 0, ±Γ0)
    for x in [-psi, psi]:
        for z in [-phi, phi]:
            vertices.append([x, 0, z])

    vertices = np.array(vertices).T   # shape (3, 20)

    # --- compute edge length ---
    n = vertices.shape[1]
    min_dist = np.inf

    for i in range(n):
        for j in range(i+1, n):
            d = np.linalg.norm(vertices[:, i] - vertices[:, j])
            if d < min_dist:
                min_dist = d

    edge_length = min_dist

    # --- find edges ---
    edges = []
    tol = 1e-6

    for i in range(n):
        for j in range(i+1, n):
            d = np.linalg.norm(vertices[:, i] - vertices[:, j])
            if d < edge_length + tol:
                edges.append([i, j])

    edges = np.array(edges, dtype=int)

    return vertices, edges

import matplotlib.pyplot as plt

vertices, edges = make_dodecahedron()

ax = plt.figure().add_subplot(projection='3d')
ax.axis('off')

# plot vertices
ax.scatter(vertices[0], vertices[1], vertices[2], color='blue')

# plot edges
for i, j in edges:
    ax.plot(
        [vertices[0, i], vertices[0, j]],
        [vertices[1, i], vertices[1, j]],
        [vertices[2, i], vertices[2, j]],
        color='red'
    )

plt.show()

#Q1 
import numpy as np

def make_dodecahedron():
    """
    Construct the vertices and edges of a regular dodecahedron.
    - The vertices :
       (±1, ±1, ±1), (±Γ0, ±Γ1, 0), (0, ±Γ0, ±Γ1), (±Γ1, 0, ±Γ0), where Γ0 = (sqrt(5)+1)/2 and Γ1 = (sqrt(5)-1)/2.
    - edges : Each row [i, j] (with 0 ≤ i < j < 20) represents a pair of vertices whose Euclidean distance is minimal (i.e. they form an edge of the dodecahedron).
    """
    # Golden ratio constants
    gamma0 = (np.sqrt(5) + 1) / 2
    gamma1 = (np.sqrt(5) - 1) / 2

    vertices_list = []

    # (±1, ±1, ±1)
    for x in [-1, 1]:
        for y in [-1, 1]:
            for z in [-1, 1]:
                vertices_list.append([x, y, z])

    # (±Γ0, ±Γ1, 0)
    for x in [-gamma0, gamma0]:
        for y in [-gamma1, gamma1]:
            vertices_list.append([x, y, 0])

    # (0, ±Γ0, ±Γ1)
    for y in [-gamma0, gamma0]:
        for z in [-gamma1, gamma1]:
            vertices_list.append([0, y, z])

    # (±Γ1, 0, ±Γ0)
    for x in [-gamma1, gamma1]:
        for z in [-gamma0, gamma0]:
            vertices_list.append([x, 0, z])

    # Convert to numpy array with shape (3,20)
    vertices = np.array(vertices_list).T

    # Compute minimum distance (edge length)
    n = vertices.shape[1]
    edge_length = np.inf

    for i in range(n):
        for j in range(i + 1, n):
            d = np.linalg.norm(vertices[:, i] - vertices[:, j])
            if d < edge_length:
                edge_length = d

    # Find all edges (pairs at minimum distance)
    edges_list = []
    tol = 1e-6

    for i in range(n):
        for j in range(i + 1, n):
            d = np.linalg.norm(vertices[:, i] - vertices[:, j])
            if d < edge_length + tol:
                edges_list.append([i, j])

    edges = np.array(edges_list, dtype=int)

    return vertices, edges

#dont submit just check 
v, e = make_dodecahedron()
print(v.shape)  # (3, 20)
print(e.shape)  # (30, 2)

#Task 2: Solitons
#vectorised NumPy implementation 
import numpy as np

def phi(t, x):
    """
    Compute the five soliton solutions (phi_0,...,phi_4) of the KdV equation.
    """
    q = np.sqrt(2)
    r = x - 4*t
    s = q * (x - 8*t)
    p = np.log(3 + 2*q)

    T = 32*np.cosh(2*r - p) + 16*np.cosh(2*s - p) + 16
    B = 4*(1 + q)*np.cosh(r)*np.cosh(s) + (4*q - 8)*np.exp(r + s)

    phi0 = 2 / (np.cosh(r)**2)
    phi1 = 4 / (np.cosh(s)**2)
    phi2 = 2 / (np.cosh(r - p)**2)
    phi3 = 4 / (np.cosh(s - p)**2)
    phi4 = T / (B**2)

    return np.array([phi0, phi1, phi2, phi3, phi4])

#plotting 
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-30, 30, 1000)
t = -0.8

values = phi(t, x)

plt.plot(x, values[4])
plt.title("phi_4(-0.8, x)")
plt.xlabel("x")
plt.ylabel("phi_4")
plt.show()

#animation 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# assume phi(t,x) is already defined

# grids
t = np.linspace(-3, 3, 200)
x = np.linspace(-30, 30, 1000)

# figure + axis
fig, ax = plt.subplots()
ax.set_xlim(-30, 30)
ax.set_ylim(0, 5)

# initial plot (t = -3)
y = phi(t[0], x)[4]
line = ax.plot(x, y)[0]

# update function
def repaint(i):
    y = phi(t[i], x)[4]
    line.set_data(x, y)
    return (line,)

# animation
anim0 = FuncAnimation(
    fig,
    repaint,
    frames=len(t),
    interval=20,
    blit=True
)

plt.show()

#animation 2
fig, ax = plt.subplots()
ax.set_xlim(-30, 30)
ax.set_ylim(0, 25)

# initial lines
lines = []
labels = [
    r'$\phi_0$',
    r'$\phi_1$',
    r'$\phi_2$',
    r'$\phi_3$'
]

for i in range(4):
    y = phi(t[0], x)[i] + 5*i
    line = ax.plot(x, y, label=labels[i])[0]
    lines.append(line)

ax.legend()

# repaint function
def repaint_multi(i):
    values = phi(t[i], x)
    for j in range(4):
        y = values[j] + 5*j
        lines[j].set_data(x, y)
    return tuple(lines)

# animation
anim1 = FuncAnimation(
    fig,
    repaint_multi,
    frames=len(t),
    interval=20,
    blit=True
)

plt.show()

#Q2 
 def phi(t, x):
    """
    Compute the five soliton solutions (phi_0,...,phi_4) of the KdV equation.
    """
    q = np.sqrt(2)
    r = x - 4*t
    s = q * (x - 8*t)
    p = np.log(3 + 2*q)

    T = 32*np.cosh(2*r - p) + 16*np.cosh(2*s - p) + 16
    B = 4*(1 + q)*np.cosh(r)*np.cosh(s) + (4*q - 8)*np.exp(r + s)

    phi0 = 2 / (np.cosh(r)**2)
    phi1 = 4 / (np.cosh(s)**2)
    phi2 = 2 / (np.cosh(r - p)**2)
    phi3 = 4 / (np.cosh(s - p)**2)
    phi4 = T / (B**2)

    return np.array([phi0, phi1, phi2, phi3, phi4])
#Task 3: Stacked balls
