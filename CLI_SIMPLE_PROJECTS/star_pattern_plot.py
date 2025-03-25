import matplotlib.pyplot as plt 
import numpy as np 

rows, cols = 5, 5

x = np.arange(cols)
y = np.arange(rows)
x, y = np.meshgrid(x, y)

X = x.flatten()
Y = y.flatten()
flg, ax = plt.subplots(figsize=(6,6))
ax.scatter(X, Y, marker='*', s=300, color='gold', edgecolors='black')

ax.set_xlim(-1, cols)
ax.set_ylim(-1, rows)
ax.set_xticks([])
ax.set_yticks([])
ax.set_frame_on(False)

plt.show()