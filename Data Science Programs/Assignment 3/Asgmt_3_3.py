import re

f = open("ReadData.txt", "r")
fi = f.read()
ans = re.findall(r"\b\d{2}\W\d{2}\W\d{4}\b", fi)
print(ans)
f.close()
