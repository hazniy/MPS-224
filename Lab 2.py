#Task 1: Row sum norm and condition numbers
from numpy import max, sum, abs, array, zeros
from numpy.linalg import inv

H = zeros((2, 2))
print(H)

def hilbert_matrix(n):
    """"assignment ; H i,j = 1/i+j+1 for indices starting at 0
        wikipedia ; H i,j = 1/i+j-1 bcs it indexes from 1 
        so not an error, just diff indexing"""
    """"logic: 
        1. create nxn zero matrix 
        2. fill entry (i,j) with: 1/(i+j+1)"""
    H = zeros((n, n))
    for i in range(n):
        for j in range(n):
            H[i, j] = 1 / (i + j + 1)
    return H

def row_sum_norm(A):
    """"for a matrix A: 
        - take absolute value of every entry 
        - for each row, compute the sum 
        - take the max of those row sums
        e.g. ∥A∥=max(∣a∣+∣b∣,∣c∣+∣d∣)"""
    """logic: 
        1. abs(A) #take absolute values
        2. sum(abs(A), axis=1) #sum across row
        axis = 0, sum down the columns, vert 
        axis = 1, sum across the rows, hori
        3. max(...) #take the max"""
    row_sums = sum(abs(A), axis=1)
    return max(row_sums)

#other way to calc row sum norm : 
p = float('inf')

def condition_number(A):
    """"cond(A) = ∥A∥⋅∥A^−1∥"""
    """logic: 
        1. Compute row sum norm of A
        2. Compute inverse of A using inv(A)
        3. Compute row sum norm of inverse
        4. Multiply"""
    A_inv = inv(A)
    return row_sum_norm(A) * row_sum_norm(A_inv)

#other way to calc condition number : 
numpy.linalg.cond(A, p)

#submit 
def row_sum_norm(A):
    row_sums = sum(abs(A), axis=1)
    return max(row_sums)
  
def condition_number(A):
    A_inv = inv(A)
    return row_sum_norm(A) * row_sum_norm(A_inv)


#Task 2: Onion matrices
  import numpy as np

def onion(v): 
    """"given vector v = [a,b,c] and build matrix 5x5 which
    a's outer, b's second, c's in the middle
    so if len(v) = 1, matrix = 1x1, len(v) = 2, matrix 3x3, len(v) = 3, matrix = 5x5
    hence size = 2n - 1"""
    n = len(v)
    size = 2*n - 1
    M = np.zeros((size, size))
    
    for i in range(size):
        for j in range(size):
            layer = min(i, j, size-1-i, size-1-j) #closest edge determines the layer
            # i = Distance to top edge
            # j = Distance to left edge
            # size-1-i = Distance to bottom edge
            # size-1-j = Distance to right edge
            M[i, j] = v[layer]
    return M

v = np.array([5])
print(onion(v))

v = np.array([1,2])
print(onion(v))

v = np.array([1,2,3])
print(onion(v))

#submit 
import numpy as np

def onion(v): 
    n = len(v)
    size = 2*n - 1
    M = np.zeros((size, size))
    
    for i in range(size):
        for j in range(size):
            layer = min(i, j, size-1-i, size-1-j) 
            M[i, j] = v[layer]
    return M

  
#Task 3: Moving average
import numpy as np

def a(n,k): 
    """"calculates ak for the given value of n
    - for k<n, ak=k, e.g. 0,1,2,...,n-1
    - for k>=n, ak=average of previous n numbers, 
      e.g. ak = ak-n + ak-n+1 + ... + ak-1/n"""
    """clear example : n = 3
    a0 = 0
    a1 = 1
    a2 = 2
    a3 = (0+1+2)/3 = 1
    a4 = (1+2+1)/3 = 4/3
    a5 = (2+1+4/3)/3 = 13/9
    """
   # Create array to store values from a0 to ak
    values = np.zeros(k+1)
    
    # First part: a_k = k for k < n
    for i in range(min(n, k+1)):
        values[i] = i
    
    # Second part: moving average
    for i in range(n, k+1):
        values[i] = np.mean(values[i-n:i])
    
    return values[k] 

print(a(3, 0))   # 0
print(a(3, 1))   # 1
print(a(3, 2))   # 2
print(a(3, 3))   # 1
print(a(3, 4))   # 4/3

#submit 
import numpy as np

def a(n,k): 
    values = np.zeros(k+1)

    for i in range(min(n, k+1)):
        values[i] = i
    
    for i in range(n, k+1):
        values[i] = np.mean(values[i-n:i])
    
    return values[k] 

  
#Task 4: Matrix exponentials
#exp(A) = ∑∞k=0 A^k/k!, exactly like normal exponential!
#but A^0 = I(identity matrix), A^1 = A, A^2 =A@A etc
# @ = matrix multiplication, like * 

import numpy as np 

def matrix_exp(A): 
    """logic
    1. Uses the series formula
    2. Stops when the next term is very small
    3. Returns the matrix exponential"""
    n = A.shape[0]
    
    S = np.eye(n)        # Sum starts with I
    T = np.eye(n)        # First term is I
    k = 0
    
    while np.max(np.abs(T)) > 1e-9: #common good compromise
        k += 1
        T = A @ T / k
        S = S + T
    
    return S

A = np.zeros((2,2))
print(matrix_exp(A))
