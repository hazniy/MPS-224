import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

#future reference, the difference between pi/2 and I7
I7 = 467807924713440738696537864469/935615849440640907310521750000 * np.pi
print(f"The difference between I7 and pi/2 is {np.pi/2 - I7}")

#define f0(x)...f7(x)
m0 = 1
m1 = 3
m2 = 3*5
m3 = 3*5*7
m4 = 3*5*7*9
m5 = 3*5*7*9*11
m6 = 3*5*7*9*11*13
m7 = 3*5*7*9*11*13*15

#define fk(x) themselves
f0 = lambda x: m0 * np.sin(x) / x 
f1 = lambda x: m1 * np.sin(x) * np.sin(x/3) / x ** 2
f2 = lambda x: m2 * np.sin(x) * np.sin(x/3) * np.sin(x/5) / x ** 3
f3 = lambda x: m3 * np.sin(x) * np.sin(x/3) * np.sin(x/5) * np.sin(x/7) / x ** 4
f4 = lambda x: m4 * np.sin(x) * np.sin(x/3) * np.sin(x/5) * np.sin(x/7) * np.sin(x/9) / x ** 5
f5 = lambda x: m5 * np.sin(x) * np.sin(x/3) * np.sin(x/5) * np.sin(x/7) * np.sin(x/9) * np.sin(x/11) /  x ** 6
f6 = lambda x: m6 * np.sin(x) * np.sin(x/3) * np.sin(x/5) * np.sin(x/7) * np.sin(x/9) * np.sin(x/11) * np.sin(x/13) / x ** 7
f7 = lambda x: m7 * np.sin(x) * np.sin(x/3) * np.sin(x/5) * np.sin(x/7) * np.sin(x/9) * np.sin(x/11) * np.sin(x/13) *  np.sin(x/15) / x ** 8

#other ways, more efficient rather than do 1b1
def fn_basic(n, x):
    m = np.arange(1, 2*n+3, 2) # m = [1, 3, 5, ... , 2*n+1]
    # Note that x / m is the array [x/1, x/3, x/5, ... , x/(2*n+1)]
    # so np.sin(x / m) is the array [sin(x/1), sin(x/3), sin(x/5), ... , sin(x/(2*n+1))]
    # Also the .prod() method gives the product of all the elements in the array
    return m.prod() * np.sin(x / m).prod() / x ** (n+1)

#fn_basic(7, x) only works when x is a scalar not x an array 

#eliminate the error 
def fn(n):
    def f(x):
        u = np.expand_dims(x,-1) / np.arange(1, 2*n+3, 2)
        return (np.sin(u) / u).prod(axis=-1)
    return f
x = 42
print(f7(x), fn_basic(7, x), fn(7)(x))

#or 
x = np.array([[1,2,3],[4,5,6]])
print(f7(x))
print(fn(7)(x))
print(np.array([[fn_basic(7, a) for a in r] for r in x])) # same as above, but not vectorized
# print(fn_basic(7, x)) # gives an error, as explained above

#plot f6(x) and f7(x) 
xs = np.linspace(0.01, 20, 1000)
fig, ax = plt.subplots(1,2)
fig.set_figwidth(15)
ax[0].plot(xs, fn(6)(xs), 'r-', label=r"$f_6(x)$")
ax[1].plot(xs, fn(7)(xs), 'b-', label=r"$f_7(x)$")
ax[0].spines['bottom'].set_position('zero') # put the bottom spine at y=0
ax[1].spines['bottom'].set_position('zero') # put the bottom spine at y=0
ax[0].legend()
ax[1].legend()
#identical, f7(x) is close to f6(x) 

#calculate integarl infnity x=0 f(x) dx
def I(f):
    """Compute the integral of f from 0 to infinity.

    Parameters:
    f (function): the function to integrate.

    Returns:
    A pair of numbers: the value of the integral and an estimate of the error.
    """
    return sp.integrate.quad(f, 0, np.inf, limit=5000, epsabs=1e-14, epsrel=1e-14)

def check_I(f, u):
    """Check the integral of f against the expected value u."""
    integral, err = I(f)
    print(f"Approximate integral           = {integral}")
    print(f"Error estimated by scipy       = {err}")
    print(f"Difference from expected value = {integral - u}\n")

check_I(f4, np.pi/2)
check_I(f5, np.pi/2)
check_I(f6, np.pi/2)
check_I(f7, I7)

