import pandas as pd

df = pd.read_csv("mycsv.csv", header=None)
print(df)

print(df.sort_index())
# print(df.sort_values(by="name"))
print(df.rank())
