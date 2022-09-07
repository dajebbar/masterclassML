import timeit


# Time comparaison between apply and vectorize methods

setup = '''
import pandas as pd
import numpy as np
tips = pd.read_csv('notebooks/Datasets/tips.csv')

def quality(bill, tip):
    if 100 * tip / bill > 25:
        return 'Generous'
    else:
        return 'Other'
'''

stmt_one = '''
tips['quality'] = tips[['total_bill', 'tip']].apply(
    lambda tips: quality(tips['total_bill'], tips['tip']),
    axis=1
    )
'''

stmt_two = '''
tips['vectorise_quality'] = np.vectorize(quality)(tips['total_bill'], tips['tip'])
'''

print(timeit.timeit(setup=setup, stmt=stmt_one, number=1000)) # 5.1464674990002095
print(timeit.timeit(setup=setup, stmt=stmt_two, number=1000)) # 0.6560884909995366
