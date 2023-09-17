import numpy as np

arr = np.array([1,2,3,4,5,9])

np.save('data.npy', arr)

arr2 = np.load('data.npy')
print(arr2)

arr3 = np.arange(100).reshape(4,25)
np.savetxt('data_txt.txt', arr3)
print(np.genfromtxt('data_txt.txt'))