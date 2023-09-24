import pandas as pd

happiness_data = pd.read_csv('happiness.csv')

print(happiness_data.Countries) #if there is spaces in columm name use ['column name']

print(happiness_data['Countries'].max()) # min()

# happiness_data['new_column'] = happiness_data['col1'] + happiness_data[col2]

happiness_data.drop('Available data', axis = 1, inplace=True) #to delete the column

happiness_data.drop(4, inplace = True) #to drop 4th row

#important functions

print(happiness_data['Countries'].unique()) # all the unique values
print(happiness_data['Countries'].nunique()) # no.of unique values
print(happiness_data['Countries'].count()) 
print(happiness_data['Countries'].value_counts())


#filtering

print( happiness_data[happiness_data['Countries'] == 'Finland'] )

#mult condtions
# (happiness_data['Countries'] == 'Finland')&(happiness_data['index'] == 0)

some_data = [1,2,4,5,6,7]

# happiness_data[happiness_data['Column'].isin(some_data)]