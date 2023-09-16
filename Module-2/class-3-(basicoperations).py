import numpy as np

arr1 = np.arange(9).reshape(3, 3)
arr2 = np.arange(36, 45).reshape(3, 3)
# print(arr1, arr2)

print(arr1 + arr2) # - * / // %

print(arr1**3)

#functions
print(np.multiply(arr1, arr2)) #add subtract mod divide power... 

#matrix multiplication
print(np.dot(arr1, arr2)) #shapes should adhere to mat mult constraint

arr3 = np.dot(arr1, arr2)
print(arr3.std()) #SD
print(arr3.ptp()) # = arr3.max()-arr3.min()
