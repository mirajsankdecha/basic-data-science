import re

f = open("ReadData.txt", "r")
fi = f.read()
ans = re.findall(r"\b\d{10}\b", fi)
print(ans)
f.close()
