import pandas as pd
import matplotlib.pyplot as plt

x1 = [1, 2, 3]
x2 = [10, 13, 20]
y1 = [1.5, 2.4, 4]
y2 = [12, 19, 26]
plt.scatter(x1, x2)
plt.scatter(y1, y2)
plt.xlabel("Age")
plt.ylabel("Grade")
plt.title("Result Information")
plt.show()
