"""
0 yazıncaya kadar girilen sayıların toplamını bulan program
"""
print("çıkmak için 0 giriniz")
toplam = 0
sayi = None
while sayi != 0:
    sayi = int(input("Sayı giriniz:"))
    toplam = toplam + sayi # toplam += sayi
print("toplam=", toplam)
