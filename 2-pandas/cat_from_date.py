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
# print(df['doa'].dt.day_of_week.head(10))

days_lst = ['MONDAY', 'TUESDAY', 'WENSDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
id2day = {id:day for id, day in enumerate(days_lst)}
day2id = {day:id for id, day in enumerate(days_lst)}
cat_weeks = ['begweek', 'midweek', 'weekend']
df['week_period'] = (
    pd.cut(
        df.doa.dt.day_of_week,
        bins=[day2id['MONDAY']-1, day2id['WENSDAY'], day2id['SATURDAY'], day2id['SUNDAY']+1],
        labels=[cat for cat in cat_weeks]
    )
)

print(df.sample(15))
