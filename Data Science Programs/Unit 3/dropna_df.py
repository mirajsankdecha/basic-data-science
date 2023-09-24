import pandas as pd

df = pd.read_excel("weekdata.xlsx")

ndf = df.dropna(axis=0)
print(ndf.shape)
print(ndf.head(25).to_string)

print("$"*25)

ndf = df.dropna(axis=1)
print(ndf.shape)
print(ndf.head(25).to_string)
