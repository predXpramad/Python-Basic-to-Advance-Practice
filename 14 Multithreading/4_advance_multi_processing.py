###  Multiprocessing with ProcessPoolExecutor

from concurrent.futures import ProcessPoolExecutor
import time

def square_number(number):
    time.sleep(10)
    return f"Square: {number * number}"

numbers=[1,2,3,4,5,6,7,8,9,10,11]

if __name__ == "__main__":
    t1 = time.time()
    with ProcessPoolExecutor(max_workers=4) as executor:
        results = executor.map(
            square_number,
            numbers
        )
    t2 = time.time() -t1

    for result in results:
        print(result)

print(t2)