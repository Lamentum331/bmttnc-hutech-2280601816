def demso(list):
    count = {}
    for item in list:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1
    return count
inputstr = input("nhap danh sach:")
wordlist = inputstr.split()
solanXH = demso(wordlist)
print("So lan xuat hien:", solanXH)            