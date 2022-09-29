"""
1-100 arası 3e veya 4e tam bölünen sayılar
"""
for i in range(1, 101):
    if i % 3 == 0 or i % 4 == 0:
        print(i, end="-")
