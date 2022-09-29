# bir dizinin içine 1-100 arası 10 tane sayı atınız
# dizideki en büyük sayıyı buldurunuz

import random

dizi = []
for i in range(10):
    dizi.append(random.randint(1, 100))

print(max(dizi))
eb = dizi[0]
for d in dizi:
    if d > eb:
        eb = d
print("en büyük sayı:", eb)
