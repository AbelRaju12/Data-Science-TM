#DS to store data
import pandas as pd
import numpy as np


#Series

fruits = ['mango', 'apple', 'cherry', 'orange', 'banana']
print(pd.Series(fruits))

pdFruits = pd.Series(fruits, index =['a', 'b', 'c', 'd','e'])
print(pdFruits)

data = pd.Series(np.arange(5), index = [11, 22, 33, 44, 55])
print(data)

pdFruits['c'] = 'pineapple'
print(pdFruits) # => series are mutable

dict1 = {1: 'red', 2: 'blue', 3: 'grey', 4: 'white'}
dict1 = pd.Series(dict1)
print(dict1)

print(pdFruits.shape)
print(pdFruits.index)
print(pdFruits.size)

#Dataframes

fruits = ['mango', 'apple', 'cherry', 'orange', 'banana']

dfFruits = pd.DataFrame(fruits)
print(dfFruits)

arr = np.arange(16).reshape(4,4)
arr = pd.DataFrame(arr, columns = ['a', 'b', 'c', 'd'], index = ['A', 'B', 'C', 'D'])
print(arr)