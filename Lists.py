[0, 1, 4, 9, 16]         # We can make a list by writing the entries in square brackets, separated by commas.
list(range(10))          # range(10) is a 'generator' which is essentially the list [0, 1, ..., 9]
[10 ** i for i in range(5)]   # We can use a 'list comprehension' to make a new list from an old one

a = ["aardvark"]               ; print(a) # Make a list with a single entry
a.append("cheetah")            ; print(a) # Add an entry at the end.  This changes a, but does not return anything.
a.insert(1, "baboon")          ; print(a) # Insert an entry at position 1 (not 0).  Again, this is an in-place operation.
a.extend(["dingo", "elephant"]); print(a) # Add multiple entries to the end of a list.
a.remove("dingo")              ; print(a) # Remove the first entry equal to "dingo".
a.reverse()                    ; print(a) # Reverse the order of the entries in a list.
a.sort()                       ; print(a) # Sort the entries, restoring the previous order

b = a + ["banana", "football"]
print(a)  # a is unchanged #['aardvark', 'baboon', 'cheetah', 'elephant']
print(b)  # b is a new list #['aardvark', 'baboon', 'cheetah', 'elephant', 'banana', 'football']
print(len(b))  # len() returns the length of a list #6

b[0], b[5] = b[5], b[0]  # Swap the first and last entries of b
print(b) #['football', 'baboon', 'cheetah', 'elephant', 'banana', 'aardvark']
