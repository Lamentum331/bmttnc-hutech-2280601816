def chiahetcho5(sonhiphan):
    sothapphan = int(sonhiphan,2)
    if sothapphan % 5 == 0:
        return True
    else:
        return False
chuoisonhiphan = input("Nhap chuoi nhi phan(phan tach boi dau phay): ")
sonhiphanlist = chuoisonhiphan.split(',')
sochiahetcho5 = [so for so in sonhiphanlist if chiahetcho5(so)]
if len(sochiahetcho5) > 0:
    ketqua = ','.join(sochiahetcho5)
    print("Cac so nhi phan chia het cho 5:", ketqua)
else:
    print("Ko co so")    