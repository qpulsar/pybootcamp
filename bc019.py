"""
kullanıcıdan adını ve kaç kez yazacağını alan program
"""
isim = input("isminiz:")
adet = int(input("Kaç kez yazalım:"))
#print(adet*isim)
for i in range(0, adet):
    print(isim)

