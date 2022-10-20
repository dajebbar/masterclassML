import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# import missingno as msno
from sklearn import model_selection
from sklearn import metrics
from sklearn.preprocessing import (
    LabelEncoder, 
    OrdinalEncoder, 
    OneHotEncoder, 
    StandardScaler, 
    MinMaxScaler,
)
from sklearn.impute import SimpleImputer
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn import tree
from sklearn import ensemble
from sklearn.linear_model import LinearRegression
from sklearn.dummy import DummyRegressor
# import xgboost as xgb
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from sklearn.feature_extraction import DictVectorizer
# import optuna
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv("age_of_mariage.csv")

df['height'][~df['height'].isna()] = (
    df['height'][~df['height'].isna()].str.replace('"', "")
    .str.split("'").apply(
        lambda x: int(x[0])*30.48 + int(x[1])*2.54
    ).astype(float)
)

df['height'] = pd.to_numeric(df.height, errors='coerce')

df_modif = df.drop(columns=[
    'id',
    'location',
    'country', 
    'profession'])

print(df_modif.head())

data, target = (
    df_modif.drop(columns=['age_of_marriage']), df_modif['age_of_marriage'].
    fillna(df.age_of_marriage.mean())
) 