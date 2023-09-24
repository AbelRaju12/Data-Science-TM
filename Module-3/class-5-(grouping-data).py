import pandas as pd

#groupby

df = pd.read_csv('Happiness.csv')

print(df.head())

df = df.groupby('Happiness index, 2022')
print(df.groups)

##aggregation
df.groupby('Director')['Stars'].mean()

df.groupby(['Director','Season'])['Stars'].mean()