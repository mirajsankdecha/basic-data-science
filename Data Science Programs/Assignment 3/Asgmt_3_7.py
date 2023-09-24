import re

f = open("ReadData.txt", "r")
fi = f.read()
ans = re.findall(r'[\w\.-]+@[\w\.-]+', fi)
print(ans)
f.close()
