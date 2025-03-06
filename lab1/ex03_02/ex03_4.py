def truycap(tupledata):
    first= tupledata[0]
    last = tupledata[-1]
    return first,last
inputyuple = eval(input("nhap tuple:"))
first,last = truycap(inputyuple)
print("phan tu dau:", first)
print("Phan tu cuoi", last)