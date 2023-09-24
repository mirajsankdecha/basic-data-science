import re

f = open("ReadData.txt", "r")
fi = f.read()
ans = re.findall(r".$", fi)
if ans != []:
    print("Yes,It ends with Dot(.)")
else:
    print("No, It not ends with Dot(.)")
f.close()
