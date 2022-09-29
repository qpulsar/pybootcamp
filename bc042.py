# bir dizinin içine 1-100 arası 10 tane sayı atınız
# dizideki sayıların toplamını buldurunuz

import random

dizi = []
for i in range(10):
    dizi.append(random.randint(1, 100))

print(sum(dizi))

toplam = 0
for i in dizi:
    toplam += i
print(toplam)
