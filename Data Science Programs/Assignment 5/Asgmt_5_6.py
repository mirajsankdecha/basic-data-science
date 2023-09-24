import pandas as pd

df = pd.read_excel("weekdata.xlsx")

print("____________________A____________________")
print(df["AnsweringAgent"].to_string())
print("____________________B____________________")
print(df.index)
print(df[1:6815:2].to_string())
print("____________________C____________________")
print(df[df["DayOfWeek"] == "mon"])
print("____________________D____________________")
print(df[df["ReasonForCall"] == "Complaint"])
print("____________________E____________________")
tc = df[df["CallDuration"] > 10]
print(tc.to_string())
print("____________________F____________________")
ag = df[df["AnsweringAgent"] == "David"].to_string()
print("____________________G____________________")
count_calls = len(df[(df['TimeOfDay'] > '09:30:00')])
print("Number of calls made after 9.30am:", count_calls)
print("____________________H____________________")
df.dropna(inplace=True)
print(df)
print("____________________I____________________")
ndf = df.dropna(axis=1)
print(ndf)