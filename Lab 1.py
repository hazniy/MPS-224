#TASK 1
#accuracy
def SQRT(x):
    """mathematical concept: 
    start a guess (u). 
    - if u too high, x/u will be too low 
    - if u too low, x/u will be too high 
    taking average of u and x/u, we squeeze the error & land much closer to actual square root
    Know as Heron's method"""
    u = 1
    for i in range(10): 
        u = (u + x/u)/2 
    return u 
SQRT(25)

#Why our initial $u$ equal to $x/2$?  
#- For any $x \ge 4$, the square root $\sqrt{x}$ is always less than or equal to $x/2$.

#Whats abs means? 
#- abs is short for absolute value, like modulus 

#efficiency : For massive numbers (like x=1,000,000), it will automatically run for more iterations without you needing to manually change the range().
def SQRT(x):
    u = x / 2  # A slightly better starting guess than 1
    epsilon = 0.0000001  # How precise you want to be
    
    while True:
        next_u = (u + x/u) / 2
        # Check if the change is smaller than our tolerance
        if abs(u - next_u) < epsilon:
            break
        u = next_u
    return u
SQRT(25)

#other efficient way : compared with current with previous 
def SQRT_efficient(x):
    u = x / 2.0
    while True:
        prev_u = u
        u = (u + x/u) / 2
        if u == prev_u: # Stop when the value plateaus
            break
    return u
SQRT_efficient(25)

#math.sqrt : faster if you are only processing a single number.
#numpy.sqrt : calculate the square root of a list or array without needing a for loop.
import math
import numpy as np

# The number we want to calculate
number = 25

# 1. Using the math module (Standard Library)
res_math = math.sqrt(number)
print(f"Math sqrt: {res_math}")

# 2. Using NumPy (Great for lists/arrays)
res_numpy = np.sqrt(number)
print(f"NumPy sqrt: {res_numpy}")

# Bonus: NumPy's real power is handling multiple numbers at once
numbers = [4, 9, 16, 25]
res_array = np.sqrt(numbers)
print(f"NumPy array sqrt: {res_array}")


#TASK 2
