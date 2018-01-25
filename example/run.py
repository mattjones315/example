# You can do all of this in the `__main__.py` file, but this file exists
# to shows how to do relative import functions from another python file in
# the same directory as this one.
import numpy as np
from .algs import quicksort, bubblesort
import time
import matplotlib.pyplot as plt

def benchmark_conds_and_assigns():

    bconds = 0
    bassigns = 0
    qconds = 0
    qassigns = 0
    for i in np.arange(500):
        x = np.random.rand(50)
        s, _bconds, _bassigns = bubblesort(x)
        s, _qconds, _qassigns = quicksort(x)

        bconds += _bconds
        bassigns = _bassigns
        qconds += _qconds
        qassigns = _qassigns

    print(bconds / 50, bassigns / 50)
    print(qconds / 50, qassigns / 50)

def benchmark_timing():

    bb_timings = {}
    q_timings = {}
    for n in np.arange(100, 1000, 100):
        print(n)
        bb_times = []
        q_times = []
        for i in np.arange(100):
            x = np.random.rand(n)

            ## time bubblesort
            t0 = time.time()
            s, conds, assings = bubblesort(x)
            bb_times.append(time.time() - t0)

            ## time quicksort
            t0 = time.time()
            s, conds, assigns = quicksort(x)
            q_times.append(time.time() - t0)
            
        bb_times = np.array(bb_times)
        q_times = np.array(q_times)

        bb_timings[n] = bb_times
        q_timings[n] = q_times

    return bb_timings, q_timings

def plot_timings(bb, q):

    bb_means = {k: np.mean(v) for k,v in bb.items()}
    q_means = {k: np.mean(v) for k,v in q.items()}

    bb_sds = {k: np.std(v) for k,v in bb.items()}
    q_sds  = {k: np.std(v) for k,v in q.items()}

    plt.plot(bb_means.keys(), bb_means.values())
    plt.errorbar(bb_means.keys(), bb_means.values(), bb_sds.values())
    plt.xlabel("Input Size")
    plt.ylabel("CPU Seconds")
    plt.title("CPU Bencmarking of Bubblesort")
    plt.show()
    
    plt.plot(q_means.keys(), q_means.values())
    plt.errorbar(q_means.keys(), q_means.values(), q_sds.values())
    plt.xlabel("Input Size")
    plt.ylabel("CPU Seconds")
    plt.title("CPU Bencmarking of Quicksort")
    plt.show()

    
    plt.plot(bb_means.keys(), bb_means.values(), label="Bubblesort", color="red")
    plt.plot(q_means.keys(), q_means.values(), label="Quicksort", color="orange")
    plt.legend()
    plt.errorbar(bb_means.keys(), bb_means.values(), bb_sds.values(), color="red")
    plt.errorbar(q_means.keys(), q_means.values(), q_sds.values(), color="orange")
    plt.xlabel("Input Size")
    plt.ylabel("CPU Seconds")
    plt.title("Bencmarking comparison of Quicksort & Bubblesort")
    plt.show()

def run_stuff():
    """
    This function is called in `__main__.py`
    """
    print("This is `run()` from ", __file__)
    
    benchmark_conds_and_assigns()

    bb_timings, q_timings = benchmark_timing()
    
    plot_timings(bb_timings, q_timings)

    x = np.random.rand(10)

    print("Unsorted input: ", x)
    print("Bubble sort output: ", bubblesort(x)[0])
    print("Quick sort output: ", quicksort(x)[0])

