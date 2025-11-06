#Array
import array as ModArr 

arr = ModArr.array('i', [10, 20, 30, 40, 50, 60, 70, 80, 90, 100])  # array of integers
#print(arr, type(arr))

arr1 = ModArr.array('f', [1.5, 2.5, 3.5, 4.5, 7, 4])
#print(arr1, type(arr1))

arr2 = ModArr.array('w', ['a', 'b', 'c', 'd']) # array of unicode characters
#print(arr2, type(arr2))

#------------------------------ Accessing array elements ------------------------------
#print(arr[5])  # First element
#print(arr1[2])  # Third element
#print(arr2[2])  # Last element
#print(arr[100])  # Out of range index array

#for i in arr:
#    print(i)

#for i in range(len(arr)):
#    print(i, "-->",arr[i])

#for loc, val in enumerate(arr2):
#    print(f"{loc}, value:- {val}")

#print(arr[2:7])  # Slicing array from index 2 to 6
#print(arr[2:])  # Slicing array from start to index 3
#x = arr[:5]  # Slicing array from start to index 4
#print(x)
#print(arr[:])  # Slicing the entire array

#------------------------------ Modifying array elements ------------------------------
#1. Adding elements
#arr.append(110)  # Appending element at the end
#arr.extend([120, 130, 140])  # Extending array with multiple elements
#arr.insert(2, 25)  # Inserting element at index 2
#print(arr)

#2. Replacing elements
#arr[3] = 35  # Replacing element at index 3
#print(arr)

#3. Removing elements
#arr.remove(50)  # Removing first occurrence of element with value 50
#print(arr)
#arr.pop(4)  # Removing element at index 4
#print(arr)
#arr.pop()  # Removing last element
#print(arr)
#del arr[2]  # Deleting element at index 2
#print(arr)
#del arr  # Deleting the entire array
#print(arr)  # This will raise a NameError since arr is deleted

#i = 0
#while loop
#while i < len(arr):
#    print(arr[i])
#    i = i + 1

import array as ModArr 
import copy as cp
arr = ModArr.array('i', [140, 23, 42, 12, 5, 16, 71, 66, 53, 78])  # array of integers
#ac = arr
#print("Original array:", arr)
#print("Copied array:", ac)
#print(id(arr), id(ac))  # Both will have the same id, indicating they reference the same object
#ac[5] = 999
#print(arr, ac)

#ac = cp.deepcopy(arr)
#print("Original array:", arr)
#print("Copied array:", ac)
#print(id(arr), id(ac))  # Different ids, indicating they are different objects
#arr[1] = 999
#print("After modification:")
#print("Original array:", arr)
#print("Copied array:", ac)

#ArrList = arr.tolist()
#ArrList.sort()
#s_arr = ModArr.array('i', ArrList)
#sorted_list = sorted(arr)
#print("Original array:", arr, type(arr))
#print("Sorted array:", sorted_list, type(sorted_list))

#a = cp.copy(arr)
#a[0] = 200
#a.sort()
#print(id(a), id(arr))

#------------------------------ Reversing array ------------------------------
#1. Slicing
#rev_arr = arr[::-1]
#print("Reversed array using slicing:", rev_arr)
#print("Original array remains unchanged:", arr)

#2. Using reverse() method
#arr_list = arr.tolist()
#arr_list.reverse()
#ra = list(reversed(arr))
#ra = ModArr.array('i', ra)
#print("Reversed array using reverse() method:", ra)
#print("Original array after reverse() method:", arr)

#3. Using a loop
'''rev_arr = ModArr.array('i', [])
for i in range(len(arr)-1, -1, -1):
    rev_arr.append(arr[i])
    print("Appending:", arr[i])

#print("Reversed array using loop:", rev_arr)
print("Original array after loop reversal:", arr)'''

#-------------------------------- Joining arrays ------------------------------
#1. Using + operator
arr3 = ModArr.array('i', [200, 300, 400, 500, 600])
arr4 = arr + arr3
print("Joined array using + operator:", arr4)

#2. Using append() in a loop
for i in arr3:
    arr.append(i)

print("Joined array using append() in a loop:", arr)

#3. Using extend() method
arr.extend(arr3)
print("Joined array using extend() method:", arr)
