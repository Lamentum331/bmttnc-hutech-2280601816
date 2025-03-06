sogiolam = float(input("Nhap so gio lam moi tuan: "))
luonggio = float(input("nhap thu lao tren moi gio lam tieu chuan: "))
giotieuchuan = 44
sogiovuotchuan = max(0,sogiolam - giotieuchuan)
thuclinh = giotieuchuan * luonggio + sogiovuotchuan * luonggio * 1.5
print (f"So tien linh: {thuclinh}")