import numpy as np
import pandas as pd


def main():
    df = pd.read_csv('nb/Datasets/mpg.csv')
    print(df.head())
    print(df.shape)
    print(df['model_year'].unique())
    
    # groupby
    print(df.groupby(['model_year']).mean())
    print(df.groupby(['model_year', 'cylinders']).mean()[['mpg']])
    year_cyl = df.groupby(['model_year', 'cylinders']).mean()
    print(year_cyl)
    print(year_cyl.loc[[70, 80]])
    print(year_cyl.loc[(82, 4)])
    
    # Cross section
    print(year_cyl.xs(key=78, level='model_year'))
    print(year_cyl.xs(key=4, level='cylinders'))
    
    # filtering before grouping
    print(df[df['cylinders'].isin([6, 8])].groupby(['model_year', 'cylinders']).mean())
    
    # sorting index
    print(year_cyl.sort_index(level='model_year', ascending=False))
    
    # .agg()
    print(year_cyl.agg(['mean', 'std']))
    print(year_cyl.agg(['mean', 'std'])['mpg'])
    print(df.agg({'mpg':['mean', 'max'], 'weight': ['std', 'mean']}))
    
    
    

if __name__=='__main__':
    main()