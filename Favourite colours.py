import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d
from sklearn.cluster import KMeans
!pip install colour
from colour import Color

# %matplotlib widget

df = pd.read_csv("favourite_colours.csv")
df
df['fc_r'] = df['Favorite color'].apply(lambda c: int(c[1:3], 16))
df['fc_g'] = df['Favorite color'].apply(lambda c: int(c[3:5], 16))
df['fc_b'] = df['Favorite color'].apply(lambda c: int(c[5:7], 16))
n = 7
colour_matrix = np.array([df['fc_r'], df['fc_g'], df['fc_b']]).T
kmeans = KMeans(n_clusters=n, n_init=10)
kmeans.fit(colour_matrix)
None

df['ct'] = kmeans.labels_
cluster_cols = [f"#{d:06x}" for d in (np.rint(kmeans.cluster_centers_).astype(int) @ [16 ** 4,16 ** 2,1])]
cluster_cols

import matplotlib.colors as mcolors

def closest_color(hex_color):
    colors = mcolors.CSS4_COLORS
    min_dist = float("inf")
    closest = None
    
    for name, value in colors.items():
        r1, g1, b1 = mcolors.to_rgb(hex_color)
        r2, g2, b2 = mcolors.to_rgb(value)
        dist = (r1-r2)**2 + (g1-g2)**2 + (b1-b2)**2
        
        if dist < min_dist:
            min_dist = dist
            closest = name
            
    return closest

cluster_names = [closest_color(c) for c in cluster_cols]
cluster_counts = np.bincount(df['ct'])
plt.bar(range(n), cluster_counts, color = cluster_cols)
plt.xticks(range(n), cluster_names, rotation='vertical')
plt.show()
plt.pie(cluster_counts, labels=cluster_names, colors=cluster_cols)
plt.show()
None

data = [[cluster_cols[i], cluster_names[i], cluster_counts[i]] for i in range(n)]
data
