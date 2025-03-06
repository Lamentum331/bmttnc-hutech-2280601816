def daonguoc(list):
    return list[::-1]
inputlist = input("Nhap danh sach cac so cach nhau dau phay: ")
numbers = list(map(int,inputlist.split(',')))
nguocdao= daonguoc(numbers)
print("List sau dao nguoc:", nguocdao)