import numpy as np
import pandas as pd


def main():
    df = pd.read_csv('nb/Datasets/mpg.csv')
    # print(df.head())
    # print(df.shape)
    # print(df['model_year'].unique())
    
    # print(df.groupby(['model_year']).mean())
    # print(df.groupby(['model_year', 'cylinders']).mean()[['mpg']])
    year_cyl = df.groupby(['model_year', 'cylinders']).mean()
    # print(year_cyl)
    # print(year_cyl.loc[[70, 80]])
    print(year_cyl.loc[(82, 4)])
    

if __name__=='__main__':
    main()