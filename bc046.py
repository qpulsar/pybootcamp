"""
parametre olarak verilen sayıya kadar sayıları ekrana yazan fonksiyon
"""


def sayi_yaz(sayi):
    for i in range(1, sayi + 1):
        print(i, end="-")
    print()


sayi_yaz(10)
