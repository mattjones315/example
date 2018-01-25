import numpy as np

def pointless_sort(x):
    """
    This function always returns the same values to show how testing
    works, check out the `test/test_alg.py` file to see.
    """
    return np.array([1,2,3])

def bubblesort(x):
    """
    Describe how you are sorting `x`
    """
    conds = 0
    assigns = 0

    if len(x) == 0:
        return x, conds, assigns

    for i in range(len(x)):
        for j in range(1, len(x) - i):
            conds += 1
            if x[j-1] > x[j]:
                assigns += 2
                x[j], x[j-1] = x[j-1], x[j]
    #print(conds, assigns)
    return x, conds, assigns

def quicksort(x):
    """
    Describe how you are sorting `x` 
    """

    if len(x) == 0:
        return x, 0, 0

    x, conds, assigns = quicksort_alg(x, 0, len(x)-1, 0,0)
    return x, conds, assigns

def quicksort_alg(x, p, r, conds=0, assigns=0):
    """
    Describe how you are sorting `x`
    """

    def partition(a, p, r):
        _conds, _assigns = 0, 0
        pi = a[p]
        left, pivot = p, p
        right = r

        while left < right:

            while left < len(a) and a[left] <= pi:
                left += 1

            while a[right] > pi:
                right -= 1

            _conds += 1
            if left < right:
                _assigns += 1
                a[left], a[right] = a[right], a[left]
        
        a[p] = a[right]
        a[right] = pi
        _assigns += 2
        return a, right, _conds, _assigns

    if r > p:
        a, piv, _conds, _assigns = partition(x, p, r)
        conds += _conds
        assigns += _assigns
        x, _condsr, _assignsr = quicksort_alg(a, p, piv-1, conds, assigns)
        x, _condsl, _assignsl = quicksort_alg(a, piv+1, r, conds, assigns)
        conds += _condsr + _condsl
        assigns += _assignsr + _assignsl

    return x, conds, assigns

