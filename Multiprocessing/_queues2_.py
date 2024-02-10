from multiprocessing import Queue, Process, current_process

def func(queue: Queue):
    name: str = current_process().name
    
    try:
        print(f'{name} received data: {queue.get(timeout=3)}')
        #if queue.get() not get anything in 3 sec, its going to throw an exception
    except Exception as e:
        print('Timeout!', e)
        
    
def main():
    queue: Queue = Queue()
    queue.put(1)
    queue.put(2)
    queue.put(3)
    queue.put(4)
    
    
    processes = [Process(target=func, args=(queue,)) for _ in range(4)]
    
    for process in processes:
        process.start()
        
    for process in processes:
        process.join()
        
    
if __name__ == '__main__':
    main()