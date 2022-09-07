import pandas as pd
import numpy as np

np.random.seed(101)
pd.set_option('display.max_columns', 0)

def main():
    tips = pd.read_csv('notebooks/Datasets/tips.csv')
    print(tips.sort_values(['total_bill']))
    print(tips.sort_values(['total_bill', 'size']))
    print(tips['total_bill'].max())
    print(tips['total_bill'].idxmax())
    print(tips.iloc[tips['total_bill'].idxmax()])
    print()
    print(tips.iloc[tips['total_bill'].idxmin()])
    
    print(tips.corr())
    
    print(tips['sex'].value_counts(normalize=True))
    
    # replace
    print(tips['sex'].replace(to_replace=['Female', 'Male'], value=['F', 'M']))
    # map
    print(tips['sex'].map({'Female':'F', 'Male':'M',}))
    
    # between
    print(tips['total_bill'].between(10, 20, inclusive=True).head())
    
    # nlargest nsmalest
    print(tips['total_bill'].nlargest(2))
    print(tips['total_bill'].sort_values(ascending=False).head(2))
    print()
    print(tips['total_bill'].nsmallest(2))
    print(tips['total_bill'].sort_values(ascending=True).head(2))
    
    #sample
    print(tips.sample(frac=.05))
    
    
    

if __name__=='__main__':
    main()