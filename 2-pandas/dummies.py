import pandas as pd

fp = 'https://bit.ly/dummy-variables'

df = pd.read_csv(fp)
c = df.color.value_counts(dropna=False)
prem = df.premium.value_counts(dropna=False)
# print(c.head())
# print()
# print(prem.head())
df = pd.get_dummies(df)
df.premium = (df.premium == 1).astype(int)
print(df.head())