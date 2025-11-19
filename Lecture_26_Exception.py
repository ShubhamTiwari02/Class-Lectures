# '''try:
#     print("Akash is a good boy.")
# except NameError:
#     print("A NameError exception occurred.")
# except ZeroDivisionError:
#     print("A ZeroDivisionError exception occurred.")
# except:
#     print("An unexpected error occurred.")
# else:
#     print("No error occurred.")

# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
#     print(f"Result is {result}")
# #except ValueError:
# #    print("Invalid input! Please enter a valid integer.")
# #except ZeroDivisionError:
# #    print("Error! Division by zero is not allowed.")
# except:
#     print("An unexpected error occurred.")
# else:
#     for i in range(10):
#         print(f"{result} x {i+1} = {result * (i+1)}")
#     #print("No error occurred.")'''

# # try:
# #     num = int(input("Enter a number: "))
# #     result = 10 / num
# #     print(f"Result is {result}")
# # except ValueError:
# #     print("Invalid input! Please enter a valid integer.")
# # except ZeroDivisionError:
# #     print("Error! Division by zero is not allowed.")
# # except:
# #     print("An unexpected error occurred.")
# # else:
# #     for i in range(10):
# #         print(f"{result} x {i+1} = {result * (i+1)}")
# #     #print("No error occurred.")
# # finally:
# #     print("Execution completed.")

# # #raise Exception("This is a custom exception")
# # def divide(a, b):
# #     if b == 0:
# #         raise Exception("Raghav Defined Error: Division by zero is not allowed.")
# #     return a / b

# # try:
# #     result = divide(10, 0)
# #     print("Result:", result)
# # except Exception as e:
# #     print(e)

# class KunalException(Exception):
#     pass
# def risky_function():
#     raise KunalException("Something went wrong in risky_function")
#     print("risky_function executed successfully.")

# try:
#     risky_function()
# except KunalException as e:
#     print(f"Caught a Custom Exception: {e}")

# # # #Exception chaining
# # # try:
# # #     open("non_existent_file.txt", "r")
# # # except OSError:
# # #     raise RuntimeError("A runtime error occurred due to an OS error.")
# # #     #print("FileNotFoundError exception occurred.")

# # try:
# #     open("non_existent_file.txt", "r")
# # except OSError:
# #     raise RuntimeError from OSError
# #     #print("FileNotFoundError exception occurred.")

# import logging
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# def total_sum(a,b):
#     logging.debug(f"Calculating the sum of {a} and {b}")
#     result = a + b
#     logging.debug(f"Result of sum: {result}")
#     return result

# if __name__ == "__main__":
#     x = 5
#     y = 10
#     logging.info(f"Starting sum calculation for {x} and {y}")
#     sum_result = total_sum(x, y)
#     logging.info(f"The total sum is: {sum_result}")

import logging
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")
logger.debug("Akash is dangerous")
logger.info("Akash is very dangerous")
logger.warning("Akash is extremely dangerous")
logger.error("Akash is super dangerous")
logger.critical("Akash is ultra dangerous")
logger.debug("Akash is mega dangerous")
logger.info("Akash is giga dangerous")
logger.warning("Akash is tera dangerous")
logger.error("Akash is peta dangerous")
logger.critical("Akash is exa dangerous")
logger.debug("Akash is zetta dangerous")
logger.info("Akash is yotta dangerous")
logger.warning("Akash is bronto dangerous")
logger.error("Akash is geo dangerous")
logger.critical("Akash is hell dangerous")
logger.debug("Akash is infinite dangerous")
logger.info("Akash is ultimate dangerous")
logger.warning("Akash is supreme dangerous")
logger.error("Akash is omnipotent dangerous")
logger.critical("Akash is godlike dangerous")
logger.debug("Akash is cosmic dangerous")
logger.info("Akash is universal dangerous")
logger.warning("Akash is multiversal dangerous")
logger.error("Akash is omniversal dangerous")
logger.critical("Akash is beyond dangerous")
logger.debug("Akash is transcendent dangerous")
logger.info("Akash is ineffable dangerous")
logger.warning("Akash is indescribable dangerous")
logger.error("Akash is unimaginable dangerous")
logger.critical("Akash is unfathomable dangerous")
logger.debug("Akash is limitless dangerous")
logger.info("Akash is boundless dangerous")
logger.warning("Akash is infinite dangerous")
logger.error("Akash is eternal dangerous")
logger.critical("Akash is everlasting dangerous")
logger.debug("Akash is immortal dangerous")
logger.info("Akash is invincible dangerous")
logger.warning("Akash is unstoppable dangerous")
logger.error("Akash is unbeatable dangerous")
logger.critical("Akash is undefeatable dangerous")