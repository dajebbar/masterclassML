import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
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
import bentoml

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

data, target = (
    df_modif.drop(columns=['age_of_marriage']), df_modif['age_of_marriage'].
    fillna(df.age_of_marriage.mean())
) 

X = data.copy()
y = target.copy()

numerical = ['height']
categorical = ['gender', 'religion', 'caste', 'mother_tongue']

cat_encoder = LabelEncoder()

num_imputer = SimpleImputer(strategy='mean')

cat_imputer = SimpleImputer(
        strategy='most_frequent', 
        fill_value='unknown'
    )
  

X_full_train, X_test, y_full_train, y_test = model_selection.train_test_split(
      X,
      y,
      test_size=.2,
      random_state=42,
    )
X_train, X_dev, y_train, y_dev = model_selection.train_test_split(
          X_full_train,
          y_full_train,
          test_size=.25,
          random_state=42,
    )
  
X_train[numerical] = num_imputer.fit_transform(X_train[numerical])
X_dev[numerical] = num_imputer.transform(X_dev[numerical])
X_test[numerical] = num_imputer.transform(X_test[numerical])

X_train[categorical] = cat_imputer.fit_transform(X_train[categorical])
X_dev[categorical] = cat_imputer.transform(X_dev[categorical])
X_test[categorical] = cat_imputer.transform(X_test[categorical])

 
# X_train[categorical] = cat_encoder.fit_transform(X_train[categorical])
# X_dev[categorical] = cat_encoder.fit_transform(X_dev[categorical])
# X_test[categorical] = cat_encoder.fit_transform(X_test[categorical])

X_train[categorical] = X_train[categorical].apply(cat_encoder.fit_transform)
X_dev[categorical] = X_dev[categorical].apply(cat_encoder.fit_transform)
X_test[categorical] = X_test[categorical].apply(cat_encoder.fit_transform)

X = pd.concat([X_train, X_dev])
y = pd.concat([y_train, y_dev])

dv = DictVectorizer(sparse=False, sort=False)
X_dict = X.to_dict(orient="records")
X_test_dict = X_test.to_dict(orient="records")
X = dv.fit_transform(X_dict)
X_test = dv.transform(X_test_dict)


model = ensemble.RandomForestRegressor(
    n_estimators=82, 
    max_depth=15, 
    min_samples_leaf=6
)

model.fit(X,y)
y_pred = model.predict(X_test)

# print(f"MAE : {metrics.mean_absolute_error(y_test,y_pred)}")
# print(f"R² score: {metrics.r2_score(y_test,y_pred)}")

bento_model = bentoml.sklearn.save_model(
    "marriage_model",
    model,
    custom_objects={
        "dictVectorizer": dv
    }
)

print(bento_model.tag)