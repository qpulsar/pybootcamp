metin = "emin hocayla Python süper bişey!"
bh = metin.upper()
print(bh)
print(metin.upper())
print(metin.lower())
print(metin.capitalize())
print(metin.replace('a','o', 1))
kelimeler = metin.split()
print(kelimeler)
print(kelimeler[2])

ifade = "  Yaz Kampı   "
print(ifade.lstrip())
print(ifade.rstrip())
print(ifade.strip())

print(metin.endswith("bişey!"))
print(metin.title())
print(metin.swapcase())
print(metin.count('e'))
a = "23213"
print("harf mi:", a.isalnum())
print("harf mi:", a.isalpha())
print("harf mi:", a.isnumeric())

