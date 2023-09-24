import pandas as pd

df = pd.read_csv("Student.csv")

clnm = input("Enter the Column Name: ")

print(df.sort_values(by=[clnm]))
