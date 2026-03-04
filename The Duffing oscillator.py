import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def du_dt(t, u):
    return np.array([u[1], 2*u[0] - u[0]**3])

fig, ax = plt.subplots(figsize = (8, 8))
ax.set_aspect('equal')

t = np.linspace(0, 24, 4000)
ics = ([[ x0, 0] for x0 in np.arange(0.1, 1.5,0.1)] + 
       [[-x0, 0] for x0 in np.arange(0.1, 1.5,0.1)] + 
       [[ 0, y0] for y0 in np.arange(0.2, 1.5,0.1)])
for xy0 in ics:
    sol = solve_ivp(du_dt, [t[0], t[-1]], xy0, t_eval = t, method = 'DOP853', atol = 1e-9)
    ax.plot(sol.y[0], sol.y[1])
ax.plot([-np.sqrt(2), 0, np.sqrt(2)], [0, 0, 0], 'ko')
