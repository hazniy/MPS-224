import math
import numpy as np
import matplotlib.pyplot as plt

#matplotlib also generate pie charts, bar charts, histograms and so on 
labels = ['Those belonging to the Emperor', 
          'Embalmed ones', 
          'Mermaids', 
          'Stray dogs', 
          'Those that tremble as if they were mad',
          'Those that, at a distance, resemble flies']
short_labels = ['A', 'B', 'C', 'D', 'E', 'F']
sizes = [1, 4, 5, 6, 7, 8]
cols = ['red', 'green', 'blue', 'cyan', 'purple', 'orange']
None

plt.pie(sizes, labels=labels, colors=cols)
plt.title('Celestial Emporium of Benevolent Knowledge')
None

fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(short_labels, sizes, color=cols, label=labels)
ax.set_title('Celestial Emporium of Benevolent Knowledge')
ax.legend()

def heads(N=10):
    """Generate N random coin tosses and return the number of heads."""
    return sum(np.random.randint(0,2,N))

def make_coin_histogram(N = 16, M = 2 ** 15):
    """
    Generate M sets of N random coin tosses and plot the histogram of the 
    number of heads in each set.  Also plot the numbers predicted by the 
    binomial distribution.
    """
    X = [heads(N) for _ in range(M)]
    H = np.histogram(X, bins=N+1, range=(-0.5,N + 0.5), density=True) # unused
    plt.hist(X, bins=N+1, range=(-0.5,N + 0.5), density=True)
    plt.plot(range(N+1),[math.comb(N,i) * 0.5 ** N for i in range(N+1)],color='red')
    
make_coin_histogram(64, 2 ** 16)
