"""
Verilan sayının faktöriyelini hesaplayan fonksiyon
5! = 5*4*3*2*1
"""


def faktoriyel(sayi):
    f = 1
    for i in range(2, sayi + 1):
        f *= i
    print(f)

faktoriyel(5)