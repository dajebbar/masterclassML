import pandas as pd
import numpy as np

np.random.seed(101)
pd.set_option('display.max_columns', 0)


def main():
    arr = np.random.randint(0, 101, size=(4, 3))
    # print(arr)
    df_idx = ['CA', 'NY', 'AZ', 'TX']
    df_cols = ['Jan', 'Feb', 'Mar']
    # df = pd.DataFrame(data=arr)
    # print(df)
    
    # df = pd.DataFrame(data=arr, index=df_idx)
    # print(df)
    
    df = pd.DataFrame(data=arr, index=df_idx, columns=df_cols)
    # print(df)
    # print()
    # df.info()
    
    tips = pd.read_csv('notebooks/Datasets/tips.csv')
    # print(tips.head())
    
    # print(tips[['tip', 'total_bill']])
    tips['tip_percentage'] = 100. * tips['tip'] / tips['total_bill']
    # print(tips.head())
    tips.drop(columns=['tip_percentage'], inplace=True)
    tips = tips.set_index('Payment ID')
    # print(tips.head())
    # tips = tips.reset_index()
    
    print(tips.loc[:'Sat3880', ['tip', 'time']])
    print(tips.iloc[:10, [3, 4]])

if __name__=='__main__':
    main()