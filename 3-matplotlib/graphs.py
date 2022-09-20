import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


x = np.arange(10)
y = x **2 +3*x - 5
plt.figure(figsize=(6, 4))
plt.plot(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(0, 10)
plt.ylim(0, 110)
plt.title('Quadratic')
plt.show()