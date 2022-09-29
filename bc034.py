"""
Kullanıcının girdiği kelime palindrom oluncaya kadar
yeni kelime isteyen program
"""
kelime = None
while True:
    kelime = input("palindrom giriniz:")
    if kelime == kelime[::-1]:
        break
    print("olmadı")
print("tebrikler")