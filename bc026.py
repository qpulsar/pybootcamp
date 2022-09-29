"""
1000 kez yazı tura (1/2)
"""
import random

yazi = 0
tura = 0
for tekrar in range(1, 100001):
    sayi = random.randint(1, 2)
    if sayi == 1:
        yazi += 1
    else:
        tura += 1

print("yazi = ", yazi)
print("tura = ", tura)