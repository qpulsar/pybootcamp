"""
1-100 rastgele sayı 50<= veya 50> büyük mü bulunuz
"""
import random

sayi = random.randint(1, 100)

if sayi<=50:
    print("elli veya daha küçük")
else:
    print("elliden büyük")
