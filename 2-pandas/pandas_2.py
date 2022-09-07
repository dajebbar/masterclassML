import pandas as pd
import numpy as np

np.random.seed(101)
pd.set_option('display.max_columns', 0)

def main():
    '''
        filrage conditionnel:
            par condition unique
            par plusieurs conditions
            vérification par rapport à plusieurs valeurs possibles
    '''
    data = np.array([
        [1776, 328, 20.5],
        [1867, 38, 1.7],
        [1821, 126, 1.22]
    ])
    df = pd.DataFrame(data=data, 
                    index=['USA', 'CANADA', 'MEXICO'],
                    columns=['year', 'pop', 'gdp']
                    )
    # print(df)
    # filtering by pop
    # cond_1 = df['pop'] > 100.
    # print(df[cond_1])
    
    tips = pd.read_csv('notebooks/Datasets/tips.csv')
    # print(tips.head())
    # print(tips[tips['total_bill'] > 40])
    # print(tips[tips['sex']=='Male'])
    
    # print(tips[(tips['total_bill'] > 30) & (tips['sex']=='Male')])
    # print(tips['day'].unique())
    # print(tips[(tips['day']=='Sun') | (tips['day']=='Sat') | (tips['day']=='Fri')])
    
    options = ['Sun', 'Sat', 'Fri']
    print(tips[tips['day'].isin(options)])
    
    

if __name__=='__main__':
    main()