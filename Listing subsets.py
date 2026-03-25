import math
import unittest

def next_ramp(r, n):
    """ 
    This function expects r to be a ramp of some length m with upper bound n,
    and returns the next ramp (in lexicographic order) of the same length 
    and upper bound.  If r is already the last ramp, the function returns None.
    """
    i = len(r) - 1
    while i >= 0 and r[i] >= n:
        i -= 1
    if i < 0:
        return None
    return r[:i] + [r[i] + 1] * (len(r) - i)

def list_ramps_a(m, n):
    """
    This function returns the list of all ramps of length m with upper bound n,
    in lexicographic order.
    """
    if n < 0:
        return []
    r = [0] * m
    L = []
    while r is not None:
        L.append(r)
        r = next_ramp(r, n)
    return L

def list_ramps_b(m, n):
    """
    This function is supposed to return the list of all ramps of length m with 
    upper bound n, in lexicographic order.  However, it does not always do 
    this correctly.  
    """
    L = [[i] for i in range(n+1)]
    for k in range(m-1):
        L = [L[i] + [j] for i in range(len(L)) for j in range(L[i][-1], n+1)]
    return L

def list_ramps_c(m, n):
    """
    This function is supposed to return the list of all ramps of length m with 
    upper bound n, in lexicographic order.  However, it does not always do 
    this correctly.  
    """
    L = [[]]
    for k in range(m):
        L = [L[i] + [j] for i in range(len(L)) for j in range(max([0]+L[i]), n)]
    return L

def list_ramps_d(m, n):
    """
    This function is supposed to return the list of all ramps of length m with 
    upper bound n, in lexicographic order.  However, it does not always do 
    this correctly.  
    """
    if m == 0:
        return [[]]
    L = [[j] for j in range(n+1)]
    for k in range(m-1):
        L = [[j] + s for s in L for j in range(s[0]+1)]
    return L

list_ramps = list_ramps_a

def spread(r):
    """
    Given a ramp [r0, r1, r2, ...], this function returns the list
    [r0, r1+1, r2+2, ...] (which is strictly increasing and so can be 
    thought of as representing a subset of the integers).
    """
    return [i + x for i, x in enumerate(r)]

def list_subsets(m, n):
    """
    This function returns the list of all subsets of {0, 1, ..., n-1} of size m
    (with each subset represented as a strictly increasing list of integers, 
    and the list of subsets being in lexicographic order).
    If list_ramps is defined to be list_ramps_a, then this function is correct.
    If list_ramps is defined to be one of the other functions, then this function
    will not always give the right answer.
    """
    L = list_ramps(m, n-m)
    return [spread(r) for r in L]

class SubsetTest(unittest.TestCase):
    def setUp(self):
       self.max_n = 5
       self.max_m = 5

    def check_type(self, m, n):
        """Check that list_subsets(m,n) returns a list of lists, each of length m."""
        L = list_subsets(m,n)
        self.assertTrue(isinstance(L, list))
        self.assertTrue(all([(isinstance(s, list) & (len(s) == m)) for s in L]))

    def check_all_int(self, m, n):
        """Check that list_subsets(m,n) returns a list of lists of integers."""
        L = list_subsets(m,n)
        self.assertTrue(all([all([isinstance(s[i],int) for i in range(m)]) for s in L]))

    def check_all_in_range(self, m, n):
        """Check that list_subsets(m,n) returns a list of lists of integers in [0,n)."""
        L = list_subsets(m,n)
        self.assertTrue(all([all([0 <= s[i] < n for i in range(m)]) for s in L]))

    def check_all_sorted(self, m, n):
        """Check that the lists returned by list_subsets(m,n) are each strictly increasing."""
        L = list_subsets(m,n)
        self.assertTrue(all([all([s[i] < s[i+1] for i in range(m-1)]) for s in L]))

    def check_sorted(self, m, n):
        """
        Check that list_subsets(m,n) is itself strictly increasing wrt lexicographic order.
        Python automatically compares lists lexicographically, so we do not need to write
        any extra code for that.
        """
        L = list_subsets(m,n)
        self.assertTrue(all([L[i] < L[i+1] for i in range(len(L)-1)]))

    def check_length(self, m, n):
        """Check that list_subsets(m,n) returns exactly (n choose m) subsets."""
        self.assertEqual(len(list_subsets(m,n)), math.comb(n, m))

    def test_0_type(self):
        for m in range(self.max_m+1):
            for n in range(self.max_n+1):
                # The line 'with self.subTest(m=m, n=n):' ensures that if 
                # self.check_type(n, m) fails, the error message will include
                # the values of n and m that caused the failure.
                with self.subTest(m=m, n=n):
                    self.check_type(m, n)

    def test_1_all_sorted(self):
        for m in range(self.max_m+1):
            for n in range(self.max_n+1):
                with self.subTest(m=m, n=n):
                    self.check_all_sorted(m, n)

    def test_2_all_in_range(self):
        for m in range(self.max_m+1):
            for n in range(self.max_n+1):
                with self.subTest(m=m, n=n):
                    self.check_all_in_range(m, n)

    def test_3_sorted(self):
        for m in range(self.max_m+1):
            for n in range(self.max_n+1):
                with self.subTest(m=m, n=n):
                    self.check_sorted(m, n)

    def test_4_length(self):
        for m in range(self.max_m+1):
            for n in range(self.max_n+1):
                with self.subTest(m=m, n=n):
                    self.check_length(m, n)

list_ramps = list_ramps_a

unittest.main(argv=[''], verbosity=2, exit=False)
