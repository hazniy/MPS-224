x = 1234
print(x)

def f(): 
    global x #This allows you to modify the variable outside of the current function scope
    x = 9999
    y = 5678 
    print(f'Inside f(), y = {y}') #Inside f(), y = 5678 
    print(f'Inside f(), x = {x}') #Inside f(), x = 9999
f()
x #become 9999 instead 1234

def z(w): 
    x = 9999
    y = 5678 
    w = -w
    print(f'Inside z(), y = {y}')
    print(f'Inside z(), x = {x}')
    print(f'Inside z(), w = {w}')
z(11111)
#Inside z(), y = 5678
#Inside z(), x = 9999
#Inside z(), w = -11111
t = 222
z(t)
#Inside z(), y = 5678
#Inside z(), x = 9999
#Inside z(), w = -222

#from other view/ example 
x = 111 # This has global scope
print(f'Outside the function, x={x}')

def f(a):
    b = 2 * a # Here we introduce a new variable with local scope
    print(f'Inside the function, b={b}')
    print(f'Inside the function, x={x}')
    return 3 * b

f(100)

print(f'Outside the function, we still have x={x}')
print(f'Outside the function, b={b}') # This will fail

#LIST 
def g(l): 
    l[0] = l[0] + 1000
    print(f'l is now {l}')
l = [1,2,3,4,5]
g(l) #l is now [1001, 2, 3, 4, 5]

#other example
l = [1,2,3,4]
def add_the_answer_to_l():
    l.append(42)
print(f'Originally             : {l=}')
add_the_answer_to_l()
print(f'After the function call: {l=}')
#Originally             : l=[1, 2, 3, 4]
#After the function call: l=[1, 2, 3, 4, 42]
