import numpy as np 
u = np.array([1,2,3])
v = np.array([4,7,3])
u * 100 #array([100, 200, 300])
np.array(list(range(20))) #array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
np.arange(20,40) #give from 20-39
np.arange(20,40,5) #array([20, 25, 30, 35])
np.linspace(0,10,30) #gives equally space points 
np.zeros(3,2) #give zeros 3x2 matrix 
np.one((3,2)) #give 1 3x2 matrix 


p = np.array(list(range(20)))
p.shape #(20,)
n = np.eye(4)
n 
#array([[1., 0., 0., 0.],
      #[0., 1., 0., 0.],
      #[0., 0., 1., 0.],
      #[0., 0., 0., 1.]])
n.shape #(4, 4)
n.reshape((2,8))
#array([[1., 0., 0., 0., 0., 1., 0., 0.],
      #[0., 0., 1., 0., 0., 0., 0., 1.]])
      
A = np.array([[3,4],[-4,3]])
B = np.array([[1,1],[1,1]])
print(A)
print(B)
print(A@B)
#[[ 7  7]
#[-1 -1]]
