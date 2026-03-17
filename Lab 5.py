#Task 1: Integration over the unit disc 
#f(x,y)dxdy = unit disc D, x^2+y^2<=1
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

#gives exact integral 
def disc_int_monomial(i, j):
    if i % 2 == 1 or j % 2 == 1:
        return 0
    
    num = math.gamma((i+1)/2) * math.gamma((j+1)/2)
    den = math.gamma((i+j)/2 + 2)
    
    return num / den

#cubature rule 
def extend_disc_rule(u0):
    
    rows = []
    
    for x, y, w in u0:
        
        if x == 0 and y == 0:
            rows.append([x,y,w,0])
        
        elif y == 0 and x != 0:
            pts = [(x,0),(-x,0),(0,x),(0,-x)]
            for px,py in pts:
                rows.append([px,py,w,1])
                
        elif x == y:
            pts = [(x,x),(-x,x),(x,-x),(-x,-x)]
            for px,py in pts:
                rows.append([px,py,w,2])
                
        else:
            pts = [
                (x,y),(-x,y),(x,-y),(-x,-y),
                (y,x),(-y,x),(y,-x),(-y,-x)
            ]
            for px,py in pts:
                rows.append([px,py,w,3])
    
    return np.array(rows)

#plot of a rule u consisting of rows [x,y,w,t]
def show_disc_rule(u):
    
    fig, ax = plt.subplots()
    
    ax.add_patch(Circle((0,0),1,fill=False))
    
    colors = {0:'black',1:'red',2:'green',3:'blue'}
    
    for x,y,w,t in u:
        ax.scatter(x,y,s=200*w,color=colors[t])
    
    ax.set_aspect('equal')
    ax.axis('off')
    
    plt.show()

#numerical integral 
def disc_int(f,u):
    
    total = 0
    
    for x,y,w,t in u:
        total += w * f(x,y)
        
    return total

#test 
kim_song_rule0 = np.array([
    [0,0,0.114983341799985660],
    [0.42463390374323367,0,0.087938325357145539],
    [0.69446902308083445,0,0.076206570461793249],
    [0.88696766316393713,0,0.042666281539386779],
    [0.23562252091530831,0.23562252091530831,0.095664962820418119],
    [0.59664767781455707,0.59664767781455707,0.062085722273139239],
    [0.68785354082699271,0.68785354082699271,0.019156522218855521],
    [0.54894025523701459,0.31294754888343992,0.085162533604288747],
    [0.79035487531148609,0.30538732225214729,0.056834571713156972],
    [0.84937290409632805,0.46270056598293749,0.024268628331345539],
    [0.96121228504617867,0.17385745088683603,0.020201237989565462]
    ])
kim_song_rule = extend_disc_rule(kim_song_rule0)
disc_int(lambda x,y: x**2 * y**4, kim_song_rule)
disc_int_monomial(2,4)

#submit Q1
def disc_int_monomial(i, j):
    """use binomial summation, if odd power the integral is zero, if i>j then use symmetry"""
    if i % 2 == 1 or j % 2 == 1:
        return 0.0
    if i > j:
        return disc_int_monomial(j, i)
    k = i // 2
    l = j // 2
    s = 0
    for m in range(l-k, l+k+1):
        term = ((-1)**(l+m) *
                math.comb(2*l, m) *
                math.comb(2*k, k+l-m))
        s = s + term
    value = math.pi * s / (4**(k+l) * (k+l+1))
    return value
#test value
disc_int_monomial(0,0)
disc_int_monomial(2,0)
disc_int_monomial(3,2)

#Submit Q2
import numpy as np

def extend_disc_rule(u0): 
    rows = []
    for x, y, w in u0:
        if x == 0 and y == 0:
            rows.append([0, 0, w, 0])
        
        elif x * y == 0:
            pts = [
                (x,y), (-x,y), (x,-y), (-x,-y),
                (y,x), (-y,x), (y,-x), (-y,-x)
            ]
            pts = list(set(pts))  # remove duplicates
            for px, py in pts:
                rows.append([px, py, w, 1])
        
        elif abs(x) == abs(y):
            pts = [(x,y), (-x,y), (x,-y), (-x,-y)]
            for px, py in pts:
                rows.append([px, py, w, 2])
        
        else:
            pts = [
                (x,y), (-x,y), (x,-y), (-x,-y),
                (y,x), (-y,x), (y,-x), (-y,-x)
            ]
            for px, py in pts:
                rows.append([px, py, w, 3])
    
    return np.array(rows)

