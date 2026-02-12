#TASK 1 
"""logic : 
- u = (u + x/u)/2
- while True : compared with previous u to minimize the loop
"""

#TASK 2
"""logic: 
- if the 1st half = 2nd half than its true
"""

"""logic: 
- we have to separate word in the list, if the length = 1, and [0] = , 
use item.strip() to remove any leading and trailing whitespaces
use .split(',') to splits string into a list
- use empty array, and is_double, and append the array
"""

#TASK 3
"""
n = number of terms 
N = num dividing by to find the remainder / The "ceiling" or divisor. All numbers in your list will be less than N
logic : 
- if not isinstance int, and >0 then return False  [positive int] 
- if n = 1 then return 0
- seq = [0,1] then loop (2,n), next term = (seq[-1] + seq[-2]) % N, then append seq
"""

""" 
logic : 
- positive integer 
- N = 1 then 1 
- previous = 0, current = 1, period = 0 
- while TRUE : next_term = (prev + current) % N, prev = current, current = next term, period += 1
- if prev = 0 and current = 1 then return period 
"""
