#datetime
import datetime
n = datetime.datetime.now()
#print("Current date and time:", n)
#print("Current year:", n.year)
#print("Current month:", n.month)
#print("Current day:", n.day)
#print("Current hour:", n.hour)
#print("Current minute:", n.minute)
#print("Current second:", n.second)
#print(n.strftime("%D"))
#print(n.strftime("%Y-%m-%d %H:%M:%S"))
#print(n.strftime("%W"))
#print(n.strftime("%I:%M %p"))  # 12-hour format with AM/PM
#print(n.strftime("%H:%M %p"))  # 24-hour format with AM/PM
#print(n.strftime("%B %d, %Y"))
#print(n.strftime("%A, %B %d, %Y"))

#x = datetime.datetime(2005, 7, 8)
#print(x.strftime("%A, %B %d, %Y"))

#print(n.strftime("%c"))  # Day of the year
#print(n.strftime("%x"))
#print(n.strftime("%X"))
#print(n.strftime("%V"))  # ISO week number of the year
#print(n.strftime("%C"))  # Century (year divided by 100, truncated to an integer)
#print(n.strftime("%f"))  # Microsecond as a zero-padded decimal number
#print(n.strftime("%Z"))  # Time zone name

#------------------------------ Math module ------------------------------
#inbuilt math module and extensive mathematical functions (math module)
#x = min(5, 10, 25, 2, 15, 0, -5, 3)
#y = max(5, 10, 25, 2, 15, 0, -5, 3)
#print(x)
#print(y)

#a = abs(-100.25) #abs() function returns the absolute (positive) value of the specified number
#print(a)

#b = pow(20, 3) #pow() function returns the value of x to the power of y (xy)
#print(b)

import math as m
#c = m.sqrt(15) #math.sqrt() function returns the square root of a
#print(c)
#d = m.ceil(4.2) #math.ceil() function rounds a number UP to the nearest integer
#print(d)
#e = m.floor(4.7) #math.floor() function rounds a number DOWN to the nearest integer
#print(e)
#r = round(5.1) #round() function rounds a number to the nearest integer
#print(r)
#f = m.factorial(6) #math.factorial() function returns the factorial of a number
#print(f)
#p = m.pi #math.pi function returns the value of pi
#print(p)
#e = m.e #math.e function returns the value of e
#print(e)
#a = m.tau #math.tau function returns the value of tau (2*pi)
#print(a)
#b = m.nan #math.nan function returns a floating-point "Not a Number" (NaN) value
#print(b)
#c = m.inf #math.inf function returns a floating-point positive infinity value
#print(c)
#c = m.comb(8, 3) #math.comb(n, k) function returns the number of ways to choose k items from n items without repetition and without order
#print(c)