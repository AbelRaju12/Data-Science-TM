import pandas as pd

happiness_data = pd.read_csv('happiness.csv')

print(happiness_data.head())

print(happiness_data.isnull()) # null values
print(happiness_data.isnull().any()) #if there are any null values in the row
print(happiness_data.isnull().sum()) #to see the exact no. of null rows

happiness_data = happiness_data.dropna() #drops null vals

# data = pd.read_csv('Happiness.csv')

# #if there are null values in a coloumn we can fill it
# data = data['Countries'].fillna(data['Countries'])

# print(data.duplicated()) #.sum()

# # print(data.duplicated('Countries'))

# # data.drop_duplicates('Countries', inplace = True)


import numpy as np
arr=np.arange(16).reshape(4,4)
df1=pd.DataFrame(arr,columns=['A','B','E','C'])
print(df1)

arr2=np.arange(16).reshape(4,4)
df2=pd.DataFrame(arr,columns=['A','F','E','C'])
print(df2)

#join
df3=pd.concat([df1,df2])
print(df3)

#fills the null values with
df3.fillna(method='ffill',inplace=True)#forward filling
df3 = df3.fillna(method='bfill') #backward filling

print(df3)
