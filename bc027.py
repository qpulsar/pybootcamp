import random

sayi1 = random.randint(0, 100)
sayi2 = random.randint(0, 100)
sayi3 = random.randint(0, 100)
sayi4 = random.randint(0, 100)
sayi5 = random.randint(0, 100)
ortalama = (sayi1+sayi2+sayi3+sayi4+sayi5) / 5
print(ortalama)

toplam = 0
for i in range(0, 5):
    toplam += random.randint(0,100)

print(toplam / 5)
