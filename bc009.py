print("Menü")
print("1- Dikdörtgenin alanı")
print("2- Dairenin alanı")
secim = int(input("Seçiminiz:"))

if secim == 1:
    print("Dikdörtgen")
    a = float(input("Birinci kenarı girin:"))
    b = float(input("İkinci kenarı girin:"))
    print(f"dikdörtgenin alanı={a * b}")
elif secim == 2:
    print("Daire")
    r = float(input("Yarı çapı girin:"))
    print(f"dairenin alanı={3.14 * pow(r, 2)}")
else:
    print("Yanlış seçim")