#Test value 
u0 = np.array([
[0,0,0.2],
[0.5,0,0.05],
[0.625,0.625,0.05],
[0.875,0.125,0.05]
])
extend_disc_rule(u0)

#submit Q3
def disc_int(f,u):
    """f = function of 2 variables (x,y) with x^2+y^2 < 1
    u = numpy array shape (m,4) for some m"""
    total = 0
    for x,y,w,t in u:
        total = total + w * f(x,y)
    return total

#Test Value 
u = np.array([
[0,0,0.5,0],
[0.5,0,0.25,1],
[-0.5,0,0.25,1]
])
f = lambda x,y: x**2 + y**2
disc_int(f,u)
  
#Task 2 : Roots of the Wilkinson polynomial
#polynomials basic 
import numpy as np
np.array([2,-3,4,-5]) #2x^3-3x^2+4x-5 
np.convolve([1,-1],[1,-2]) #(x-1)(x-2) = multiplying
np.roots(p) #finding roots 
import numpy as np
import matplotlib.pyplot as plt

def wilkinson_poly(n, epsilon=0):
    """returns a numpy array containing list of coefficients of pn,E(x)"""
    p = np.array([1.0]) 
    for k in range(1, n+1):
        p = np.convolve(p, [1, -k])  #loop multiplies by (x-k) 
    p[1] = p[1] + epsilon
    return p
  
#Test Value 
wilkinson_poly(3,0.1)

#compute roots 
def wilkinson_roots(n, epsilon=0):
    
    p = wilkinson_poly(n, epsilon)
    
    return np.roots(p) #returns array of complex roots 

#argand diagram, plot the roots in the complex plane 
#real part = x-axis 
#imaginary part = y-axis 
def wilkinson_roots_argand_plot(n, epsilon=0):
    
    r = wilkinson_roots(n, epsilon)
    
    plt.scatter(r.real, r.imag)
    
    plt.xlabel("Real")
    plt.ylabel("Imaginary")
    
    plt.axhline(0)
    plt.axvline(0)
    
    plt.title(f"Roots of Wilkinson Polynomial n={n}, ε={epsilon}")
    
    plt.show()
    
#how roots move when E changes 
def wilkinson_roots_real_part_plot(n):
    
    eps = np.linspace(0,1,100)
    
    for e in eps:
        r = wilkinson_roots(n, e)
        plt.scatter([e]*len(r), r.real, s=5)
    
    plt.xlabel("epsilon")
    plt.ylabel("Real part of roots")
    
    plt.title(f"Real parts of roots for n={n}")
    
    plt.show()
    
def wilkinson_roots_imag_part_plot(n):
    
    eps = np.linspace(0,1,100)
    
    for e in eps:
        r = wilkinson_roots(n, e)
        plt.scatter([e]*len(r), r.imag, s=5)
    
    plt.xlabel("epsilon")
    plt.ylabel("Imaginary part of roots")
    
    plt.title(f"Imaginary parts of roots for n={n}")
    
    plt.show()

#test 
wilkinson_poly(2)
wilkinson_poly(3)
wilkinson_poly(3, 0.01)
wilkinson_roots(3)
wilkinson_roots(5, 0.0001)
wilkinson_roots_argand_plot(10)
wilkinson_roots_argand_plot(20, 1e-7)
wilkinson_roots_real_part_plot(10)
wilkinson_roots_imag_part_plot(10)

#Submit Q4 
def wilkinson_poly(n, epsilon=0):
    """returns a numpy array containing list of coefficients of pn,E(x)"""
    p = np.array([1.0]) #1
    for k in range(1, n+1):
        p = np.convolve(p, [1, -k])  #loop multiplies by (x-k) 
    eps_poly = np.zeros(n+1)
    eps_poly[1] = epsilon
    return p + eps_poly
  
#Test Value 
wilkinson_poly(3,0.1)
