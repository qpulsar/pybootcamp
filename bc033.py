"""
Tersinden ve düzünden aynı okunan ifadelere palindrom denir
girilen metnin palindrom olup olmadığını bulan program
"""

kelime = input("kelime giriniz:")
if kelime == kelime[::-1]:
    print("palindrom")
else:
    print("değil")
