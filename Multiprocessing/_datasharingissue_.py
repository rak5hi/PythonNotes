from multiprocessing import Process


numbers: list[int] = [0]


def func():
    global numbers
    
    numbers.extend([1, 2, 3])
    print(f'Process data: {numbers}')
    
    
def main():
    process = Process(target=func)
    process.start()
    process.join()
    
    print('Main data:', numbers)
    
    
if __name__ == '__main__':
    main()
    
#OUTPUT:
"""
Process data: [0, 1, 2, 3]
Main data: [0]
"""

""" Global variable is not updated even after calling the function.
Bcz in Multiprocessing, each worker has its own memory,

so processes do not share memory.
Each process just has its own space of memory.

so as soon as process started and referred to global numbers,
its created its own space of memory."""