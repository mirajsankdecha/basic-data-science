char = "A"
for i in range(65, 91):
    char = chr(i)
    with open(char+".txt", "w") as f:
        f.write(char)
