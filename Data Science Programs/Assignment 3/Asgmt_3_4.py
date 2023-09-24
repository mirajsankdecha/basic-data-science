f = open("ReadData.txt", "r")
fi = f.read()
vovels = 0
for i in fi:
    if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        vovels = vovels+1
print("Numbers of Vovels are:", vovels)
f.close()
