## PRocesses that run in parallel
### CPU-Bound Tasks-Tasks that are heavy on CPU usage (e.g., mathematical computations, data processing).
## PArallel execution- Multiple cores of the CPU


## Runnung function as independent process
import multiprocessing
import time

def square_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Square of {i} is {i**2}")

def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"cube of {i} is {i*i*i}")

## Unline multithreading, here the function is not being executed by thread but by process in seperate memory, so we 
# create entry point with __init__

if __name__ == "__main__":      ## This is an entry point, where the execution of code starts
    ## Create 3 Process
    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)

    # Start the process
    t1 = time.time()
    p1.start()
    p2.start()


    ## Wait for process to complete
    p1.join()
    p2.join()

    tf = time.time() - t1
    print(f"Total time: {tf:1.3f}")