def tinhtongchan(list):
    tong = 0
    for num in list:
        if num % 2 == 0 :
            tong += num
    return tong
inputlist = input("Nhap ds cach nhau boi dau phay: ")
numbers = list(map(int,inputlist.split(',')))
tongchan = tinhtongchan(numbers)
print(" tong chan trong list:", tongchan) 