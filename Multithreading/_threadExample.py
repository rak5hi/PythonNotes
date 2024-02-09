import threading
import time

def sample(seconds):
    print(f'sleeping for {seconds} seconds')
    time.sleep(seconds)
   
t1 = threading.Thread(target=sample, args=(3,)) 
t2 = threading.Thread(target=sample, args=[2]) 
t3 = threading.Thread(target=sample, args=[1]) 
#thread2 = threading.Thread(target=process_data, args=('Thread-2', 5))
    
start = time.perf_counter()

# sample(3)
# sample(2)
# sample(1)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

end = time.perf_counter()
print(f'Time count: {end-start}')

# without thread, output = 6 sec
# with thread, output = 3 sec

