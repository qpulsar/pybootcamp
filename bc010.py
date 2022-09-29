sayi1 = float(input("1. Sayıyı giriniz :"))
sayi2 = float(input("2. Sayıyı giriniz :"))
print("--- MENÜ ---")
print("1- Toplama")
print("2- Çıkarma")
print("3- Bölme")
print("4- Çarpma")
secim = input("Seçiminiz -->")
if secim == "1":
    print(f"{sayi1}+{sayi2} = {sayi1 + sayi2}")
elif secim == "2":
    print(f"{sayi1}-{sayi2} = {sayi1 - sayi2}")
elif secim == "3":
    print(f"{sayi1}/{sayi2} = {sayi1 / sayi2}")
elif secim == "4":
    print(f"{sayi1}*{sayi2} = {sayi1 * sayi2}")
else:
    print("Ben sadece 4 işlem biliyorum")