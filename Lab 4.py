#Task 1: The equation x = x^3
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def dxdt(t, x):
    return x**3

t = np.linspace(0, 0.1, 1000)
sol = solve_ivp(dxdt, (t[0], t[-1]), [1], t_eval=t)
#plt.plot(sol.t, sol.y[0]) opt 1
#plt.plot(t, sol.y[0]) opt 2
plt.xlabel("t")
plt.ylabel("x(t)")
plt.show()

def cutoff(a):
    def dxdt(t, x):
        return x**3
    t = np.linspace(0, 1, 10000)
    sol = solve_ivp(dxdt, (t[0], t[-1]), [a], t_eval=t)
    return sol.t[-1]

for a in range(1,6):
    print(a, cutoff(a))

#the more accurate one 

def cutoff(a):
    return 1/(2*a**2)

for a in range(1,6):
    print(a, cutoff(a))

#submit 
import numpy as np
from scipy.integrate import solve_ivp

def cutoff(a):
    def dxdt(t, x):
        return x**3
    
    t = np.linspace(0, 1, 10000)
    sol = solve_ivp(dxdt, (t[0], t[-1]), [a], t_eval=t) #or sol = solve_ivp(dxdt, (0,1), [a], t_eval=t)
    
    return sol.t[-1] #st value is just before the cutoff time 𝑡0

#Task 2: Methane Combustion 
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

R = 1.987
P0 = 2.422e-2

A = np.array([1.59e13, 3.98e8, 6.16e13])
beta = np.array([0, 0, -0.97])
E = np.array([4.78e4, 1.00e4, 7.84e4])

N = np.array([
[-1, 0, 0],
[-1.5, -0.5, 0.5],
[1, -1, 1],
[2, 0, 0],
[0, 1, -1]
])

def rate_constants(T):
    return A * T**beta * np.exp(-E/(R*T))

def fraction_to_molarity(p, T, P=P0):
    return p * P / (R*T)

def molarity_to_fraction(x):
    return x / np.sum(x)

def x_dot(t, x, k):

    y = np.maximum(x, 1e-9)

    r0 = k[0]*y[0]**0.70 * y[1]**0.80
    r1 = k[1]*y[1]**0.25 * y[2]**0.50
    r2 = k[2]*y[1]**0.25 * y[3]**0.50 * y[4]

    r = np.array([r0, r1, r2])

    return N @ r

def solve_combustion(T, p0, t_max, n):

    x0 = fraction_to_molarity(p0, T)

    k = rate_constants(T)

    t = np.linspace(0, t_max, n)

    sol = solve_ivp(
        x_dot,
        (0, t_max),
        x0,
        method='BDF',
        atol=1e-9,
        t_eval=t,
        args=(k,)
    )

    x = sol.y.T

    p = np.array([molarity_to_fraction(row) for row in x])

    return sol.t, p

def show_combustion(T, p0, t_max, n):

    t, p = solve_combustion(T, p0, t_max, n)

    labels = ["CH4", "O2", "CO", "H2O", "CO2"]

    for i in range(5):
        plt.plot(t, p[:,i], label=labels[i])

    plt.xscale("log")

    plt.xlabel("time")
    plt.ylabel("molar fraction")

    plt.legend()
    plt.show()
    
T = 1500
p0 = np.array([0.1, 0.25, 0.01, 0.01, 0.63])
t_max = 0.1

show_combustion(T, p0, t_max, 5000)
