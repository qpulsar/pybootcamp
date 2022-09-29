from tkinter import *


# görevler
def sayiekle(dugme):
    sayi.set(sayi.get() + str(dugme))


def islem(isaret):
    global noktavar
    sayi.set(sayi.get() + isaret)
    noktavar = False


def hesapla():
    global noktavar
    noktavar = False
    try:
        sayi.set(eval(sayi.get()))
    except:
        sayi.set("Geçersiz işlem")


def temizle():
    global noktavar
    noktavar = False
    sayi.set("")


def nokta():
    global noktavar
    if not noktavar:
        sayi.set(sayi.get()+".")
        noktavar = True


root = Tk()
root.title("Ultra Gelişmiş HM")
root.geometry("-50+50")

sayi = StringVar()
f = ("Comic Sans Ms", 20)
noktavar = False

Entry(root, textvariable=sayi, font=f) \
    .grid(row=0, column=0, columnspan=3, sticky="NEWS")

Button(root, text="C", font=f, bg="grey75", command=temizle) \
    .grid(row=0, column=3, sticky="NEWS")

dizilis = [7, 8, 9, 4, 5, 6, 1, 2, 3]
sayac = 0
for satir in range(1, 4):
    for sutun in range(0, 3):
        Button(root, text=dizilis[sayac], width=4, height=2, font=f,
               command=lambda p=dizilis[sayac]: sayiekle(p)) \
            .grid(row=satir, column=sutun, sticky="NEWS")
        sayac += 1
Button(root, text="0", width=4, height=2, font=f,
       command=lambda p=0: sayiekle(p)) \
    .grid(column=0, row=4, columnspan=2, sticky="NEWS")
Button(root, text=".", width=4, height=2, font=f, command=nokta) \
    .grid(column=2, row=4, sticky="NEWS")
Button(root, text="+", width=2, height=2, font=f, bg="IndianRed1",
       command=lambda: islem("+")) \
    .grid(column=3, row=1, sticky="NEWS")
Button(root, text="-", width=2, height=2, font=f, bg="IndianRed1",
       command=lambda: islem("-")) \
    .grid(column=3, row=2, sticky="NEWS")
Button(root, text="*", width=2, height=2, font=f, bg="IndianRed1",
       command=lambda: islem("*")) \
    .grid(column=3, row=3, sticky="NEWS")
Button(root, text="/", width=2, height=2, font=f, bg="IndianRed1",
       command=lambda: islem("/")) \
    .grid(column=3, row=4, sticky="NEWS")
Button(root, text="=", width=4, height=2, font=f, bg="Red1",
       command=hesapla) \
    .grid(column=0, row=5, columnspan=4, sticky="NEWS")

root.mainloop()
