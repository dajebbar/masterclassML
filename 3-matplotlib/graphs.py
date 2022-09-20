import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


x = np.arange(10)
y = x **2 +3*x - 5
a = np.linspace(0, 10, 11)
b = a **4

plt.figure(figsize=(6, 4))

plt.subplot(1, 2, 1)
plt.plot(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(0, 10)
plt.ylim(0, 110)
plt.title('Quadratic')

plt.subplot(1, 2, 2)
plt.plot(a, b)
plt.xlabel('a')
plt.ylabel('b')
plt.xlim(0, 10)
plt.ylim(0, 11000)
plt.title('X⁴')

plt.show()
# plt.savefig('../graphs/plot.png')