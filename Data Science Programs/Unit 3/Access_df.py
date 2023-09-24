import pandas as pd

df = pd.read_csv("mycsv.csv")

# print(df.head(5))
# print(df.Name)
# print(df.Name[1])
# print(df.Name[2])
print(df.Branch[0:7])
print(df.Branch[0:7:2])
