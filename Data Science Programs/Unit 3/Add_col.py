import pandas as pd
import numpy as np

df = pd.read_excel("weekdata.xlsx")
df["Country"] = "India"
print(df)

ndf = df.drop("Country", axis=1)
print(ndf.to_string())

df.duplicated()
print(df)
