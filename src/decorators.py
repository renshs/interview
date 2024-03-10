from time import perf_counter
import functools
import numpy as np


def benchmark(func):
    @functools.wraps(func)
    def wrapper(*args):
        results = []
        for i in range(10):
            start = perf_counter()
            func(*args)
            end = perf_counter()
            duration = end - start
            results.append(duration)
        return (
            f"mean: {np.mean(results)} seconds\nstd: {np.std(results)} seconds"
        )

    return wrapper


def benchmark_simple(func):
    @functools.wraps(func)
    def wrapper(*args):
        start = perf_counter()
        func(*args)
        end = perf_counter()
        duration = end - start
        return f"result: {duration} sec"

    return wrapper
