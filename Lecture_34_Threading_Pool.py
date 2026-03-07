#Thread pools - Its a mechanism to execute multiple threads concurrently. It is a way to manage a pool of worker threads that can be used to execute tasks in parallel. The main advantage of using a thread pool is that it can improve the performance of a program by reducing the overhead of creating and destroying threads.
#Multiproccessing.dummy and concurrent.futures.ThreadPoolExecutor are two different ways to create a thread pool in Python. The main difference between the two is that multiprocessing.dummy is a wrapper around the threading module, while concurrent.futures.ThreadPoolExecutor is a higher-level interface for managing threads.
#The multiprocessing.dummy module provides a simple way to create a thread pool using the threading module. It allows you to create a pool of worker threads and submit tasks to be executed by those threads

# from multiprocessing.dummy import Pool 
# import time

# def square(x):
#     sqr =  x * x
#     time.sleep(1)
#     print(f"The square of {x} is {sqr}")

# def cube(x):
#     cube = x * x * x
#     time.sleep(10)
#     print(f"The cube of {x} is {cube}")

# numbers = [1, 2, 3, 4, 5]
# pool = Pool(5)
# pool.map(square, numbers)
# pool.map(cube, numbers)
# pool.close()
# pool.join()

# from concurrent.futures import ThreadPoolExecutor
# from time import sleep
# def square(numbers):
#    for val in numbers:
#       ret = val*val
#       sleep(1)
#       print(f"The square of {val} is {ret}")
      
# def cube(numbers):
#    for val in numbers:
#       ret = val*val*val
#       sleep(1)
#       print(f"The cube of {val} is {ret}")
      
# if __name__ == '__main__':
#    numbers = [1,2,3,4,5]
#    executor = ThreadPoolExecutor(4)
#    thread1 = executor.submit(square, (numbers))
#    thread2 = executor.submit(cube, (numbers))
#    print("Thread 1 executed? --> ",thread1.done())
#    print("Thread 2 executed? --> ",thread2.done())
#    sleep(10)
#    print("Thread 1 executed? -> ",thread1.done())
#    print("Thread 2 executed? -> ",thread2.done())

#Main thread - The main thread is the initial thread of execution in a Python program. It is responsible for starting the program and managing the execution of other threads. The main thread can create and manage other threads, and it can also perform tasks such as handling user input, managing resources, and coordinating the execution of other threads. The main thread is typically the first thread to be created when a Python program starts, and it continues to run until the program terminates.
# import threading
# name = "Akash"
# print(f"Hello, {name} from the main thread!")
# print(threading.current_thread)

# import threading
# import time

# def myfuction_1():
#     print("Function 1 is starting")
#     time.sleep(2)
#     print("Function 1 is done")

# def myfuction_2(main_thread):
#     print("Function 2 is waiting for function 1 to complete")
#     main_thread.join()
#     print("Function 2 is starting")
#     time.sleep(2)
#     print("Function 2 is done")

# worker1 = threading.Thread(target=myfuction_1)
# worker2 = threading.Thread(target=myfuction_2, args=(worker1,))

# worker1.start()
# worker2.start()
# for i in range(6):
#     print("Main thread is doing some work...")
#     time.sleep(1)

# worker1.join()
# print("Main thread is done")

#Thread synchronization - Thread synchronization is the process of coordinating the execution of multiple threads to ensure that they do not interfere with each other and that they access shared resources in a controlled manner. This is important because multiple threads can access the same resources, such as memory or files, and if they do so without proper synchronization, it can lead to race conditions, where the outcome of the program depends on the timing of the threads' execution. To prevent this, thread synchronization techniques such as locks, semaphores, and condition variables can be used to control access to shared resources and ensure that only one thread can access a resource at a time. This helps to ensure that the program runs correctly and produces consistent results.
# import threading
# counter = 10

# def increment(theLock, num):
#     global counter
#     for i in range(num):
#         theLock.acquire()
#         counter += 1
#         print("Counter value is: ", counter)
#         theLock.release()

# theLock = threading.Lock()
# thread1 = threading.Thread(target=increment, args=(theLock, 10))
# thread2 = threading.Thread(target=increment, args=(theLock, 20))
# thread3 = threading.Thread(target=increment, args=(theLock, 30))
# thread1.start()
# thread2.start()
# thread3.start()

# for i in (thread1, thread2, thread3):
#     i.join()

# print("Counter value is: ", counter)
# print("All threads are done")
# print("The final value of counter is: ", counter)

# import threading
# import time

# class MyThread(threading.Thread):
#     def __init__(self, thread_id, name, counter):
#         threading.Thread.__init__(self)
#         self.name = name
#         self.thread_id = thread_id
#         self.counter = counter

#     def run(self):
#         print(f"{self.name} is starting")
#         time.sleep(2)
#         print_time(self.name, self.counter, 3)

# def print_time(thread_name, delay, counter):
#     while counter:
#         time.sleep(delay)
#         print("%s : %s" % (thread_name, time.ctime(time.time())))
#         counter -= 1

# threads = []
# thread1 = MyThread(1, "Thread-1", 5)
# thread2 = MyThread(2, "Thread-2", 10)
# thread3 = MyThread(3, "Thread-3", 15)

# thread1.start()
# thread2.start()
# thread3.start()

# thread1.join()
# thread2.join()
# thread3.join()

# print("Exiting the program")

# import threading
# import time
# def run():
#     thread = threading.current_thread()
#     print(f"{thread.name} is starting")
#     print(f"Daemon thread: {thread.daemon}")

# thread1 = threading.Thread(target=run, name="Thread-1", daemon=True)
# thread2 = threading.Thread(target=run, name="Thread-2", daemon=True)
# thread1.start()
# thread2.start()

# print("Is main thread is daemon thread? ", threading.current_thread().daemon)
# time.sleep(1)


