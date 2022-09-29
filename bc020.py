"""
Kullanıcının girdiği 3 sayının ortalamasını bulan program
"""
toplam = 0
for i in range(0, 3):
    toplam += int(input("Sayı giriniz"))
print("ortalama=", toplam / 3)
