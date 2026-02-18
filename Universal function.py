import numpy as np
a = np.linspace(0,2*np.pi,101)  
a
np.round(np.sin(a),3) #round 3dp

a = np.arange(5)
b = 10 ** a
print(f'a    = {a}')
print(f'b    = {b}')
print(f'a+b  = {a+b}')
print(f'a*b  = {a*b}')
print(f'a**2 = {a ** 2}')

a = np.array([[1, 2],[3, 4]])
b = np.array([[100, 1000],[100, 1000]])
print(f'a = \n{a}')
print(f'b = \n{b}')
print(f'a * b = \n{a*b}')
print(f'a @ b = \n{a@b}') #arrays of appropriate shape

u = np.arange(1000)
print('Using universal function')
%timeit np.sin(u) #how long a piece of code takes
print('Using a loop')
%timeit [np.sin(x) for x in u]

#three different functions to generate a list of random numbers and calculate their variance
import random as rnd

def var0(n = 1000):
    l = []
    for i in range(n):
        l.append(rnd.random())
    sum_x = 0
    sum_x2 = 0
    for x in l:
        sum_x += x
        sum_x2 += x**2
    mean_x = sum_x / n
    mean_x2 = sum_x2 / n
    var = mean_x2 - mean_x**2
    return var

def var1(n = 1000):
    l = np.random.random(n)
    return (l ** 2).sum() / n - l.sum() ** 2 / n ** 2

def var2(n = 1000):
    return np.random.random(n).var()

print('Version 0')
%timeit -n100 var0(10000) #check the performance of these three alternatives
print('Version 1')
%timeit -n100 var1(10000) #7 groups of 100 runs of each function
print('Version 2')
%timeit -n100 var2(10000)
