import threading
import time

def process(num):
    
    for i in range(num):
        print(i)
   
n1 = threading.Thread(target=process, args=[10000]) 
n2 = threading.Thread(target=process, args=[20000]) 
n3 = threading.Thread(target=process, args=[10000]) 

start = time.perf_counter()

process(10000)
process(20000)
process(10000)

# n1.start()
# n2.start()
# n3.start()

# n1.join()
# n2.join()
# n3.join()

end = time.perf_counter()
print(f'Time count: {end-start}')

# without thread, output = 5.3 sec
# with thread, output = 5.7 sec

""" thread is usefull for optimization when there is sleep()/IO/API """

""" This is where Multiprocess comes in"""