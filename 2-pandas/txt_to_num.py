import pandas as pd
import numpy as np


fp = 'https://bit.ly/bitcoin-purchases'
bitcoin = pd.read_csv(fp)

bitcoin.columns = bitcoin.columns.str.lower().str.replace(' ', '_')

bitcoin['wire_amount'] = bitcoin['wire_amount'].apply(lambda num: float(num.replace('$', '')))
print(bitcoin.sample(10))
print()
print(bitcoin['wire_amount'].dtype)
