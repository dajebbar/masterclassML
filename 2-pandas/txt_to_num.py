import pandas as pd
import numpy as np


fp = 'https://bit.ly/bitcoin-purchases'
bitcoin = pd.read_csv(fp)

bitcoin.columns = bitcoin.columns.str.lower().str.replace(' ', '_')
print(bitcoin.sample(10))
