from calendar import month
import pandas as pd
import datetime


fp = 'https://bit.ly/felonies-dataset'
df = pd.read_csv(fp)

# df.columns = df.columns.str.replace(' ', '_').str.lower()
# df.rename(columns={'date_of_arrest':'dof'}, inplace=True)


df.columns = (
    df.columns.str.replace(' ', '_')
    .str.lower() 
)

(
    df.rename(columns={
        'date_of_arrest': 'doa',
    }, inplace=True)
)

df['doa'] = pd.to_datetime(df['doa'])
year = lambda yr : datetime.datetime(yr, month=1, day=1)
print_date = lambda dt: dt.strftime('%d, %b %Y')

print(print_date(year(1852)))
# print(df['doa'].dt.year.unique())
# print(df['doa'].dt.year.unique().size)
# print(df['doa'].dt.year.sample(10))
# print(df.info())
# print(df.head())
