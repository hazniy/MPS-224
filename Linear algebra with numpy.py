import numpy as np 
import numpy.linalg as la 
I = np.eye(3) 
print(I)
#[[1. 0. 0.]
#[0. 1. 0.]
#[0. 0. 1.]]
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(A)

la.det(A) #determinant
la.inv(A) #inverse
np.abs(la.inv(A)) #absolute value 
np.max(A) #largest num in A
la.eig(A) #eigenvalues 
