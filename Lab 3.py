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
