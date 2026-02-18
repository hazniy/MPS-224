import numpy as np 
A = np.array([[11,22],[33,44]])
B = np.array([[1,10],[100,1000]])
print(A)
print(B)
A*B #this is called broadcasting

q = np.array([[1,10,100]])
print(q)
print(q.T) #transpose
print(q.ndim) #num dimension
print(q.shape) #matrix shape 
q_broadcast = np.hstack((q,q,q,q,q)) 
print(q_broadcast) #expand the array 5 times hori

q_broadcast = np.vstack((q,q,q,q,q)) 
print(q_broadcast)#expand the array 5 times verti
