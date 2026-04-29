#Synthetic signals
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

#Task 2: Electrocardiograms 
#read types.txt and allow access by both index and code 
def make_ecg_dict():
    ecg_dict = {}
    
    with open('/content/ecg/types.txt', 'r') as f:
        for line in f:
            parts = line.strip().split(',')
            index = int(parts[0])
            code = parts[1]
            full_name = parts[2]
            
            entry = (index, code, full_name)
            
            ecg_dict[index] = entry
            ecg_dict[code] = entry
    
    return ecg_dict


# create dictionary
ecg_dict = make_ecg_dict()

#extract .mat data 
import scipy.io

mat = scipy.io.loadmat('/content/ecg/AFIB' + '.mat')
data = mat['val'].squeeze()

import numpy as np
import scipy.io

def get_ecg_data(n):
    index, code, full_name = ecg_dict[n]
    
    mat = scipy.io.loadmat('/content/ecg/' + code + '.mat')
    
    # extract signal
    data = mat['val'].squeeze()
    
    return (index, code, full_name, data)

#normalise + plot + find peaks
import matplotlib.pyplot as plt
import scipy.signal

index, code, full_name, x = get_ecg_data('AFIB')

# normalise
x = (x - np.mean(x)) / np.std(x)

# time axis (360 Hz)
t = np.arange(len(x)) / 360

# find peaks (tune parameters if needed)
peaks, _ = scipy.signal.find_peaks(x, height=0.5, distance=100)

plt.figure(figsize=(12,4))
plt.plot(t, x)
plt.scatter(t[peaks], x[peaks], color='red')
plt.title(full_name)
plt.xlabel('Time (s)')
plt.show()

# average spacing
spacing = np.diff(peaks) / 360
print("Average peak spacing (seconds):", np.mean(spacing))

#high pass filter 
filter = scipy.signal.butter(4, 0.2, 'high', output='sos')
x_filtered = scipy.signal.sosfilt(filter, x)

# discard first 2 seconds
x_filtered = x_filtered[2*360:]
t_filtered = np.arange(len(x_filtered)) / 360

plt.figure(figsize=(12,4))
plt.plot(t_filtered, x_filtered)
plt.title('High-pass filtered')
plt.show()

#power spectrum (periodogram)
fs, ps = scipy.signal.periodogram(x, fs=360)

# keep frequencies ≤ 50 Hz
mask = fs <= 50
fs = fs[mask]
ps = ps[mask]

plt.figure(figsize=(12,4))
plt.plot(fs, ps)
plt.title('Power spectrum')
plt.xlabel('Frequency (Hz)')
plt.show()

def show_ecg(n):
    index, code, full_name, x = get_ecg_data(n)
    
    # normalise
    x = (x - np.mean(x)) / np.std(x)
    t = np.arange(len(x)) / 360
    
    # peaks
    peaks, _ = scipy.signal.find_peaks(x, height=0.5, distance=100)
    
    # high-pass filter
    filter = scipy.signal.butter(4, 0.2, 'high', output='sos')
    x_filtered = scipy.signal.sosfilt(filter, x)
    
    # discard first 2 seconds
    x_filtered = x_filtered[2*360:]
    t_filtered = np.arange(len(x_filtered)) / 360
    
    # periodogram
    fs, ps = scipy.signal.periodogram(x, fs=360)
    mask = fs <= 50
    fs = fs[mask]
    ps = ps[mask]
    
    # plotting
    fig, ax = plt.subplots(1, 3, figsize=(12,4))
    
    # original + peaks
    ax[0].plot(t, x)
    ax[0].scatter(t[peaks], x[peaks], color='red')
    ax[0].set_title(full_name)
    ax[0].set_xlabel('Time (s)')
    
    # filtered
    ax[1].plot(t_filtered, x_filtered)
    ax[1].set_title('High-pass filtered')
    
    # power spectrum
    ax[2].plot(fs, ps)
    ax[2].set_title('Power spectrum')
    ax[2].set_xlabel('Frequency (Hz)')
    
    plt.tight_layout()
    plt.show()

#Q4 
def make_ecg_dict():
    """
    Reads the file 'types.txt' and returns a dictionary mapping both
    index numbers and codes to tuples of the form: (index, code, full_name).
    """
    ecg_dict = {}
    
    with open('types.txt', 'r') as f:
        for line in f:
            parts = line.strip().split(',')
            index = int(parts[0])
            code = parts[1]
            full_name = parts[2]
            
            entry = (index, code, full_name)
            
            ecg_dict[index] = entry
            ecg_dict[code] = entry
    
    return ecg_dict

#Q5 
def get_ecg_data(n):
    """
    Returns ECG data corresponding to the given index or code.
    """
    index, code, full_name = ecg_dict[n]
    
    mat = scipy.io.loadmat(code + '.mat')
    data = mat['val'].squeeze()
    
    return (index, code, full_name, data)

#Task 3: Birdsong 
