import pandas as pd
import datetime

yr = 2022
mth = 9
d = 20
hr = 13
min = 30
sec = 18

m_date = datetime.datetime(yr, mth, d)
# print(m_date)
m_date = datetime.datetime(yr, mth, d, hr, min, sec)
# print(m_date)

s = pd.Series(['25 Nov 2021', '10-04-1991', None])
# print(s)
s_date = pd.to_datetime(s)
print()
# print(s_date)
# print(s_date[0].month)

euro_date = '11-9-2022'
# print(pd.to_datetime(euro_date))
# print(pd.to_datetime(euro_date, dayfirst=True))

df = pd.read_csv('notebooks/Datasets/RetailSales_BeerWineLiquor.csv')
# print(df['DATE'].dtype)
df['DATE'] = pd.to_datetime(df['DATE'])
# print(df.head())
df.set_index('DATE', inplace=True)
df_q = df.resample(rule='BQ').mean()
print(df_q)