#trapezium rule will only give the exact answer if the degree is zero or one.
def trapezium_rule(f, a, b, n):
    """Compute the integral of f from a to b using the trapezium rule.

    Parameters:
    f (function): the function to integrate.
    a (float): the lower limit of integration.
    b (float): the upper limit of integration.
    n (int): the number of subintervals to use.

    Returns:
    The value of the integral.
    """
    x = np.linspace(a, b, n+1) # n+1 points make n subintervals
    y = f(x)
    return (b-a) * (np.sum(y) - 0.5 * (y[0] + y[-1])) / n

#Simpson's rule will give the exact answer for the integral (even with  n=2)
def simpsons_rule(f, a, b, n):
    """Compute the integral of f from a to b using Simpson's rule.

    Parameters:
    f (function): the function to integrate.
    a (float): the lower limit of integration.
    b (float): the upper limit of integration.
    n (int): the number of subintervals to use.

    Returns:
    The value of the integral.
    """
    if not (isinstance(n, int) and n > 0 and n % 2 == 0):
        raise ValueError("n must be an even positive integer")
    x = np.linspace(a, b, n+1) # n+1 points make n subintervals
    y = f(x)
    h = (b-a) / n
    return h/3 * (y[0] + y[-1] + 2*np.sum(y[2:-1:2]) + 4*np.sum(y[1:-1:2]))

def scipy_rule(f, a, b, n):
   return sp.integrate.quad(f, a, b, limit=5000, epsabs=1e-14, epsrel=1e-14)[0]

def check_rule(rule, f, a, b, n):
    """Check the integral of f using the given rule."""
    int = rule(f, a, b, n)
    true_int = scipy_rule(f, a, b, n)
    print(f"Approximate integral = {int}")
    print(f"Accurate integral    = {true_int}")
    print(f"Difference           = {int - true_int}")
    print('')

#Above we claimed that Simpson's rule gives the exact answer for cubic polynomials. We now check a case of this
def p(x):
    return 4 + 6*x + 17*x**2 - 3*x**3

check_rule(simpsons_rule, p, 4, 7, 2)

#five-point gaussian quadrature
gauss5_points = np.array([
    -np.sqrt(5 + 2*np.sqrt(10/7))/3, 
    -np.sqrt(5 - 2*np.sqrt(10/7))/3,
     0,
     np.sqrt(5 - 2*np.sqrt(10/7))/3,
     np.sqrt(5 + 2*np.sqrt(10/7))/3,
])

gauss5_weights = np.array([
    (322 - 13*np.sqrt(70))/900,  
    (322 + 13*np.sqrt(70))/900,
    128/225,
    (322 + 13*np.sqrt(70))/900,
    (322 - 13*np.sqrt(70))/900  
])

def gauss5_rule(f, a, b, n = None):
    """Compute the integral of f from a to b using a 5-point Gauss rule.

    Parameters:
    f (function): the function to integrate.
    a (float): the lower limit of integration.
    b (float): the upper limit of integration.
    n (int): ignored, included for compatibility with other functions.

    Returns:
    The value of the integral.
    """
    x = 0.5 * (b-a) * gauss5_points + 0.5 * (b+a)
    return 0.5 * (b-a) * np.sum(gauss5_weights * f(x))

def split_gauss5_rule(f, a, b, n):
    return np.array([gauss5_rule(f, a+i*(b-a)/n, a+(i+1)*(b-a)/n) for i in range(n)]).sum()

#check all the rules 
def p5(x):
    return x * (x - 1) * (x - 2) * (x - 3) * (x - 4) * (x - 5)

check_rule(trapezium_rule, p5, 1, 6, 100)
check_rule(simpsons_rule, p5, 1, 6, 100)
check_rule(gauss5_rule, p5, 1, 6, None) #the moss accurate one 

#try calculate integral 10 1 sin9x) dx
check_rule(trapezium_rule, np.sin, 1, 10, 100)
check_rule(simpsons_rule, np.sin, 1, 10, 100)
check_rule(gauss5_rule, np.sin, 1, 10, None)
check_rule(split_gauss5_rule, np.sin, 1, 10, 5)

#try integral infinity 0 f7(x)
print(f"trapezium rule  : {trapezium_rule(   fn(7), 1e-14, 1000, 1000) - I7}")
print(f"Simpson's rule  : {simpsons_rule(    fn(7), 1e-14, 1000, 1000) - I7}")
print(f"split Gauss rule: {split_gauss5_rule(fn(7), 1e-14, 1000, 1000) - I7}")
print(f"scipy rule      : {scipy_rule(       fn(7), 1e-14, 1000, None) - I7}")
