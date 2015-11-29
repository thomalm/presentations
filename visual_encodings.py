__author__ = 'thomasalm'

import matplotlib.pyplot as plt
from scipy import stats
import seaborn

x = [1, 2, 3]
y = [2, 3, 1]

plt.subplot(2, 4, 1)
plt.scatter(x, y, s=100);
plt.title("Position")

plt.subplot(2, 4, 2)
seaborn.distplot(x, kde=False);
plt.title("Length")

plt.subplot(2, 4, 3)
plt.plot(x, y);
plt.title("Direction")

plt.subplot(2, 4, 4)
plt.scatter(0, 0.5, s=50)
plt.scatter(1, 0.5, s=1000)
plt.title("Size")

plt.subplot(2, 4, 5)
plt.scatter(0, 0.5, marker='*', s=500);
plt.scatter(1, 0.5, marker=',', s=500);
plt.title("Shape")

plt.subplot(2, 4, 6)
plt.scatter(0, 0.5, c='r', s=500);
plt.scatter(1, 0.5, c='g', s=500);
plt.title("Color");

x = [1, 2, 3, 4, 5]
y = [1, 1, 1, 1, 1]
plt.subplot(2, 4, 7)
plt.scatter(x, y, c=x, s=300)
plt.title("Contrast")

plt.subplot(2, 4, 8)
plt.scatter(x, y, c=x, s=300, cmap="Blues")
plt.title("Color Saturation")

plt.tight_layout()
plt.show()
