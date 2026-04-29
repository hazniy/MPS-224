import numpy as np
import scipy.fft as fft
import matplotlib.pyplot as plt

# 0. Square wave (0 or 1, 50% duty cycle)
def f0(x):
    x = np.mod(x, 1)
    return (x >= 0.5).astype(float)

# 1. Sawtooth wave (already given)
def f1(x):
    return x - np.floor(x)

# 2. Triangle wave (peaks at 0.5, symmetric)
def f2(x):
    x = np.mod(x, 1)
    return 0.5 - np.abs(x - 0.5)

# 3. Pulse wave (short pulses, width 0.25 every period)
def f3(x):
    x = np.mod(x, 1)
    return np.where(x < 0.25, 1.0, 0.0)

# 4. Rectified sine wave
def f4(x):
    x = np.mod(x, 1)
    return np.abs(np.sin(np.pi * x))

functions = [f0, f1, f2, f3, f4]

#Q1
def f0(x):
    """Square wave (0 or 1, 50% duty cycle)"""
    x = np.mod(x, 1)
    return (x >= 0.5).astype(float)

#Q2
def f2(x):
    """Triangle wave (peaks at 0.5, symmetric)"""
    x = np.mod(x, 1)
    return 0.5 - np.abs(x - 0.5)

#Q3
def f4(x):
    """
    Rectified sine wave with period 1.
    """
    x = np.mod(x, 1)
    return np.abs(np.sin(np.pi * x))

#set up sampling 
N = 64 
ts = np.arange(0, 1, 1/N)

#for square wave 
import matplotlib.pyplot as plt

xs = np.linspace(0, 4, 1000, endpoint=False)

functions = [f0, f1, f2, f3, f4]
titles = ["Square wave", "Sawtooth wave", "Triangle wave", "Pulse wave", "Rectified sine wave"]

fig, axes = plt.subplots(5, 1, figsize=(8, 10))

for i, f in enumerate(functions):
    axes[i].plot(xs, f(xs))
    axes[i].set_title(titles[i])
    axes[i].set_ylim(-0.1, 1.1)

plt.tight_layout()
plt.show()

#for triangle wave 
import matplotlib.pyplot as plt

xs = np.linspace(0, 4, 1000, endpoint=False)

functions = [f0, f1, f2, f3, f4]
titles = ["Square wave", "Sawtooth wave", "Triangle wave", "Pulse wave", "Rectified sine wave"]

fig, axes = plt.subplots(5, 1, figsize=(8, 10))

for i, f in enumerate(functions):
    axes[i].plot(xs, f(xs))
    axes[i].set_title(titles[i])
    axes[i].set_ylim(-0.1, 0.6)

plt.tight_layout()
plt.show()

#for the rest 
#for square wave 
import matplotlib.pyplot as plt

xs = np.linspace(0, 4, 1000)

functions = [f0, f1, f2, f3, f4]
titles = ["Square wave", "Sawtooth wave", "Triangle wave", "Pulse wave", "Rectified sine wave"]

fig, axes = plt.subplots(5, 1, figsize=(8, 10))

for i, f in enumerate(functions):
    axes[i].plot(xs, f(xs))
    axes[i].set_title(titles[i])
    axes[i].set_ylim(-0.1, 1.1)

plt.tight_layout()
plt.show()

#theoretical dourier values
k = np.arange(N)
pi = np.pi

# Avoid division warnings
k_safe = np.where(k == 0, 1, k)

# f0: Square wave
F0 = np.zeros(N, dtype=complex)
F0[0] = 1/2
F0[1:] = np.where(k[1:] % 2 == 0, 0, 1j/(pi * k_safe[1:]))

# f1: Sawtooth
F1 = np.zeros(N, dtype=complex)
F1[0] = 1/2
F1[1:] = 1j/(2*pi*k_safe[1:])

# f2: Triangle
F2 = np.zeros(N, dtype=complex)
F2[0] = 1/4
F2[1:] = np.where(k[1:] % 2 == 0, 0, -1/(pi**2 * k_safe[1:]**2))

# f3: Pulse wave
F3 = np.zeros(N, dtype=complex)
F3[0] = 1/4
F3[1:] = -1j * (1 - (-1j)**k[1:]) / (2*pi*k_safe[1:])

# f4: Rectified sine
F4 = 2 / (pi * (1 - 4*k**2))

theory = [F0, F1, F2, F3, F4]

half = N // 2
k = np.arange(N)
pi = np.pi

F0 = np.zeros(N, dtype=complex)
F1 = np.zeros(N, dtype=complex)
F2 = np.zeros(N, dtype=complex)
F3 = np.zeros(N, dtype=complex)
F4 = np.zeros(N, dtype=complex)

# --- f0: Square wave ---
F0[0] = 1/2
for i in range(1, N):
    if i % 2 == 1:  # odd
        F0[i] = 1j / (pi * i)
    else:
        F0[i] = 0

# --- f1: Sawtooth ---
F1[0] = 1/2
F1[1:] = 1j / (2 * pi * k[1:])

# --- f2: Triangle ---
F2[0] = 1/4
for i in range(1, N):
    if i % 2 == 1:
        F2[i] = -1 / (pi**2 * i**2)
    else:
        F2[i] = 0

# --- f3: Pulse ---
F3[0] = 1/4
F3[1:] = -1j * (1 - (-1j)**k[1:]) / (2 * pi * k[1:])

# --- f4: Rectified sine ---
F4[:] = 2 / (pi * (1 - 4 * k**2))

theory = [F0, F1, F2, F3, F4]


fig, axes = plt.subplots(5, 1, figsize=(7, 12))

for i, f in enumerate(functions):
    vals = f(ts)
    ft = fft.fft(vals) / N
    
    half = N // 2
    
    axes[i].plot(np.abs(ft[:half]), 'o', label="FFT")
    axes[i].plot(np.abs(theory[i][:half]), '-', label="Theory")
    
    axes[i].set_title(f"f{i}")
    axes[i].set_xlabel("k")
    axes[i].set_ylabel("|coefficient|")
    axes[i].legend()

plt.tight_layout()
plt.show()
