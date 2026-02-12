#TASK 1
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


#TASK 3
