import pandas as pd
import datetime

yr = 2022
mth = 9
d = 20
hr = 13
min = 30
sec = 18

m_date = datetime.datetime(yr, mth, d)
print(m_date)
m_date = datetime.datetime(yr, mth, d, hr, min, sec)
print(m_date)