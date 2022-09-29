"""
sayının üssünü bulan fonksiyon
"""


def us(taban, kuvvet):
    sonuc = 1
    for i in range(kuvvet):
        sonuc *= taban
    return sonuc


print(us(4, 3))

