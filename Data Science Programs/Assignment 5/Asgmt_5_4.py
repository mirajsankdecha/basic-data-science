import pandas as pd

df = pd.read_excel("weekdata.xlsx")
print(df.columns)
print("*"*20)
print(df.size)
print("*"*20)
print(df.info())
print("*"*20)
print(df.count())
print("*"*20)
print(df.describe())
