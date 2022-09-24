import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

fp = 'https://bit.ly/missing-values'

df = pd.read_csv(fp)
# print(df.tail())

print(df.isna().sum())
