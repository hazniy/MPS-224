#https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_daily_mlo.txt.
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# We first read the data from the file.  The following code sets lines to be a list 
# of strings, one for each line in the file.
with open('co2_daily_mlo.txt') as f:
    lines = f.readlines()

# We now discard the comment lines, and parse each of the remaining lines into a list of numbers.
records = []
for i, line in enumerate(lines):
    if line.startswith('#'):
        continue
    fields = line.split()
    x = [int(fields[0]), int(fields[1]), int(fields[2]), float(fields[3]), float(fields[4])]
    records.append(x)

# We now convert the list of records into a pandas DataFrame.
# If it were not for the comment lines, we could have used pandas.read_fwf() instead
df = pd.DataFrame.from_records(records, columns=['year', 'month', 'day', 'decimal_date', 'co2'])

display(df.info())
display(df.describe())

df.plot(x='decimal_date', y='co2', title='$CO_2$ concentration at Mauna Loa Observatory')

def p(x, a0, a1, a2, b0, b1):
    return a0 + a1 * x + a2 * x * x + b0 * np.cos(2*np.pi*x) + b1 * np.sin(2*np.pi*x)

ab = curve_fit(p, df['decimal_date'], df['co2'], p0=[-3650,2,0,0,0])[0]

print(ab)

df['co2_pred'] = p(df['decimal_date'], *ab)

df.plot(x='decimal_date', y=['co2', 'co2_pred'], title='CO2 concentration at Mauna Loa Observatory')
plt.legend(['Measured $CO_2$ concentration', 'Modelled $CO_2$ concentration'])
