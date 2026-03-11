import numpy as np
import matplotlib.pyplot as plt

# Start defining the LaplaceSolver class
class LaplaceSolver:
    # Inside the class we have various def statements to define functions
    # These functions are methods of the class, and are called using notation like L.steps(100),
    # where L is an instance of the class Laplace.  In every method, the first argument is 
    # called self.  When we do L.steps(100), the self argument is automatically set to L.

    # The first method (known as the constructor) is called __init__, and is a bit different
    # from the other methods.  When we create a new Laplace solver with a line like
    # L = Laplace(x_min=-1, x_max=1, y_min=-1, y_max=1), the __init__ method is called
    # automatically to set things up.  The arguments x_min, x_max, y_min, and y_max are
    # passed through to the __init__ method, along with self (which is automatically set to L). 
    def __init__(self, x_min=0, x_max=1, y_min=0, y_max=1, nx=100, ny=100):
        # The next few lines just create a record of the input arguments.
        # This means that if we create a solver using L = Laplace(x_min=-10, x_max = 10),
        # then L.x_min will be -10 and L.x_max will be 10 and so on.
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.nx = nx
        self.ny = ny
        # We now set some extra attributes that are not just copies of the constructor arguments.
        self.dx = (x_max - x_min) / nx # gap between successive values of x
        self.dy = (y_max - y_min) / ny # gap between successive values of y
        self.xr = np.linspace(x_min, x_max, nx+1) # one-dimensional array of x values
        self.yc = np.linspace(y_min, y_max, ny+1) # one-dimensional array of y values
        self.x, self.y = np.meshgrid(self.xr, self.yc) # two-dimensional arrays of x and y values
        self.mask = np.zeros_like(self.x, dtype=int) # default value of the mask is zero
        self.potential = np.zeros_like(self.x) # default value of the potential is zero
        # For later use we also need a 2D array called odd, of the same shape as x and y
        # This has odd[i,j] = 1 if i+j is odd, and odd[i,j] = 0 if i+j is even
        self.odd = np.zeros_like(self.x)
        self.odd[1:-1:2, 0:-1:2] = 1
        self.odd[0:-1:2, 1:-1:2] = 1
        self.u = np.zeros_like(self.x) # Initial guess at the solution
        self.err = 1 # Later this will be an estimate of the error in the solution
        self.change = 1 # Later this will be an estimate of the change in the solution
                        # made at the last improvement step.
        self.f = 2.0 - 2*np.pi/np.sqrt(self.nx * self.ny) # The relaxation factor

    def set_edge_mask(self):
        """Set the mask to be the edge of the rectangle, so the domain D is the full rectangle."""
        self.mask[ :, :] = 0
        self.mask[ 0, :] = 1
        self.mask[-1, :] = 1
        self.mask[:,  0] = 1
        self.mask[:, -1] = 1

    def set_circle_mask(self, xc=0, yc=0, r=1):
        """Set the mask to be the outside of a circle, so the domain D is the inside."""
        self.mask = ((self.x - xc)**2 + (self.y - yc)**2 >= r**2) * 1

#set up initial value of u 
    def start(self):
        """Set the initial value of the solution. 

        Outside the domain D, the solution is set equal to the potential.  
        Inside the domain D, the solution is set equal to zero.
        """
        self.u = self.mask * self.potential

    def naive_step(self):
        """Make one step of the naive method, where we just average the neighbours.
        
        This works, but only very slowly.
        """
        # We make a copy of the current solution and then modify the copy.
        # The current solution is self.u, and the copy is called u.
        # We do this so that we can compare the new value of u with the old value of self.u
        # and thus calculate the size of the change.
        u = self.u.copy()
        # Points on the edge of the rectangle do not have four neighbours, so we cannot 
        # apply the usual averaging procedure.  In any sensible case they will not 
        # lie in the interior of D, so we will be setting the values there equal to the 
        # potential anyway.  We therefore ignore the edges.  The slice [1:-1, 1:-1]
        # refers to the part of the array u that does not include the edges.
        #
        # Similarly, u[1:-1,0:-2] gives the part of u where the left and right edges and 
        # the bottom two rows have been removed.  This means that the entries in 
        # u[1:-1,0:-2] are the northern neighbours of the points in u[1:-1,1:-1].
        # Similarly, u[1:-1,2:] gives the southern neighbours, u[0:-2,1:-1] gives the
        # western neighbours, and u[2:,1:-1] gives the eastern neighbours.
        # We can therefore add these four slices and multiply by 0.25 to get the average.
        u[1:-1, 1:-1] = 0.25 * (u[1:-1, 0:-2] + u[1:-1, 2:] + u[0:-2, 1:-1] + u[2:, 1:-1])
        # We now adjust u so that it is equal to the potential outside the domain D.
        u = u * (1 - self.mask) + self.potential * self.mask
        # We now calculate the size of the change in the solution
        self.change = np.max(np.abs(u - self.u))
        # We now calculate the error in the solution.  This only works correctly if 
        # we already knew the solution and we set the potential to be equal to the
        # correct solution in the first place.
        self.err = np.max(np.abs(u - self.potential))
        # Now set the current solution to be the new solution.
        self.u = u
        return (self.change, self.err)

