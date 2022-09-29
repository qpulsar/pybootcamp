"""
bir dizinin içine 0-100 arası
50 adet rastgele sayı yerleştiriniz
"""
import random

d = []
for i in range(0, 50):
    d.append(random.randint(0, 100))
print(d)
