#Task 1
import numpy as np
import matplotlib.pyplot as plt

"""plot graph f(x) = x(1-x), g(x) = x(1-x)(1-2x), x = 0, x = 1"""
x = np.linspace(0, 1, 500) #x = 0, x= 1, 500 points 
f = x*(1-x)
g = x*(1-x)*(1-2*x)

fig, ax = plt.subplots()
ax.plot(x, f, 
        color = 'red',       
        linewidth = 2,          
        linestyle = '-',       
        label='f(x)', 
        )  
ax.plot(x, g, 
        color = 'blue',       
        linewidth = 2,          
        linestyle = '-',       
        label='g(x)'
        )

ax.set_xlabel('x') 
ax.set_ylabel('y') 
ax.set_title('Two functions')
ax.legend() 
plt.show()

#Task 2
import numpy as np
import matplotlib.pyplot as plt

def plot_lissajous(n, m):
    """plot Lissajous curve (x,y) = (sin(nt),cos(mt)) for 0<=t<=2pi"""
    t = np.linspace(0, 2*np.pi, 500)
    x = np.sin(n*t)
    y = np.cos(m*t)

    plt.figure(figsize=(5, 5))
    plt.plot(x, y,
            color='#aa4a44',
            linestyle='--')
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    plt.axis('off')

    plt.show()
    
plot_lissajous(3, 4)

#Task 3
import numpy as np
import matplotlib.pyplot as plt

# Create fine grid (1000 x 1000)
x = np.linspace(-11, 11, 1000)
y = np.linspace(-11, 11, 1000)
X, Y = np.meshgrid(x, y)

# Define function
F = X**2 + Y**2 + 20*np.sin(2*np.pi*X) + np.cos(2*np.pi*Y) - 100

# Plot
fig, ax = plt.subplots(figsize=(6,6))

# Implicit curve (level 0)
ax.contour(X, Y, F, levels=[0], colors='blue')

# Dotted circle of radius 10
theta = np.linspace(0, 2*np.pi, 500)
ax.plot(10*np.cos(theta), 10*np.sin(theta),
        linestyle=':', color='red')

ax.set_xlim(-11, 11)
ax.set_ylim(-11, 11)
ax.set_aspect('equal')

plt.show()

#Task 4
import numpy as np
import matplotlib.pyplot as plt

def show_bisect(f, a, b):
    
    # Call the given bisect function
    cs = bisect(f, a, b)
    
    # Fine grid for plotting f
    x = np.linspace(a, b, 1000)
    y = f(x)
    
    fig, ax = plt.subplots(figsize=(6, 4))
    
    # Plot f(x)
    ax.plot(x, y, color='blue')
    
    # Horizontal line y=0
    ax.axhline(0, color='black')
    
    # Draw dotted vertical lines for each approximate root
    for c in cs:
        yc = f(c)
        
        if yc > 0:
            colour = 'red'
        else:
            colour = 'green'
        
        ax.plot([c, c], [0, yc], linestyle=':', color=colour)
    
    ax.set_xlim(a, b)
    plt.show()
    
f = lambda x: 10*np.cos(x) - np.cos(10*x)

show_bisect(f, 0, np.pi)
