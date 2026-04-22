#Task 1: the periodic table 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d
from sklearn.cluster import KMeans
# %matplotlib widget

df = pd.read_csv("elements.csv")
df
df.shape[1] #num of columns
sorted(df["Type"].unique()) #list all types, in order, without repetitions
df.groupby("Type").size() #how many elements for each type
gases_df = df[df["Phase"] == "gas"][["Element", "Symbol"]].reset_index(drop=True)
gases_df #list names & symbol that gas & reset index 
ds = df[df["Element"] == "Darmstadtium"] #extract row for darmstadtium
ds_clean = ds.dropna(axis=1) #remove Nan 
ds_clean
idx = df["Boiling Point (K)"].argmax() #locate highest boiling point element
df.loc[idx]

type_colours = pd.DataFrame([
       ['Alkali Metal','purple'],
       ['Alkaline Earth Metal','blue'],
       ['Halogen','cyan'],
       ['Transition Metal','green'],
       ['Metal','yellow'],
       ['Metalloid','orange'],
       ['Nonmetal','red'],
       ['Noble Gas','grey'],
       ['Actinide','brown'],
       ['Transactinide','purple'],
       ['Lanthanide','pink']
      ],columns=['Type','Colour'])

df = df.merge(type_colours,how='left',on='Type') #merge colour column 

#build periodic table 
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(12, 6))

# Loop through each element
for _, row in df.iterrows():
    x = row["Display Column"]
    y = row["Display Row"]
    symbol = row["Symbol"]
    colour = row["Colour_x"]
    
    # Place the text (element symbol)
    ax.text(x, y, symbol,
            ha='center', va='center',
            fontsize=10,
            color='black',
            bbox=dict(facecolor=colour, edgecolor='black'))

# Flip y-axis so row 1 is at the top (like periodic table)
ax.invert_yaxis()

# Set limits to frame everything properly
ax.set_xlim(0.5, df["Display Column"].max() + 0.5)
ax.set_ylim(df["Display Row"].max() + 0.5, 0.5)

# Remove axes
ax.axis('off')

# Draw outer box (this fixes layout issues)
rect = plt.Rectangle(
    (0.5, 0.5),
    df["Display Column"].max(),
    df["Display Row"].max(),
    fill=False,
    edgecolor='black',
    linewidth=2
)
ax.add_patch(rect)

plt.show()

## Q1
def count_elements_by_type(df):
    return df.groupby("Type").size().sort_values(ascending=False)

## Q2
def gasses_only(df):
    result = df[df["Phase"] == "gas"][["Element", "Symbol"]]
    result = result.rename(columns={"Element": "Element"})
    return result.reset_index(drop=True)

## Q3
def highest_bp_element(df):
    idx = df["Boiling Point (K)"].argmax()
    return df.loc[idx, "Element"]

## Q4 
def Ds_stripped(df):
    ds = df[df["Element"] == "Darmstadtium"]   # extract row
    ds_clean = ds.dropna(axis=1)              # remove NaN columns
    return ds_clean.squeeze()                 # convert to Series
  
#Task 2: Whitby tides 
import pandas as pd

data = []

with open('whitby_tides.txt') as f:
    lines = f.readlines()

#a
# skip header lines (adjust if needed)
for line in lines[11:]:
    
    line = line.strip()
    
    # skip empty lines
    if line == "":
        continue

    parts = line.split()

    # extract date and time
    date_str = parts[1] + " " + parts[2]   # '2023/01/01 02:15:00'
    
    # convert to timestamp
    seconds = pd.Timestamp(date_str).timestamp()

    # start of year timestamp
    start_year = pd.Timestamp("2023-01-01 00:00:00").timestamp()

    # hours since start of year
    hours = (seconds - start_year) / 3600

    # tide level (4th column)
    level_str = parts[3]

    # remove trailing M if present
    level_str = level_str.replace("M", "").replace("N", "").replace("T", "")
    level = float(level_str)

    # skip missing data
    if level == -99:
        continue

    data.append([hours, level])

# convert to DataFrame
df_tides = pd.DataFrame(data, columns=["time", "level"])

df_tides

#b
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10,5))

plt.plot(df_tides["time"], df_tides["level"])

# vertical lines every 24 hours
max_time = df_tides["time"].max()
for t in np.arange(0, max_time, 24):
    plt.axvline(t, linestyle="dotted", color="grey", linewidth=0.8)

plt.xlabel("Time (hours since start of year)")
plt.ylabel("Tide level")
plt.title("Whitby Tide Levels")

plt.show()

#c
tau = [
     12.4206012,  # Principal lunar semidiurnal
     12,          # Principal solar semidiurnal
     12.65834751, # Larger lunar elliptic semidiurnal
     23.93447213, # Lunar diurnal
     6.210300601, # Shallow water overtides of principal lunar
     25.81933871, # Lunar diurnal
     4.140200401, # Shallow water overtides of principal lunar
     8.177140247, # Shallow water terdiurnal
     6            # Shallow water overtides of principal solar
    ]

omega = 2*np.pi/np.array(tau)

def p(t, *a):
    result = a[0]
    k = 1

    for w in omega:
        result += a[k] * np.cos(w*t)
        result += a[k+1] * np.sin(w*t)
        k += 2

    return result

from scipy.optimize import curve_fit
a0 = np.zeros(1 + 2*len(omega))
params, _ = curve_fit(p, df_tides["time"], df_tides["level"], p0=a0)

import matplotlib.pyplot as plt
import numpy as np

# filter data range
mask = (df_tides["time"] >= 1000) & (df_tides["time"] <= 2000)

t_data = df_tides["time"][mask]
y_data = df_tides["level"][mask]

# smooth model curve
t_model = np.linspace(1000, 2000, 1000)
y_model = p(t_model, *params)

plt.figure(figsize=(10,5))

# actual data
plt.plot(t_data, y_data, label="Actual tide")

# model
plt.plot(t_model, y_model, label="Model", linewidth=2)

plt.xlabel("Time (hours)")
plt.ylabel("Tide level")
plt.title("Tide data vs fitted harmonic model")
plt.legend()

plt.show()

## Q5 
def p(t, *a):
    t = np.expand_dims(t, axis=0)   # make t shape (1, N)

    result = a[0]

    for i, w in enumerate(omega):
        result += a[2*i + 1] * np.cos(w * t)
        result += a[2*i + 2] * np.sin(w * t)

    return result
#Task 3: Spurious correlations 
#Task 4: Fruit and vegetables 
