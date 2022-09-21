from cProfile import label
from tkinter import font
from turtle import title
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

x = np.arange(10)
y = x **2 +3*x - 5
a = np.linspace(0, 10, 11)
b = a **4

# plt.figure(figsize=(6, 4))

'''plt.subplot(1, 2, 1)
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
'''

# fig = plt.figure(figsize=(3, 2), dpi=150)

# axe1 = fig.add_axes([0, 0, 1, 1])
# axe1.plot(a, b)

# axe2 = fig.add_axes([0, .7, .35, .35])
# axe2.plot(x, y)

fig, ax = plt.subplots(1, 2)
fig.set_size_inches(10, 5)

ax[0].plot(x,y, label='X² vs X⁴')
ax[0].plot(a,b)
ax[1].plot(a,b)

ax[0].set(title='X²', xlabel='X', ylabel='Y')
ax[1].set(title='X⁴', xlabel='X', ylabel='Y')
fig.subplots_adjust(wspace=.4, hspace=.4)
fig.suptitle('Functions curve', fontsize=16)
ax[0].legend()
plt.show()
# fig.savefig('../graphs/ab_xy.png', bbox_inches='tight')
# fig.savefig('../graphs/a_b.png', bbox_inches='tight')
# plt.savefig('../graphs/plot.png')