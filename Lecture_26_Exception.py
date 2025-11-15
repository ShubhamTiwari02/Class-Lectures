'''try:
    print("Akash is a good boy.")
except NameError:
    print("A NameError exception occurred.")
except ZeroDivisionError:
    print("A ZeroDivisionError exception occurred.")
except:
    print("An unexpected error occurred.")
else:
    print("No error occurred.")

try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(f"Result is {result}")
#except ValueError:
#    print("Invalid input! Please enter a valid integer.")
#except ZeroDivisionError:
#    print("Error! Division by zero is not allowed.")
except:
    print("An unexpected error occurred.")
else:
    for i in range(10):
        print(f"{result} x {i+1} = {result * (i+1)}")
    #print("No error occurred.")'''

# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
#     print(f"Result is {result}")
# except ValueError:
#     print("Invalid input! Please enter a valid integer.")
# except ZeroDivisionError:
#     print("Error! Division by zero is not allowed.")
# except:
#     print("An unexpected error occurred.")
# else:
#     for i in range(10):
#         print(f"{result} x {i+1} = {result * (i+1)}")
#     #print("No error occurred.")
# finally:
#     print("Execution completed.")

# #raise Exception("This is a custom exception")
# def divide(a, b):
#     if b == 0:
#         raise Exception("Raghav Defined Error: Division by zero is not allowed.")
#     return a / b

# try:
#     result = divide(10, 0)
#     print("Result:", result)
# except Exception as e:
#     print(e)

class KunalException(Exception):
    pass
def risky_function():
    raise KunalException("Something went wrong in risky_function")
    print("risky_function executed successfully.")

try:
    risky_function()
except KunalException as e:
    print(f"Caught a Custom Exception: {e}")