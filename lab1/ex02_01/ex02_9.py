def ktsoprime(n):
    if n <=1:
        return False
    for i in range (2,int(n ** 0.5)+1):
        if n%1 == 0:
           return False
    return True
number = int(input("Nhap vao so: "))
if ktsoprime(number):
    print(number, "la so nguyen to")
else:
    print(number, "Khong phai so nguyen to")        