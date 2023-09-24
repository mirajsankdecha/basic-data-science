import pandas as pd
import matplotlib.pyplot as plt

Car_name = ["Audi", "Porche", "Toyota", "BMW"]
sales = [25, 50, 75, 95]
plt.pie(sales, labels=Car_name)
plt.show()
