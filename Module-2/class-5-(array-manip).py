import numpy as np

arr = np.linspace(1,10,9)
# print(arr)
arr = arr.reshape(3,3)
# print(arr)

arr2 = np.linspace(1,5,9)
arr2 = arr2.reshape(3, 3)

arr_concat = np.concatenate([arr, arr2]) #must matching dimensions for array
print(arr_concat) #axis = 0

arr_concat = np.concatenate([arr, arr2], axis = 1) # cocnatenttion will now be performed coloumn wise 
print(arr_concat) 


#stacking

data1 = np.arange(1,10)
data2 = np.arange(13,22)

print(np.stack((data1, data2)))  #it increases the dimension to 2d
print(np.column_stack((data1, data2)))  #it increases the dimension to 2d
#hstack, vstack


arr_split = np.split(arr, 3)
print(arr_split)

stacked = np.arange(16).reshape(4,4)
print(np.hsplit(stacked, 4))
print(np.vsplit(stacked, 4))