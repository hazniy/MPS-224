#pangram : sentence that contains every letter of the alphabet 
# Here we define a function using the keyword def
# There is further discussion of functions in the notebook functions.ipynb

# Note that there are three arguments, and the last one has a default value
# so it can be omitted.

# Note also that the function body is indented by four spaces.
# Directly after the function definition, we have a docstring which 
# explains how to use the function.
def is_multi_pangram(s, k, verbose=False):
    """Checks if a string is a k-fold multi-pangram.

    Args:
        s: A string.
        k: An integer.
        verbose: A boolean indicating whether to print an explanation.

    Returns:
        True if s is a k-fold multi-pangram, i.e. if s contains 
        all letters of the alphabet at least k times.  Here we
        do not distinguish between upper and lower case letters.
    """

    # First we use isinstance() to check that the arguments are of the correct type
    # If not, we raise a TypeError with a helpful error message.  This will be
    # displayed if the user calls the function with the wrong type of arguments.
    # There is further discussion of data types in the notebook data_types.ipynb
    if not isinstance(s, str):
        raise TypeError("s must be a string")
    
    if not (isinstance(k, int) and k > 0):
        raise TypeError("k must be a positive integer")
    
    # This is a local variable, which is only defined within this function.
    # If we try to refer to it outside the function, we will get an error.
    # There is further discussion of this kind of thing in the notebook scope.ipynb
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # We use a dictionary to count the number of occurrences of each letter
    # We use a dictionary comprehension to initialize the dictionary with
    # all letters of the alphabet given a count of zero.
    # There is further discussion of comprehensions in the notebook comprehension.ipynb
    # It would be equivalent to write counts = {'a': 0, 'b': 0, ..., 'z': 0}
    # but that would be tedious and error-prone.
    counts = {letter: 0 for letter in alphabet}

    # We now have a loop, which is one of the most basic control structures in Python.
    # There is further discussion of loops in the notebook control.ipynb
    # We also use the lower() method of strings to convert all letters to lower case.
    # There is further discussion of strings and their methods in the notebook strings.ipynb
    # Note that when we call s.lower() we get a new, lower case string, but s itself is not changed.
    # There is more discussion of this sort of thing in the notebook mutability.ipynb
    for letter in s.lower():
        if letter in alphabet: # ignore spaces, punctuation and other non-alphabetic characters
            counts[letter] += 1 # equivalent to counts[letter] = counts[letter] + 1

    for letter in alphabet:
        n = counts[letter]
        if n < k:
            if verbose:
                print(f"The string is not a {k}-fold multi-pangram.")
                if n == 0:
                    # Note the use of f-strings for formatting the output
                    # There is further discussion in the notebook formatting.ipynb
                    print(f"The letter {letter} does not occur at all.")
                elif n == 1:
                    print(f"The letter {letter} occurs only once.")
                else:
                    print(f"The letter {letter} occurs only {n} times.")
            return False
        
    if verbose:
        print(f"The string is a {k}-fold multi-pangram.")

    return True
  
test_string0 = "Sixty zippers were quickly picked from the woven jute bag.  Meanwhile, six big devils from Japan zoomed under the bed."
test_string1 = "The quick brown fox jumps over the lazy dog. How vexingly quick daft zebras jump!  Sphinx of black quartz, judge my vow."
is_multi_pangram(test_string0, 1, verbose=True)
is_multi_pangram(test_string0, 2, verbose=True)
#The string is a 1-fold multi-pangram. #each letter appears at least 1 times 
#The string is not a 2-fold multi-pangram. 
#The letter q occurs only once.
#False
is_multi_pangram(test_string1, 3, verbose=True)
is_multi_pangram(test_string1, 4, verbose=True)
#The string is a 3-fold multi-pangram.
#The string is not a 4-fold multi-pangram.
#The letter b occurs only 3 times. #why its not 4-fold, bcs of the b 
#False
