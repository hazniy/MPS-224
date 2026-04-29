import numpy as np
import scipy
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
import pandas as pd
from IPython.display import Audio

instruments = ['clarinet','drum','flute','gong','guitar','oboe','saxophone','trumpet','violin']
df = '/content/instruments'

def play_sample(f):
    display(Audio(filename=df + f + '.wav'))

play_sample('/clarinet0')
play_sample('/trumpet1')

#reads sound file (using scipy.io.wavfile.read()) and converts to numpy array
#get rid of silence at beginning by let m,a,b
#focus times between a & b
def show_harmonics(f):
    u = wav.read(df + f + '.wav')[1].astype(np.float32) / (2 ** 15)
    m = np.max(np.abs(u)) #maximum intensity 
    a = np.argmax(np.abs(u) >= m/2) #first time
    b = len(u) - np.argmax(np.abs(u[::-1]) >= m/2) #last time where intensity at least m/2 
    u = u[a:b]
    p = np.abs(scipy.fft.fft(u))[:(b-a)//2] #take fourier transform of intensity -> amount of power in the signal at different frequencies
    q = np.argmax(p) #primary frequency with smaller amount of energy 
    n = np.max(p)
    fig, ax = plt.subplots(2,1)
    ax[0].plot(u[:1000])
    ax[1].plot(np.arange(8*q)/q, p[:8*q]/n)

    #make a plot in which a small part of the original signal is shown in the top half, and the Fourier transform is shown in the bottom half. In the Fourier transform plot, the axes and scales are arranged so that the peak is at (1,1).
show_harmonics('/flute0')
show_harmonics('/trumpet1')
show_harmonics('/guitar0')
show_harmonics('/gong0')
