import numpy as np

#slicing

arr = np.arange(25,40)
print(arr[-1])
print(arr[5])

arr[5] = 19
print(arr[5]) #arrays are mutable

print(arr[5::2])
print(arr[:8:3])


#2d slicing
arr = arr.reshape(3,5) # 3 row 5 coloumn
print(arr)

print(arr[0][2])
print(arr[0, 2])

print(arr[-1]) #gives the third or last row

print(arr[-3, -5]) #to access first element

print(arr[:, :3]) # all rows and upto third (0-2) coloumn coloumn
print()
print(arr[-1:, 2:])
print()

print(arr[-1:-3:-1,::])
print(arr[::-1,::])
