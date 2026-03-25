import numpy as np

def permutations(n):
    """
    Returns a list of all permutations of the list [0, 1, ..., n-1].
    """
    kf = 1 # In the k-th iteration, kf will be equal to k! 
    # At the end of the k-th iteration, P will be a matrix of size (k+1)! x (k+1) 
    # where each row is a permutation of [0,1,...,k]
    P = np.array([[0]], dtype=int)
    for k in range(1, n):
        kf *= k # kf used to be (k-1)!, this line sets it to k!
        # At this point P is the full list of permutations of [0,1,...,k-1].  We want 
        # to apply the operator T (explained above) to each of these permutations,
        # which will give us the full list of those permutations of [0,...,k] that
        # send 0 to 0.  To apply T to a single permutation, we just add one to all
        # entries and then insert 0 at the beginning.  To apply T to all permutations
        # in P simultaneously, we add one to all entries and then use np.hstack() to 
        # insert a new column of k! zeros on the left.  
        P = np.hstack((np.zeros((kf,1),dtype=int), P+1))
        # Now P has shape k! x (k+1).  To prepare for broadcasting, we reshape P to
        # have shape 1 x k! x (k+1), which amounts to just adding an extra pair of
        # square brackets around P.
        P = P.reshape(1,kf,k+1)
        # We now want to compose the permutations in P with all possible powers 
        # of the standard (k+1)-cycle c=(0,1,...,k).  Composing c^i with a 
        # permutation p is the same as adding i to each entry of p modulo k+1.
        # We can do this for all i in [0,...,k] in a single broadcast operation
        # as follows.
        P = np.mod(P + np.arange(k+1,dtype=int).reshape(k+1,1,1),k+1)
        # Now P contains all possible permutations of [0,...,k], but they are 
        # arranged as an array of shape (k+1) x k! x (k+1).  We reshape this 
        # array to have shape (k+1)! x (k+1).
        P = P.reshape((k+1)*kf,k+1)
    return P

def derangements(n):
    """
    Returns a list of all derangements of the list [0, 1, ..., n-1].
    """
    P = permutations(n)
    # Now P is an array of shape n! x n, where each row is a permutation of [0,1,...,n-1].
    # We subtract the array id=np.arange(n)=[0,...,n-1], which has shape (n,).  This is a 
    # broadcast operation that actually subtracts the array id from each row of P.
    # Let p be the permutation in row i of P.  Then the j-th entry of p-id is p[j]-j,
    # which is zero if and only if p[j]=j.  Thus, the array p-id has no zeros iff 
    # p[j] is never equal to j iff p is a derangement.  We could use 
    # np.all(p - id) to check this for a single permutation p.  To do this for all
    # rows in P simultaneously, we use the np.all() function with the axis=1 option.
    # This returns an array of booleans of shape (n!,) that is True in position i
    # iff the permutation in row i of P is a derangement.  We use this boolean array
    # to select the rows of P that correspond to derangements.  This is explained at
    # https://numpy.org/doc/stable/user/basics.indexing.html#boolean-array-indexing
    return P[np.all(P - np.arange(n) != 0,axis = 1)]

permutations(3)
derangements(4)
