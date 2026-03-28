### Multithreading With Thread Pool Executor

from concurrent.futures import ThreadPoolExecutor
import time

def print_numbers(num):
    time.sleep(2)
    return f"Number:{num}"

numbers = [1,2,3,4,5]
a =len(numbers)-1   ## Made it dynamic

t1 = time.time()
with ThreadPoolExecutor(max_workers=a) as executor:     ## We are assiging three threads where they do the work
    results = executor.map(print_numbers,numbers)         # executor id called as context variable
t2 = time.time() -t1

for result in results:
    print(result)

print(t2)

# What happened here is, based on number of workers you assigned using ThreadPoolExecutor,
# the execution of program in completed that fast. 
# Try changing the max_worker, you will notice the difference

## I found out something intresting, when I tried to use double-1 (len(numbers)-1) the thread (max_worker) to that of input, the time it takes to
## execute the program reaches to fastest. You can experiment here.

## Also noticed something intersting, If we use sleep and assign the double-1 (len(numbers)-1) thread, the execution takes 
## 2 time that of when we assign that to take same number of thread to that of input.

