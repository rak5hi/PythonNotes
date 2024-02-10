from multiprocessing import Process, Queue



def insert_val(queue: Queue, i: int):
    print(f'{i} was put in the queue...')
    queue.put(i)
    
def main():
    queue: Queue = Queue()
    
    processes = [Process(target=insert_val, args=(queue, i)) for i in range(5)]
    
    for process in processes:
        process.start()
        
    for process in processes:
        process.join()
        
    results = [queue.get() for _ in processes]
    print(results)
    
    
if __name__ == '__main__':
    main()