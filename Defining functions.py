def double(x): 
    return x * 2
double('abcd') #'abcdabcd'
double([1,2,3,4]) #double([1,2,3,4])
double(99) #198

def square(x):
    return x ** 2
square(1 + 1j) #2j

def emphasise(s, excitement=1, doubt=0):
    """Add emphasis to a string
    
    Parameters: 
    s : string to emphasise 
    excitement : num of exclamatio marks to add (defaults to 1)
    doubt : numb of question marks to add (defaults to 0)
    """
    return s + '!' * excitement + '?' * doubt 
emphasise('Hi') #Hi! the excitement = 1 state that must have 1 !
emphasise('Hi', 2, 3) #Hi!!???
emphasise('Hi', doubt = 7, excitement = 0) #Hi???????

#LATEX The Fibonacci numbers $f_n$ are defined by the following rules: we start with $f_0 = f_1 = 1$, and then we have $f_n=f_{n-1}+f_{n-2}$ for $i\geq 2$. Thus $f_2=f_0+f_1=1+1=2$, and $f_3=f_1+f_2=1+2=3$, and $f_4=f_2+f_3=2+3=5$ and so on.
def fibonacci(n): 
    """Return the list of the first n Fibonacci numbers"""
    if not(isinstance(n,int) and n>=0): 
        raise ValueError('n must be an integer >= 2')
    if n <= 1: 
        return 1
    fib = [1,1]
    for i in range(2,n): 
        fib.append(fib[-1] + fib[-2])
    return fib
fibonacci(10) #[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
#OR
def fibonacci(n):
    """Return the list of the first n Fibonacci numbers."""
    if not(isinstance(n, int)):
        raise TypeError('n must be a integer')
    if n < 2:
        raise ValueError('n must be a integer >= 2')
    fib = [1, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib
print(fibonacci(10)) #[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# print(fibonacci(1.5)) # Generates an error: we cannot compute the Fibonacci sequence for a non-integer value

#fibonacci numbers converges to the golden ratio
tau = (1 + 5 ** 0.5) / 2   # The true golden ratio
l  = fibonacci(100)      
tau_approx = l[-1] / l[-2] # The approximate golden ratio f_{99}/f_{98}
print(tau, tau_approx, tau - tau_approx)
