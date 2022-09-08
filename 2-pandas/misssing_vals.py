import numpy as np
import pandas as pd

pd.set_option('display.max_columns', 0)

# Missing values options:
    # - Save
    # -Delete
    # - replace

def main():
    movies = pd.read_csv('nb/Datasets/movie_scores.csv')
    # isnull notnull
    
    # print(movies)
    # print(movies.shape)
    # print(movies.isnull())
    # print(movies.isnull().sum())
    # print(movies.notnull())
    # print(movies[(movies['pre_movie_score'].isnull()) & (movies['first_name'].notnull())])
    
    # dropna
    
    # print(movies.dropna())
    
    # dropna tresh
    
    # print(movies.dropna(thresh=1))
    # print(movies.dropna(thresh=4))
    # print(movies.dropna(thresh=5))
    
    # dropna subset
    # print(movies.dropna(subset=['last_name', 'pre_movie_score']))
    
    # fillna
    # print(movies['pre_movie_score'].fillna(0))
    print(movies['pre_movie_score'].fillna(movies['pre_movie_score'].median()))
    
    
    

if __name__=='__main__':
    main()