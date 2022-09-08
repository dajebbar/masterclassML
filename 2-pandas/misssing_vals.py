import numpy as np
import pandas as pd

pd.set_option('display.max_columns', 0)

# Missing values options:
    # - Save
    # -Delete
    # - replace

def main():
    movies = pd.read_csv('nb/Datasets/movie_scores.csv')
    # print(movies)
    # print(movies.shape)
    # print(movies.isnull())
    # print(movies.isnull().sum())
    # print(movies.notnull())
    # print(movies[(movies['pre_movie_score'].isnull()) & (movies['first_name'].notnull())])
    
    # print(movies.dropna())
    # print(movies.dropna(thresh=1))
    # print(movies.dropna(thresh=4))
    print(movies.dropna(thresh=5))
    
    

if __name__=='__main__':
    main()