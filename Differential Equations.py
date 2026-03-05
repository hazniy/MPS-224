from spicy.integrate 
#1D
def dxdt(t, x) : 
  return (x*1-x)

x0 = 0.5 #initial value 
ts = np.linspace(0, 5, 100) 
solve_ivp(dxdt, (ts[0], ts[-1]),[x0], t_eval=ts) 
print(sol.y.shape) #1D, 6 value 
plt.plot(sol.t,sol.y[0],'red line') 

#2D - van der pol oscillator 
#x. = first derivative 
#1. first order reduction 
def dZdt(t,z, a=1): 
  x,y = Z 
return [y, a*(1-x**2)*y-x] 

ts = np.linspace(0,20,100) 
ic =  [0.5,0] 
sol= solve_ivp(dZdt, (ts[0], ts[-1]), ic, t_eval = ts, args=(2,)) #args change a

plt.plot(ts, sol.y[0], '-') 
