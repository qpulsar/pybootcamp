"""
Dairenin alanını bulan program
Emin
01.08.2022
"""
r = float(input("Dairenin yarı çapını giriniz:"))
alan = 3.14 * r * r

print("alan= ", alan)
print("yarı çapı", r,"olan dairenin alanı ",alan,"cm karedir.")
print(f"yarı çapı {r} olan dairenin alanı {alan} cm karedir.")
print("yarı çapı {} olan dairenin alanı {} cm karedir.".format(r, alan))
