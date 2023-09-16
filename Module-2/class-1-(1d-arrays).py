import numpy as np

#1d array
arr = np.array([1, 2, 3, 4, 5])
print(type(arr))

arr = np.array((1, 2, 3, 4, 5))
print(type(arr))

arr = np.array({1, 2, 3, 4, 5})
print(type(arr))

#it only accept similar kind of elements. if you mix numbers and strings, it will type cast int to string
arr = np.array([1, 5, 6, "abel"])
print(arr)

arr = np.arange(3,20,3)
print(arr)
arr = np.arange(20)
print(arr)

#linspace-> equally spaced array elements b/w a range with specific size if you want
print(np.linspace(1,3,6))

print(np.full(13, 40)) # fill 13 places with 40

print(arr.shape)
print(arr.size) #total number of elements. size and shape same in case of 1d array
print(arr.ndim) #dimensions
print(arr.itemsize) #space for each element
print(arr.dtype)