# #import threading 
# from threading import Thread
# import time
# # def add_numbers(a, b):
# #     time.sleep(15)
# #     result = a + b
# #     print(f"The sum of {a} and {b} is: {result}")

# # def basic_func():
# #     print("Basic function is running currently...")

# # def subtract_numbers(a, b):
# #     time.sleep(12)
# #     result = a - b
# #     print(f"The difference of {a} and {b} is: {result}")

# # def multiply_numbers(a, b):
# #     time.sleep(8)
# #     result = a * b
# #     print(f"The product of {a} and {b} is: {result}")

# # def cube_numbers(a):
# #     time.sleep(3)
# #     result = a ** 3
# #     print(f"The cube of {a} is: {result}")

# # Thread(target=add_numbers, args=(5, 3)).start()
# # Thread(target=subtract_numbers, args=(5, 3)).start()
# # Thread(target=multiply_numbers, args=(5, 3)).start()
# # Thread(target=cube_numbers, args=(5,)).start()
# # Thread(target=basic_func).start()
# exitflag = 0
# class KunalThread(Thread):
#     def __init__(self, threadID, name, counter):
#         Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter

#     def run(self):
#         print(f"Starting thread: {self.name}")
#         self.print_time(self.counter, 2)
#         print(f"Exiting thread: {self.name}")

#     def print_time(self, counter, delay):
#         while counter:
#             if exitflag:
#                 break
#             time.sleep(delay)
#             print(f"{self.name}: {time.ctime(time.time())}")
#             counter -= 1

# thread1 = KunalThread(1, "Thread-1", 5)
# thread2 = KunalThread(2, "Thread-2", 10)
# thread1.start()
# thread2.start()
# print("Exiting Main Thread")

#Joinning Threads
# import threading
# import time

# def myfuction_1(arg1):
#     for i in range(arg1):
#         print(f"Function 1 is running for :{i}")
#         time.sleep(1)

# def myfuction_2(arg1):
#     for i in range(arg1):
#         print(f"Function 2 is running for :{i}")
#         time.sleep(1)

# thread1 = threading.Thread(target=myfuction_1, args=(10,))
# thread2 = threading.Thread(target=myfuction_2, args=(10,))
# thread1.start()
# thread1.join(timeout=5)  
# thread2.start()
# thread2.join()
# print("Exiting Main Thread")

#Thread naming 
#Example 1 of thread naming in python
# import threading
# import time

# def myfuction_1(arg1):
#     print(f"Thread Name: {threading.current_thread().name}")
#     time.sleep(1)

# thread1 = threading.Thread(target=myfuction_1, args=(10,), name="LoginThread")
# thread2 = threading.Thread(target=myfuction_1, args=(10,), name="SignupThread")
# print("The thread name is: ", threading.current_thread().name)
# thread1.start()
# thread1.join()
# thread2.start()
# thread2.join()
# print("Exiting Main Thread")

#Example 2 of thread naming in python
# import threading
# import time

# def myfuction_1(arg1):
#     #threading.current_thread().name = "ApplicationThread"
#     print(f"Thread Name: {threading.current_thread().name}")
#     time.sleep(1)

# thread1 = threading.Thread(target=myfuction_1, args=(10,), name="LoginThread")
# thread2 = threading.Thread(target=myfuction_1, args=(10,), name="SignupThread")
# thread3 = threading.Thread(target=myfuction_1, args=(10,), name = "ApplicationThread")
# print("The thread name is: ", threading.current_thread().name)
# thread1.start()
# thread1.join()
# thread2.start()
# thread2.join()
# thread3.start()
# thread3.join()
# thread3.name = "KunalThread"
# print("Exiting Main Thread")

#Scheduling Threads
#1 way to schedule threads is by using time.sleep() method. It will pause the thread for a specified amount of time.
# import threading
# import time

# def myfuction_1(name, StartTime):
#     now = time.time()
#     elapsed_time = now - StartTime
#     print(f"Elapsed Time: {elapsed_time} seconds, Name = {name}")
#     time.sleep(1)

# start = time.time()
# print("Start", time.ctime(start))

# thread1 = threading.Timer(2, myfuction_1, args=("Thread-1", start))
# thread2 = threading.Timer(4, myfuction_1, args=("Thread-2", start))
# #thread3 = threading.Thread(target=myfuction_1, args=("Thread-3", start))

# thread1.start()
# thread1.join()
# thread2.start()
# thread2.join()
# end = time.time()
# print("End", time.ctime(end))
# print("Exiting Main Thread")

#2 way to schedule thread is by using the schedule module. It allows you to schedule tasks at specific intervals or times.
# import sched
# import time
# scheduler = sched.scheduler(time.time, time.sleep)

# def myfuction_1(name, StartTime):
#     now = time.time()
#     elapsed_time = now - StartTime
#     print(f"Elapsed Time: {elapsed_time} seconds, Name = {name}")

# start = time.time()
# print("Start", time.ctime(start))
# scheduler.enter(2, 1, myfuction_1, argument=("Thread-1", start))
# scheduler.enter(4, 1, myfuction_1, argument=("Thread-2", start))
# scheduler.run()
# end = time.time()
# print("End", time.ctime(end))
# print("Exiting Main Thread")

#3rd Way
# from datetime import datetime
# import sched
# import time

# def add_numbers(a, b):
#     print("Performing addition...", datetime.now())
#     print("Time:", time.monotonic())
#     print(f"The sum of {a} and {b} is: {a + b}")

# scheduler = sched.scheduler()
# print("Start time:", datetime.now())
# event1 = scheduler.enter(5, 1, add_numbers, argument=(15, 30))
# print("Event created :", event1)
# scheduler.run()
# print("End time:", datetime.now())
