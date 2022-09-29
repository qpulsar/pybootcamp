# tekrar eden kalmasın
sayilar = [1, 5, 3, 5, 9, 3, 8, 1, 0, 8]
yeni = []

for i in sayilar:
    if i not in yeni:
        yeni.append(i)       # yeni += [i]

print(yeni)