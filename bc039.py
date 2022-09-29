"""
Verilan sayı asal mı?
"""
#sadece python'da
sayi = 97
for i in range(2, sayi):
    if sayi % i == 0:
        print("Asal değil")
        break
else:
    print("asal")

#hepsi için
mesaj = "Asal"
for i in range(2, sayi):
    if sayi % i == 0:
        mesaj = "asal değil"
        break
print(mesaj)