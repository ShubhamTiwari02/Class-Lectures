#Bitwise operators - &, |, ^, ~, <<, >> 
#It works on bits and performs bit by bit operation. These are used to compare (binary) numbers.
a = 20
b = 10
print("a =",a, ":", bin(a), ", b =", b, ":", bin(b))
c = a & b #AND - sets each bit to 1 if both bits are 1 
print("a & b =", c, ":", bin(c)) #0000
c = a | b #OR - sets each bit to 1 if one of the bits is 1
print("a | b =", c, ":", bin(c))
c = a ^ b #XOR - sets each bit to 1 if only one of the bits is 1
print("a ^ b =", c, ":", bin(c))
c = ~a #NOT - inverts all the bits 
print("~a =", c, ":", bin(c))
c = a << 2 #Left Shift - shifts the bits of a to the left by 2 positions
print("a << 2 =", c, ":", bin(c))
c = a >> 2 #Right Shift - shifts the bits of a to the right by 2 positions
print("a >> 2 =", c, ":", bin(c))

#Assignment operators - =, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<= (assigns values to variables)
a = 10
b = 5
c = a + b
print("a:", a, "b:", b, "c:", c) #c = 15
c += 2 #c = c + 2
print("c += 2:", c) #c = 17
c -= 4 #c = c - 4
print("c -= 4:", c) #c = 13
c *= 2 #c = c * 2
print("c *= 2:", c, type(c)) #c = 26
c /= 2 #c = c / 2
print("c /= 2:", c, type(c)) #c = 13.0
c = int(c) #explicit conversion
print(c)
d = 15
d %= 2 #d = d % 2
print("d %= 2:", d) #d = 1
d = 15
d //= 2 #d = d // 2
print("d //= 2:", d) #d = 0
d = 13
d **= 3 #d = d ** 3
print("d **= 3:", d)

#Binary numbers system - 0 and 1
#Decimal numbers system - 0 to 9
#Octal numbers system - 0 to 7
#Hexadecimal numbers system - 0 to 9 and A to F
#Number systems conversion
a = 10 #decimal
b = bin(a) #binary
c = oct(a) #octal
d = hex(a) #hexadecimal
print("Decimal:", a)
print("Binary:", b)
print("Octal:", c)
print("Hexadecimal:", d)