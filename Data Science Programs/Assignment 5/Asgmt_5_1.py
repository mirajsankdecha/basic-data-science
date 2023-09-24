import pandas as pd

data = {
    "ID": [1, 2, 3, 4, 5],
    "Name": ["A", "B", "C", "D", "E"],
    "City": ["Windsor", "Tokyo", "Rio", "Torrento", "Dubai"],
    "Department": ["Computer", "Security", "Administration", "Finance", "HR"],
    "Designation": ["Software Engineer", "System Analyst", "Project Manager", "Programmer Analyst", "Manager"],
    "Salary": [250000, 300000, 350000, 400000, 500000]
}
df = pd.DataFrame(data)
print(df)
print(df.shape)
print(df.size)
