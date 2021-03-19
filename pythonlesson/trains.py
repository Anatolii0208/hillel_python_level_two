from os import mkdir, rmdir, remove, rename, listdir, path

with open("part_data_1.txt", "r") as file:
    h = file.readline().split()
    print(h)
    rows=[]
    for line in file.readlines():
        rows.append(line.split())
print(rows)