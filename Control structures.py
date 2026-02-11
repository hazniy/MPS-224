#FOR
for i in range (1,10):
    j = i * i 
    print(f"The square of {i} is {j}")

#WHILE
i = 1 
while i * i < 42: 
    print(f"The square of {i} is {i*i}, which is less than 42")
    i = i + 1
print(f"The square of {i} is {i*i}, which is greater than or equal to 42 ") #print this when i * i not < 42

#FOR IF
m = 196 
found = False 
for i in range(1000): 
    if i * i == m: 
        found = True 
        print(f"The square root of {m} is {i}")
        break #keep looping the i until i*i = m 
if not found: 
    print(f"No square root of {m} was found")

#DEF SQUARE ROOT
def int_sqrt(m, max_range = 1000):
    for i in range(1000): 
        if i * i == m: 
            print(f"The square root of {m} is {i}")
            return i
    print(f"No square root of {m} was found")
    return None
int_sqrt(625)
#if theres return, no need Found already 

#DEF fizz buzz 
def fizz_buzz(i): 
    s = ''
    if i % 3 == 0: 
        s = 'Fizz'
    if i % 5 == 0: 
        s = s + 'Buzz'
    if s == '': 
        s = str(i)
    return s 
fizz_buzz(100) #buzz
fizz_buzz(27) #fizz
fizz_buzz(105) #fizzbuzz
fizz_buzz(1) #1
for i in range(1,20):
    print(fizz_buzz(i)) #list down all the outcome range 1-19 
#or 
    print(f"{i} : {fizz_buzz(i)}") # list it in form 1 : 1...
    print(f"{i:2} : {fizz_buzz(i)}") #for line up 
