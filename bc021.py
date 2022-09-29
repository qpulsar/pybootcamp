"""
Kullanıcının girdiği 2 sayıdan büyük olanı bulun
"""
sayi1=int(input("Birinci sayıyı giriniz:"))
sayi2=int(input("İkinci sayıyı giriniz:"))
if sayi1>sayi2:
    print(f"{sayi1} daha büyük")
elif sayi2>sayi1:
    print(f"{sayi2} daha büyük")
else:
    print("eşitler")

