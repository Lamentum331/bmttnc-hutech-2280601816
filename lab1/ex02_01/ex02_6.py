inputstr = input("Nhap X,Y: ")
dimmension = [int(x) for x in inputstr.split(',')]
rowNum=dimmension[0]
colnum=dimmension[1]
multi =[[0 for col in range(colnum)] for row in range(rowNum)]
for row in range(rowNum):
    for col in range(colnum):
        multi[row][col] = row*col
print(multi)