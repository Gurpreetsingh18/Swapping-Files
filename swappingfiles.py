
data = ""
with open("file1.txt", "rb") as f:
    data = f.read()

with open("file2.txt", "rb") as f1:
    with open("file1.txt", "wb") as f2:
        f2.write(f1.read())

with open("file2.txt", "wb") as f:
    f.write(data)

del data




