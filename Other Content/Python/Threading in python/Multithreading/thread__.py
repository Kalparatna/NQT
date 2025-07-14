import threading
import time



# sleep function used to pause the process for time givesn
# indicate some task being done

'''
Normal Code:   Will take 7 seconds total to execute 

def func(seconds):
    print(f'sleeping for {seconds} seconds')
    time.sleep(seconds)

func(4)
# Will excecute after 4 seconds
func(3)
# Will excecute after 3 seconds
func(2)
# Will excecute after 2 seconds
func(1)
'''

#Using Threads    :  Will take 0 to 1 seconds total to execute 

def func(seconds):
    print(f'Sleeping for {seconds} seconds')
    time.sleep(seconds)


# t1 = threading.Thread(target=func, args=[4])
# t2 = threading.Thread(target=func, args=[3])
# t3 = threading.Thread(target=func, args=[2])
# t4 = threading.Thread(target=func, args=[1])

# t1.start()
# t2.start()
# t3.start()
# t4.start()

#print("Process being executed")

# Number of threads
num_threads = 4

# Create and start threads in a loop
threads = []
for i in range(num_threads):
    thread = threading.Thread(target=func, args=[i+1])
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("All threads completed!")


    