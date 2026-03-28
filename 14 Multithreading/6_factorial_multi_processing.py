'''
Real-World Example: Multiprocessing for CPU-bound Tasks
Scenario: Factorial Calculation
Factorial calculations, especially for large numbers, 
involve significant computational work. Multiprocessing 
can be used to distribute the workload across multiple 
CPU cores, improving performance.

'''

import multiprocessing
import math
import sys
import time
from concurrent.futures import ProcessPoolExecutor

# Increase the maximum number of digits for integer conversion
sys.set_int_max_str_digits(100000)

## function to compute factorials of a given number 
def compute_factorial(number):
    print(f"Computing factorial of {number}")
    result = math.factorial(number)
    print(f"Factorial of {number} is {result}")
    return result

if __name__ == "__main__":
    numbers = [5000,6000,700,8000]

    t1 = time.time()

    # Create pool of worker processes
    with multiprocessing.Pool() as pool:    ##using all cpu cores
        results = pool.map(
            compute_factorial, numbers
        )

    t2 = time.time() - t1

    print(f"Results: {results}")
    print(t2)

    print(f"\n\n\n\n")


    # # Experiment
    # results = []
    # numbers = [5000,6000,700,8000]

    # t1 = time.time()

    # # Create pool of worker processes
    # with ProcessPoolExecutor(max_workers=3) as pool:    ##using all cpu cores
    #     results = pool.map(
    #         compute_factorial, numbers
    #     )

    # t2 = time.time() - t1

    # print(f"Results: {results}")
    # print(t2)