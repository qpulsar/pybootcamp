sozluk = {"isim": "Emin", "yas": 82, "kilo": 182, "yas": 17}
print(sozluk["isim"])
print(sozluk)
sozluk["yas"] = 42
print(sozluk)

for key, value in sozluk.items():
    print(key, value)
