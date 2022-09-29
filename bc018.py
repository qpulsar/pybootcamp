"""
Kullanıcının girdiği 3 sayının toplamını bulan program
"""
toplam = 0
for i in range(1, 4):
    toplam += int(input("Sayi giriniz:"))
print("toplam = ", toplam)
print(20*"-")
sayac =0
while sayac<4:
    sayi = int(input("Sayı giriniz:"))
    toplam += sayi
    sayac += 1
print("toplam = ", toplam)