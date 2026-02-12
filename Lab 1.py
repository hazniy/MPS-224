#TASK 1 : square roots 
#accuracy
def SQRT(x):
    """mathematical concept: 
    start a guess (u). 
    - if u too high, x/u will be too low 
    - if u too low, x/u will be too high 
    taking average of u and x/u, we squeeze the error & land much closer to actual square root
    Know as Heron's method"""
    u = 1
    for i in range(10): 
        u = (u + x/u)/2 
    return u 
SQRT(25)

#Why our initial $u$ equal to $x/2$?  
#- For any $x \ge 4$, the square root $\sqrt{x}$ is always less than or equal to $x/2$.

#Whats abs means? 
#- abs is short for absolute value, like modulus 

#efficiency : For massive numbers (like x=1,000,000), it will automatically run for more iterations without you needing to manually change the range().
def SQRT(x):
    u = x / 2  # A slightly better starting guess than 1
    epsilon = 0.0000001  # How precise you want to be
    
    while True:
        next_u = (u + x/u) / 2
        # Check if the change is smaller than our tolerance
        if abs(u - next_u) < epsilon:
            break
        u = next_u
    return u
SQRT(25)

#other efficient way : compared with current with previous 
def SQRT_efficient(x):
    u = x / 2.0
    while True:
        prev_u = u
        u = (u + x/u) / 2
        if u == prev_u: # Stop when the value plateaus
            break
    return u
SQRT_efficient(25)

#math.sqrt : faster if you are only processing a single number.
#numpy.sqrt : calculate the square root of a list or array without needing a for loop.
import math
import numpy as np

# The number we want to calculate
number = 25

# 1. Using the math module (Standard Library)
res_math = math.sqrt(number)
print(f"Math sqrt: {res_math}")

# 2. Using NumPy (Great for lists/arrays)
res_numpy = np.sqrt(number)
print(f"NumPy sqrt: {res_numpy}")

# Bonus: NumPy's real power is handling multiple numbers at once
numbers = [4, 9, 16, 25]
res_array = np.sqrt(numbers)
print(f"NumPy array sqrt: {res_array}")


#TASK 2
#without slicing
def is_double(word): 
    new_word = ''
    length = len(word)
    if length % 2 == 0: 
        for i in range(length//2): 
            char = word[i]
            new_word = new_word + char
        n = 0
        is_match = True
        while n < length//2: 
            if word[n] != word[length//2 + n]: 
                is_match = False
                break
            n += 1
        return is_match
    return False
is_double('bonbon')  

###basic slicing 
word = 'hazniy'
mid = len(word)//2
print(word[:mid])
print(word[mid:])

#slicing 
def is_double(word):
    length = len(word)
    
    # If it's odd, it can't be a perfect double
    if length % 2 != 0:
        return False
    
    mid = length // 2
    first_half = word[:mid]
    second_half = word[mid:]
    
    return first_half == second_half

print(is_double('bonbon')) # Returns: True
print(is_double('apple'))  # Returns: False

#shorter version
def is_double(word):
    length = len(word)
    half = length // 2
    return length % 2 == 0 and word[:half] == word[half:]
is_double('bonbon')

###print word for word 
word_list = ['alia', 'aliu']
print([word for word in word_list])
print(*(word for word in word_list)) #unpacking, now in array 

###to split string and add comma 
def normalize_input(data):
    # Turns ['a, b', 'c'] or ['a, b, c'] into ['a', 'b', 'c']
    full_string = " ".join(data).replace(',', ' ')
    return full_string.split()
normalize_input(['alia, bonbon, bonbim']) #word by word
normalize_input('alia, bonbon, bonbim') #by letter

def filter_double(word_list):
    # This reads like a sentence: "Give me the word for every word 
    # in the list, but only if is_double(word) is True."
    return [word for word in word_list if is_double(word)]
filter_double(['alia', 'bonbon', 'bonbim'])

def filter_double(word_list):
    # filter() returns an iterator, so we wrap it in list() 
    # to get a usable list back.
    return list(filter(is_double, word_list))
filter_double(['alia', 'bonbon', 'bonbim'])

#this one considering how user input the string too 
def filter_double(input_list):
    # Check if the user accidentally passed one long string inside a list
    if len(input_list) == 1 and ',' in input_list[0]:
        # Split by comma and strip whitespace from each name
        input_list = [item.strip() for item in input_list[0].split(',')]

    result = []
    for word in input_list:
        if is_double(word): # Assuming this is your logic
            result.append(word)
    return result
filter_double(['alia', 'bonbon', 'bonbim'])
filter_double(['alia, bonbon, bonbim'])

#Clean version : 
def is_double(word):
    length = len(word)
    half = length // 2
    return length % 2 == 0 and word[:half] == word[half:]
#will return True or False here 

def filter_double(input_list):
    # Check if the user accidentally passed one long string inside a list
    if len(input_list) == 1 and ',' in input_list[0]:
        # Split by comma and strip whitespace from each name
        input_list = [item.strip() for item in input_list[0].split(',')]

    result = []
    for word in input_list:
        if is_double(word): # Assuming this is your logic
            result.append(word)
    return result
filter_double(['alia, bonbon, roro'])


#TASK 3 : Pisano Periods (sequence always starts with 0,1)
#For pisano sequence, why 1 % N, what this means?
#- $%$ equal to remainder 

#What's isinstance()
#- isinstance(object, type) : checks whether a value belongs to a certain data type (class).

# Pisano periods : the period with which the sequence of Fibonacci numbers modulo N becomes periodic.
def pisano_sequence(N,n): 
    """
    n = number of terms 
    N = num dividing by to find the remainder / The "ceiling" or divisor. All numbers in your list will be less than N 
    """
    if not (isinstance(N, int) and isinstance(n, int) and N > 0 and n > 0): 
        return False
    if n == 1: 
        return [0 % N] #which is 0  
    
    seq = [0 % N,1 % N]
    
    for i in range(2,n): 
        next_term = (seq[-1] + seq[-2]) % N
        seq.append(next_term)
    return seq
pisano_sequence(3,4)

def pisano_period(N):
    """
    Every Fibonacci sequence modulo N eventually repeats. 
    Since the next number in a Fibonacci sequence depends only on the previous two, 
    the sequence "starts over" as soon as we see the pattern 0, 1 again. 
    Your job is to find how many steps it takes to get back to that 0, 1 start.
    
    Returns the period of the Fibonacci sequence modulo N. The period always starts with 0,1 
    Logic :  Start with F_0 = 0 and F_1 = 1. Calculate F_2, F_3, ... one by one.
    """
    # 1. Check if N is a strictly positive integer
    if not (isinstance(N, int) and N > 0):
        return False
    
    # 2. Special case for N=1
    if N == 1:
        return 1

    prev = 0
    curr = 1
    period = 0
    
    while True:
        next_term = (prev + curr) % N
        prev = curr
        curr = next_term
        period += 1
        
        if prev == 0 and curr == 1:
            return period
    
pisano_period(3)
