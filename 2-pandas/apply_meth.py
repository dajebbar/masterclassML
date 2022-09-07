import pandas as pd
import numpy as np

np.random.seed(101)
pd.set_option('display.max_columns', 0)

def main():
    tips = pd.read_csv('notebooks/Datasets/tips.csv')
    
    # apply in one column
    # tips['tips_4_num'] = tips['CC Number'].apply(lambda x: int(str(x)[-4:]))
    # print(tips.head())
    # print(tips['tips_4_num'].dtype)
    
    # tips['yelp'] = tips['total_bill'].apply(
    #     lambda price: '$' if price<10 else('$$' if 10<=price<30 else '$$$')
    #     )
    # print(tips.sample(n=10))
    
    def quality(bill, tip):
        if 100 * tip / bill > 25:
            return 'Generous'
        else:
            return 'Other'
    
    tips['quality'] = tips[['total_bill', 'tip']].apply(
        lambda tips: quality(tips['total_bill'], tips['tip']),
        axis=1
    )
    
    # vectorise
    tips['vectorise_quality'] = np.vectorize(quality)(tips['total_bill'], tips['tip'])
    print(tips.sample(n=20))
    
    
    
    

if __name__=='__main__':
    main()