#run improvement process x times 
    def step(self):
        # This implements a better method, which I learned from this paper:
        # "Numerical solution of Laplace's Equation", by Per Brinch Hansen
        # https://surface.syr.edu/cgi/viewcontent.cgi?article=1160&context=eecs_techreports
        # Say that a point (x[i,j], y[i,j]) is "odd" if i+j is odd, and "even" if i+j is even.
        # Note that all neighbours of an odd point are even, and all neighbours of an even point are odd.
        # We let r[i,j] be the residual at (x[i,j], y[i,j]), which is the difference between the average of the
        # neighbours and the value of the solution at (x[i,j], y[i,j]).  In the naive method, we just 
        # add r to u.  In this method, we instead add f*r to u, but only at the odd points.  
        # Here f is a parameter which is typically slightly less than 2, which is set in the constructor.
        # We then recalculate r, and add f*r to u at the even points.  Finally we adjust u so that it is equal
        # to the potential outside the domain D.
        u = self.u.copy()
        r  = np.zeros_like(self.u)
        r[1:-1, 1:-1] = 0.25 * (u[1:-1, 0:-2] + u[1:-1, 2:] + u[0:-2, 1:-1] + u[2:, 1:-1]) - u[1:-1, 1:-1]
        u[:,:] = u + self.f * r * self.odd
        r[1:-1, 1:-1] = 0.25 * (u[1:-1, 0:-2] + u[1:-1, 2:] + u[0:-2, 1:-1] + u[2:, 1:-1]) - u[1:-1, 1:-1]
        u[:,:] = u + self.f * r * (1 - self.odd)
        u[:,:] = u * (1 - self.mask) + self.potential * self.mask
        self.change = np.max(np.abs(u - self.u))
        self.err = np.max(np.abs(u - self.potential))
        self.u = u
        return (self.change, self.err)

    def steps(self, n):
        """Call the step method n times, and return the change and the error."""
        for i in range(n):
            self.step()
        return (self.change, self.err)
    
    def show_mask(self, ax = None):
        """Make a plot showing the mask.
        
        Arguments:
        ax -- an axis object, or None.  If ax is None, then a new figure is created.

        Returns:
        ax -- the axis object, on which the mask has been drawn
        """
        if ax is None:
            fig, ax = plt.subplots()
        x = self.x.flatten()
        y = self.y.flatten()
        m = self.mask.flatten()
        ax.scatter(x[m==1], y[m==1], c = 'black', s = 2)
        ax.scatter(x[m==0], y[m==0], c = 'red', s = 1)
        return ax
    
    #plot results
    def show_contours(self, ax = None):
        """Make a plot showing the solution as a set of contours.
        
        Arguments:
        ax -- an axis object, or None.  If ax is None, then a new figure is created.

        Returns:
        ax -- the axis object, on which the contours have been drawn
        """
        if ax is None:
            fig, ax = plt.subplots()
        ax.contour(self.x, self.y, self.u * (1 - self.mask), 20)
        return ax
    
    def show_heatmap(self, ax = None):
        """Make a plot showing the solution as a heatmap.
        
        Arguments:
        ax -- an axis object, or None.  If ax is None, then a new figure is created.

        Returns:
        ax -- the axis object, on which the heatmap has been drawn
        """
        if ax is None:
            fig, ax = plt.subplots()
        ax.imshow(self.u * (1 - self.mask), origin='lower', extent=(self.x_min, self.x_max, self.y_min, self.y_max), cmap='plasma')
        return ax
    
L = LaplaceSolver(x_min=-1,x_max=1,y_min=-1,y_max=1)
L.set_circle_mask()
L.potential = L.x ** 3 - 3 * L.x * L.y ** 2
L.start()
L.steps(1000)
fig,ax = plt.subplots(1,3, figsize=(15,5))
for i in range(3):
    ax[i].set_aspect('equal')
    ax[i].axis('off')
L.show_mask(ax[0])
L.show_heatmap(ax[1])
L.show_contours(ax[2])

M = LaplaceSolver(x_min=-1,x_max=1,y_min=-1,y_max=1)
M.set_edge_mask()
M.potential = 2 - np.abs(M.x) - np.abs(M.y)
M.start()
M.steps(10000)
print(f"change = {M.change}")
fig,ax = plt.subplots(1,3, figsize=(15,5))
for i in range(3):
    ax[i].set_aspect('equal')
    ax[i].axis('off')
M.show_mask(ax[0])
M.show_heatmap(ax[1])
M.show_contours(ax[2])
