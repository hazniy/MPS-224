import numpy as np
import matplotlib.pyplot as plt

def primes_up_to(n):
    """Return the list of all prime numbers that are less than or equal to n"""

    # We test all the numbers from 2 to n in order
    # To test whether i is prime, we check whether it is divisible
    # by any of the smaller primes that we have found already.
    # If i is not divisible by any of those primes, then i must itself
    # be prime, so we add it to our list of primes.
    # 
    # (The explanation above is not needed in order to use this function.
    # Because of that, it is appropriate for the explanation to be given
    # in a comment, not as part of the docstring.) 
    primes = []
    for i in range(2, n+1):
        for p in primes:
            if i % p == 0:
                # If i is divisible by p then we break out of the 
                # inner loop.
                break
        else:
            # The else clause for the inner loop is only executed
            # if we get to the end of that loop without hitting a
            # break statement.  Thus, if we get to this point, then
            # i is not divisible by any prime p < i, so i must 
            # itself be prime, so we add it to our list of primes.
            primes.append(i)
    return primes

prime_list = primes_up_to(541)
len(prime_list)

plt.plot(np.arange(len(prime_list)), prime_list, '.')

#prime number theory 
def nth_prime_approx(n):
    """Return an approximation to the nth prime number"""
    return n * (np.log(np.log(n)) + np.log(n) - 1)

int(nth_prime_approx(1000))

prime_list = primes_up_to(7920)
plt.plot(np.arange(1,1001), prime_list, ',')
xs = np.arange(2,1001)
ys = nth_prime_approx(xs)
plt.plot(xs, ys)
