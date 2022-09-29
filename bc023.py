"""
1-100 arası 3e tam bölünen sayılar
"""
for i in range(1, 101):
    if i % 3 == 0:
        print(i, end="-")
    