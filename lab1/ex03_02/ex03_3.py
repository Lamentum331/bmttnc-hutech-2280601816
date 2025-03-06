def taotuple(list):
    return tuple(list)
inputlist = input("nhap danh sach cach nhau dau phay: ")
numbers = list(map(int,inputlist.split(',')))
mytuple = taotuple(numbers)
print("list:", numbers)
print("tuple:",mytuple)