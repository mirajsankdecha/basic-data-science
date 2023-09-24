import re

f = open("ReadData.txt", "r")
fi = f.read()
ans = re.findall(r"\bs\w*\b", fi)
print(ans)
f.close()
