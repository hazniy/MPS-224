import matplotlib.pyplot as plt
import numpy as np
import datetime
import scipy

df = 'ISS.txt'
with open(df) as f:
    lines = f.readlines() 

data = []
t_start = None
for line in lines:
    if not(line.startswith('202')):
        continue #skip any lines don not start like 2024
    x = line.split()
    t = int(datetime.datetime.strptime(line[0:19], '%Y-%m-%dT%H:%M:%S').timestamp()) #parse the time, specify how its formatted (4 year, 1 dash, 2 month, dash, 2 day, letter 'T'), num of second from beginning of 1970 
    if t_start is None:
        t_start = t
    data.append([t - t_start, float(x[1]), float(x[2]), float(x[3])])

data = np.array(data)
t0 = data[:,0].astype(int)
xyz0 = data[:,1:] #x,y,z : velocity 

#We subtract the timestamp of the beginning of the dataset to get the number of seconds since the beginning of the dataset. We also parse the x, y and z component as floating point numbers, and ignore the components of velocity.

#most taken at intervals 4 mins (240 secs)
#tidying up 
n = int(t0[-1]/240)
t = [0] #times inc by 240 secs 
xyz = [xyz0[0]] #corresponding x,y,z
for i in range(1,n):
    j = np.argmax(t0 >= i*240)
    s = (t0[j] - i*240)/(t0[j] - t0[j-1])
    t.append(i*240)
    xyz.append(xyz0[j] + s*(xyz0[j-1]-xyz0[j]))

t = np.array(t) / 3600
xyz = np.array(xyz)
x = xyz[:,0]
y = xyz[:,1]
z = xyz[:,2]

events = ['2024-04-26T02:50:00', '2024-04-26T17:00:00', '2024-04-30T12:00:00']
events = [(datetime.datetime.strptime(e, '%Y-%m-%dT%H:%M:%S').timestamp() - t_start) / (60 * 60) for e in events]
events = np.array(events)
events

def show_orbit(tmin = 0, tmax = 30):
    n = np.floor(tmin * 15).astype(int)
    m = np.ceil(tmax * 15).astype(int)
    t0 = t[n:m]
    x0 = x[n:m]
    y0 = y[n:m]
    z0 = z[n:m]
    plt.figure(figsize=(12,4))
    plt.plot(t0, x0,label='x')
    plt.plot(t0, y0,label='y')
    plt.plot(t0, z0,label='z')
    for e in events:
        if tmin <= e <= tmax:
            plt.axvline(e, color='k', linestyle='--')
    plt.legend()
    plt.show()
    fig, ax = plt.subplots(1, 3, figsize=(12,4))
    ax[0].plot(x0, y0)
    ax[0].set_title(r'$x$ against $y$')
    ax[1].plot(x0, z0)
    ax[1].set_title(r'$x$ against $z$')
    ax[2].plot(y0, z0)
    ax[2].set_title(r'$y$ against $z$')
    plt.show()

show_orbit(150,180)

fx, px = scipy.signal.periodogram(x, fs = 15)
fy, py = scipy.signal.periodogram(y, fs = 15)
fz, pz = scipy.signal.periodogram(z, fs = 15)
plt.plot(fx, px)
plt.plot(fy, py)
plt.plot(fz, pz)

pp = np.sqrt(px * px + py * py + pz * pz)
fig, ax = plt.subplots(1, 2, figsize=(12,6))
ax[0].plot(fx[2:-1], np.maximum(0,np.log(pp))[2:-1])
ax[1].plot(fx[460:480], np.maximum(0,np.log(pp))[460:480])

primary_frequency = fx[np.argmax(pp)]
secondary_frequency = fx[460:480][np.argmax(pp[460:480])]
primary_period_hours = 1 / primary_frequency
secondary_period_hours = 1 / secondary_frequency
primary_period_minutes = primary_period_hours * 60
secondary_period_minutes = secondary_period_hours * 60
print(f"The primary period is {primary_period_minutes:.3f} minutes")
print(f"The secondary period is {secondary_period_minutes:.3f} minutes")
print(f"The ratio is {primary_period_minutes / secondary_period_minutes:.3f}")

zx = []
for i in range(x.shape[0] - 1):
    if x[i] * x[i + 1] < 0:
        zx.append((i + x[i]/(x[i] - x[i + 1])) / 15)
zx = np.array(zx)
zx_even = zx[::2]
zx_odd = zx[1::2]
zxd_even = np.diff(zx_even)
zxd_odd = np.diff(zx_odd)
plt.plot(zx_even[1:], 60 * zxd_even,'r.')
plt.plot(zx_odd[1:], 60 * zxd_odd,'g.')
plt.axhline(primary_period_minutes, color='b', linestyle='--')
for e in events:
    plt.axvline(e, color='k', linestyle='--')
