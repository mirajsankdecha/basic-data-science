import pandas as pd

df = pd.read_excel("weekdata.xlsx")
print(df.shape)
ndf = df.fillna(0)
print(ndf.head(25).to_string())
