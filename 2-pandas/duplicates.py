import pandas as pd

fp = 'https://bit.ly/tx-data'
df = pd.read_csv(fp)
# print(df.head())
# print()
# print()
# print(df.tail())

df.amount = df.amount.str.replace('$', '').astype(float)
print(df.head())