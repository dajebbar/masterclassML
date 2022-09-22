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
dc = ['ten', 'twen', 'thirt', 'forth', 'five', 'six', 'seven', 'eigh', 'nine']
df['decade'] = pd.cut(df['Age'], bins=[i for i in range(9, 100, 10)], labels=[i+'ties' for i in dc])
print(df.sample(10))

