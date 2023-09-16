import numpy as np


#2d arrays

arr1 = np.array([[1, 2, 3], [2, 3, 4]]) #must be of equal lengths
print(arr1)

#reshpae
arr = np.arange(10).reshape(2,5) #converts the 10 element to 2x5 array
print(arr)
#length must be compatible with shape

print(arr.shape)

#arithems
print(arr.min(),
arr.max(),
arr.mean(),
arr.sum())

#other
print(np.zeros((2,5))) #must be in ()
print(np.ones((5,5)))


#3d arrays
#3d arrays has 3 [ at the start

arr2 = np.array([[[1, 1, 1], [0, 0, 0]],[[1, 2, 3], [4, 5, 6]],[[1, 3, 5], [7, 8, 6]]])
print(arr2)
print(arr2.shape) #(3, 2, 3) i.e, 3 2x3 arrays
print(arr2.size)
print(arr2.reshape(3,3,2)) #3*3*2 = 18

#4d array

arr3 = np.arange(72)
print(arr3.size)

print(arr3.reshape(4,3,2,3))
