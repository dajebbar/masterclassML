import pandas as pd

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
print(df['doa'].dt.year.sample(10))

# print(df.info())
# print(df.head())
