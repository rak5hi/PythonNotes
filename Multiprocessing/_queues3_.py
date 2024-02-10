from multiprocessing import Process, Queue
import time


"""Getting result from Multiprocessesing in order."""

def square_num(identifier: int, num: int, queue: Queue):
    time.sleep(2)
    queue.put((identifier, num**2))
    
def main():
    queue: Queue = Queue()
    data: list[int] = list(range(1, 9))
    
    processes = [Process(target=square_num, args=(identifier, num, queue)) for identifier,num in enumerate(data)]
    
    for process in processes:
        process.start()
        
    for process in processes:
        process.join()
        
        
    unsorted = [queue.get() for _ in processes]
    print(unsorted)
    
if __name__ == '__main__':
    main()