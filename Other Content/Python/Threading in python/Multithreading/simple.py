import threading 
import time

def task1():
    for _ in range(3):
        print("Task 1 is being excecuted !")
        time.sleep(3)

def task2():
    for _ in range(3):
        print("Task 2 is being executed !")
        time.sleep(3)

thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)

#Thread Start
thread1.start()
thread2.start()

#Wait for both threads to finish
thread1.join()
thread2.join()

print("Both threads execution completed")