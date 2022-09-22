import pandas as pd
import numpy as np


fp = 'https://bit.ly/bitcoin-purchases'
bitcoin = pd.read_csv(fp)

bitcoin.columns = bitcoin.columns.str.lower().str.replace(' ', '_')

bitcoin['wire_amount'] = bitcoin['wire_amount'].apply(lambda num: float(num.replace('$', '')))
# print(bitcoin.sample(10))
# print()
# print(bitcoin['wire_amount'].dtype)

bitcoin2 = pd.read_csv(fp+'2')
bitcoin2.columns = bitcoin.columns
# bitcoin2['wire_amount'] = bitcoin2['wire_amount'].apply(lambda num: float(num.replace(',', '.')[1:]))
# print(bitcoin2.sample(10))
# print(bitcoin2['wire_amount'].dtype)
# print(bitcoin2['wire_amount'].str.split(bitcoin2['wire_amount'][0], expand=True))
bitcoin2['wire_amount'].str.replace(',', '.')
# bitcoin2['currency'] = bitcoin2['wire_amount'].str[0]
bitcoin2.insert(loc=1, column='currency', value=bitcoin2['wire_amount'].str[0])
print(bitcoin2.sample(10))
