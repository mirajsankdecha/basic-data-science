import pandas as pd

df = pd.read_csv("mycsv.csv", header=None, names=[
                 'a', 'b', 'c', 'd', 'e', 'f'])
print(df)
