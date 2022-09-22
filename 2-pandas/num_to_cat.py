import pandas as pd

fp = 'bit.ly/felonies-dataset'
df = pd.DataFrame(fp)
print(df.head())
print()
print(df.tail())
print()
print(df.info())