import numpy as np
import pandas as pd
import geopy.distance

df = pd.read_csv('peak_district_hills.csv')

display(df)
display(df.describe())
display(df.info())
print(f"Columns: {list(df.columns)}")
print(f"Shape: {df.shape}")

df['Height'].sort_values().reset_index(drop=True).plot()
df['Height'].hist(bins=np.arange(200,700,50), legend=True)
df[['Height','Drop']].plot.hist()
county_words = sorted(list({w for s in df.County.unique() for w in s.split('/')}))
county_words

hicks_position = 53.38085, -1.48636
def hicks_distance(row):
    return geopy.distance.distance(hicks_position, (row["Latitude"], row["Longitude"])).km
df["Distance"] = df.apply(hicks_distance, axis=1)

df["Name"] = df["Name"].str.replace(r"\([A-Za-z' ]*\)","",regex=True)
df["Name"] = df["Name"].str.replace(r"\[[A-Za-z' ]*\]","",regex=True)
df["Name"] = df["Name"].str.replace(r"- [A-Za-z' ]*","",regex=True)
df["Name"] = df["Name"].str.strip()

def last_word(s):
    return s.split(' ')[-1]

df["Type"] = df["Name"].map(last_word)
df = df[["Name","Type","Height","Drop","Latitude","Longitude","Distance","County"]]

types = list(df["Type"].unique())
print("\n".join([' '.join(types[10*i:10*(i+1)]) for i in range(len(types)//10+1)]))

dft = df.groupby("Type") \
        .agg(count=('Name', 'size'), height=('Height', 'mean')) \
        .sort_values(by='height', ascending=False) \
        .reset_index()

dft[dft["count"] > 2]

display(df[0:5])
display(df.loc[0:5])
display(df.iloc[0:5])

# Some of the columns from a single row
display(df.loc[3,['Latitude','Longitude']])

# All the columns from the top row
df.loc[0]

print(df.at[3,"Latitude"])
print(df.iat[3,4])
len(df[df["Drop"] > 100])

df[df["County"].str.contains("Sheffield")]

df.assign(s=lambda x: 0.2*x.Height).plot.scatter(x='Longitude', y='Latitude', c='Drop', s='s', colormap='viridis')
