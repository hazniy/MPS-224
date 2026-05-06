Write a function make_dodecahedron(). It should return a tuple (vertices, edges) as follows.
vertices should be a numpy array of shape (3,20), whose columns give the coordinates of the vertices of the dodecahedron as described in the lab briefing.
edges should be a numpy array of shape (30,2) with integer data type. The rows should be all the pairs [i,j] with 0≤i<j<20
 such that ∥vi−vj∥
 takes the minimum possible value.
Do not import matplotlib or include a %matplotlib directive or call any plotting commands.
Note: The vertex coordinates depend on the size and orientation of the dodecahedron, and the internet will find you various different sets of coordinates for various different sizes and orientations. For this question, you need to use the coordinates as specified in the lab briefing.




Write a function phi(t, x) which calculates solitons as described in the lab briefing. The formulae are as follows:
qrT=2–√=x−4t=32cosh(2r−p)+16cosh(2s−p)+16psB=log(3+2q)=q(x−8t)=4(1+q)cosh(r)cosh(s)+(4q−8)er+s

ϕ0(t,x)ϕ2(t,x)ϕ4(t,x)=2cosh(r)−2=2cosh(r−p)−2=T/B2.ϕ1(t,x)ϕ3(t,x)=4cosh(s)−2=4cosh(s−p)−2


Your function should return the vector (ϕ0(t,x),…,ϕ4(t,x))
. You should make sure that your function works correctly when t
 and x
 are arrays of the same shape. For example, if t
 and x
 both have shape (10,100)
, then ϕ(t,x)
 should have shape (5,10,100)
.


Do not import matplotlib or include a %matplotlib directive or call any plotting commands.
