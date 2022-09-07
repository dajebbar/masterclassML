import pandas as pd
import numpy as np


def main():
    country_idx = ['USA', 'Canada', 'Mexico']
    independence_day = [1776, 1867, 1821]
    
    s = pd.Series(data=independence_day, index=country_idx)
    print(s)
    print(s[0])
    print(s[['USA']])
    
    ages = dict(sam=5, kane=10, lili=16)
    ages_s = pd.Series(ages)
    print(ages_s)
    cond = ages_s > 8
    print(ages_s[cond])
    
    q1 = {'Japan': 80, 'China': 450, 'India': 200, 'USA': 250}
    q2 = {'Brazil': 100,'China': 500, 'India': 210,'USA': 260}
    
    q1_sales = pd.Series(q1)
    q2_sales = pd.Series(q2)
    # print(q1_sales & q2_sales)
    print(q1_sales.index)
    print(q1_sales + q2_sales)
    print(q1_sales.add(q2_sales, fill_value=0))

if __name__=='__main__':
    main()
