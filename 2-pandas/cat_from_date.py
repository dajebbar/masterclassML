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

print(df.info())
# print(df.head())
