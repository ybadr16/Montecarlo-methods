import numpy as np
import matplotlib.pyplot as plt


r = 3
N = int(1e6)

x = np.random.uniform(-r, r, N)
y = np.random.uniform(-r, r, N)

is_inside = x**2 + y**2 <= r**2
x_ins = x[is_inside]
y_ins = y[is_inside]

pi = 4* np.sum(is_inside)/ N


print(pi)
plt.scatter(x, y, s=0.5, color = "r")
plt.scatter(x_ins, y_ins, s=0.5, color ="b")
plt.show()


