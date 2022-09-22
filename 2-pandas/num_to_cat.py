import pandas as pd

fp = 'https://bit.ly/felonies-dataset'
df = pd.read_csv(fp)
# print(df.head())
# print()
# print(df.tail())
# print()
# print(df.info())

# print(df.Age.describe())

df['age_bin'] = pd.cut(df['Age'], bins=[9, 13, 20, 65, 100], labels=['child', 'taneeger', 'adult', 'senior'])
# print(df['age_bin'].head())
print(df.sample(10))

