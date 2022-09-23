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

# cut dates on categories
# 1975 - 1998 - 2010

df['year_cat'] = (
    pd.cut(df.doa,
            bins=[year(1968),
                    year(1975), 
                    year(1998), 
                    year(2010),
                    year(2021)], 
            labels=[f'law_{i+1}' for i in range(4)]
        )
            

)


# print(df.doa.max().day)
# print(print_date(df.doa.min()))
# print(print_date(df.doa.max()))
# print(df['doa'].dt.year.unique())
# print(df['doa'].dt.year.unique().size)
# print(df['doa'].dt.year.sample(10))
# print(df.info())

# Date Cycling
# print(df['doa'].dt.dayofweek.head(10))

days_lst = ['MONDAY', 'TUESDAY', 'WENSDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
id2day = {id:day for id, day in enumerate(days_lst)}
day2id = {day:id for id, day in enumerate(days_lst)}
cat_weeks = ['begweek', 'midweek', 'weekend']
df['week_period'] = (
    pd.cut(
        df.doa.dt.dayofweek,
        bins=[day2id['MONDAY']-1, day2id['TUESDAY'], day2id['FRIDAY'], day2id['SUNDAY']],
        labels=[cat for cat in cat_weeks]
    )
)

df.insert(loc=4, column='day_of_week', value=df.doa.dt.dayofweek.map(id2day))

month_lst = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
id2mth = {id:mth for id, mth in enumerate(month_lst)}
mth2id = {mth:id for id, mth in enumerate(month_lst)}
df['months'] = df.doa.dt.month.map(id2mth)
df['month_period'] = (
    pd.cut(
        df.doa.dt.month,
        bins = [mth2id['JAN']-1, mth2id['JUN'], mth2id['SEP'], mth2id['DEC']+1],
        labels=['semester2', 'holiday', 'semester1']
    )
)
print(df.sample(15))

