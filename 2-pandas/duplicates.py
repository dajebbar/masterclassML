import pandas as pd

fp = 'https://bit.ly/tx-data'
df = pd.read_csv(fp)
# print(df.head())
# print()
# print()
# print(df.tail())

df.amount = df.amount.apply(lambda x: float(x.replace('$', '')))

# print(df.amount.head())

print(df[df.duplicated()])