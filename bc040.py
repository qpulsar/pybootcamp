#1000e kadar asal sayıları veren program

asal = [2, 3]
limit = 1000

for i in range(5, limit+1, 2):
    bolundu = False
    for a in asal:
        if i % a == 0:
            bolundu = True
            break
    if not bolundu:   # bolundu == False
        print(f"{i} asal sayı")
        asal += [i]

print(asal)