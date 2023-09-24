import re

f = open("ReadData.txt", "r")
fi = f.read()
ans = re.findall(r"\b\w{5}\b", fi)
print(ans)
f.close()
