import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Result.csv")
x = df.age
y = df.grade
plt.bar(x, y)
plt.xlabel("Age")
plt.ylabel("Grade")
plt.title("Result Information")
plt.show()
