# csv files. ',' seperated data.
# pd.read_csv

import pandas as pd

happiness_data = pd.read_csv('happiness.csv')
print(happiness_data.head()) #top 5 #can specify values like head(10)
print(happiness_data.tail()) #last 5 #can sepcify values like tail(15)


print(happiness_data.info()) #shows the number of non-null values along with thier datatype

print(happiness_data.describe()) #statiscal information. average. min. percentile values.

print(happiness_data['Countries'])

print(happiness_data.loc[4])
print(happiness_data.iloc[4])

happiness_data_2 = pd.read_csv('happiness.csv', index_col= 'Countries')

print(happiness_data_2)

print(happiness_data_2.loc['Netherlands']) #iloc is for integer locations/index only

happiness_data_2 = happiness_data_2.reset_index() #to reset index to numbers

#slicing

print(happiness_data_2[34:45:2])
