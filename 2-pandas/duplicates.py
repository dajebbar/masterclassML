import pandas as pd

fp = 'https://bit.ly/tx-data'
df = pd.read_csv(fp)
# print(df.head())
# print()
# print()
# print(df.tail())

df.amount = df.amount.apply(lambda x: float(x.replace('$', '')))

# print(df.amount.head())

print(df[df.duplicated()].shape[0])
print(df[df.duplicated(subset=['transaction_id'])].shape[0])

df.drop_duplicates(inplace=True)
