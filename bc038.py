d = []
# 250ye kadar 3e bölünen sayıların 2 katını
# diziye akataran döngü
for i in range(250):
    if i % 3 == 0:
        d += [i * 2]
print(d)

# Pythonic !!!!
dizi = [i * 2 for i in range(250) if i % 3 == 0]
print(dizi)

# Pythonic
a = 5
b = 8
# swap
c = a
a = b
b = c
a, b = b, a
x = y = z = q = w = 82

