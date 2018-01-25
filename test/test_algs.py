import numpy as np
from example import algs

def test_pointless_sort():
    # generate random vector of length 10
    x = np.random.rand(10)

    # check that pointless_sort always returns [1,2,3]
    assert np.array_equal(algs.pointless_sort(x), np.array([1,2,3]))

    # generate a new random vector of length 10
    x = np.random.rand(10)

    # check that pointless_sort still returns [1,2,3]
    assert np.array_equal(algs.pointless_sort(x), np.array([1,2,3]))

def test_bubblesort():
    # Actually test bubblesort here. It might be useful to think about
    # some edge cases for your code, where it might fail. Some things to
    # think about: (1) does your code handle 0-element arrays without
    # failing, (2) does your code handle characters?

    x = np.array([1,2,4,0,1])
    
    s, conds, assigns = algs.bubblesort(x)
    assert np.array_equal(s, np.array([0, 1, 1, 2, 4]))

    ### Test negative elements 
    xneg = np.array([-1, 0, 5, 2, -10])
    s, conds, assigns = algs.bubblesort(xneg)
    assert np.array_equal(s, np.array([-10, -1, 0, 2, 5]))

    ### test duplicated elements
    xdup = np.array([1,1, 0, 5, 10])
    s, conds, assigns = algs.bubblesort(xdup)
    assert np.array_equal(s, np.array([0, 1, 1, 5, 10]))

    xeven = np.array([0, 1, 5, 0, 2, -1])
    s, conds, assigns = algs.bubblesort(xeven)
    assert np.array_equal(s, np.array([-1, 0, 0, 1, 2, 5]))

    ### Test empty length vector
    xempty = np.array([])
    s, conds, assigns = algs.bubblesort(xempty)
    assert np.array_equal(s, np.array([]))

    ### test character arrays
    xchar = np.array(["c", "a", "d", "b", "a"])
    s, conds, assigns = algs.bubblesort(xchar)
    assert np.array_equal(s, np.array(["a", "a", "b", "c", "d"]))

    ### test word arrays
    xwords = np.array(["apple", "aardvark", "banana", "accentuate", "down"])
    s, conds, assigns = algs.bubblesort(xwords)
    assert np.array_equal(s, np.array(["aardvark", "accentuate", "apple", "banana", "down"]))

def test_quicksort():

    x = np.array([1,2,4,0,1])
    s, conds, assigns = algs.quicksort(x)
    assert np.array_equal(s, np.array([0, 1, 1, 2, 4]))

    ### Test negative elements
    xneg = np.array([-1, 0, 5, 2, -10])
    s, conds, assigns = algs.quicksort(xneg)
    assert np.array_equal(s, np.array([-10, -1, 0, 2, 5])) 

    ### test duplicated elements
    xdup = np.array([1,1, 0, 5, 10])
    s, conds, assigns = algs.quicksort(xdup)
    assert np.array_equal(s, np.array([0, 1, 1, 5, 10]))

    ### test even length vectors 
    xeven = np.array([0, 1, 5, 0, 2, -1])
    s, conds, assigns = algs.quicksort(xeven)
    assert np.array_equal(s, np.array([-1, 0, 0, 1, 2, 5]))

    ### Test empty length vector
    xempty = np.array([])
    s, conds, assigns = algs.quicksort(xempty)
    assert np.array_equal(s, np.array([]))

    ### test character arrays
    xchar = np.array(["c", "a", "d", "b", "a"])
    s, conds, assigns = algs.quicksort(xchar)
    assert np.array_equal(s, np.array(["a", "a", "b", "c", "d"]))

    ### Test word arrays
    xwords = np.array(["apple", "aardvark", "banana", "accentuate", "down"])
    s, conds, assigns = algs.quicksort(xwords)
    assert np.array_equal(s, np.array(["aardvark", "accentuate", "apple", "banana", "down"]))


def time_bubblesort():

    sizes = np.arange(100, 1000, 100)
    times = []
    print(sizes)
    for size in sizes:
        arrs = []


