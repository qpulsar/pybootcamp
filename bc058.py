from tkinter import *
import random


def uzerinde(w):
    bizimki = w.widget
    bizimki["bg"] = "violetred"


def gitti(w):
    bizimki = w.widget
    bizimki["bg"] = "dodgerblue"


def tiklandi(w):
    bizimki = w.widget
    global kalan_mayin_sayisi
    if bizimki["text"] in (".", "*"):
        return 
    if int(bizimki["text"]) in mayin_tarlasi:
        print("Patladı", bizimki["text"])
        kalan_mayin_sayisi -= 1
        lbl_mayin_sayisi["text"] = kalan_mayin_sayisi
        bizimki["text"] = "*"
    else:
        bizimki["text"] = "."


def sure_ilerle():
    global sure
    if kalan_mayin_sayisi > 0 and devam:
        sure += 1
        lbl_sure["text"] = sure
        lbl_sure.after(1000, sure_ilerle)


f = ("Tahoma", 20)
mayin_sayisi = 25
kalan_mayin_sayisi = mayin_sayisi
mayin_tarlasi = []
sure = 0
devam = True
for i in range(mayin_sayisi):
    temp = random.randint(0, 399)
    while temp in mayin_tarlasi:
        temp = random.randint(0, 399)
    mayin_tarlasi += [temp]
print(mayin_tarlasi)

root = Tk()
root.title("Mayın Tarlası 0.2")
root.geometry("570x500-0+0")

# -------------------------------
ustframe = Frame(root)
lbl_mayin_sayisi = Label(ustframe, text=kalan_mayin_sayisi,
                         font=f, width=12, height=2, bg="red3")
lbl_mayin_sayisi.grid(row=0, column=0)
lbl_yuz = Label(ustframe, text="\U0001F600",
                font=f, width=4, height=2, bg="orange3")
lbl_yuz.grid(row=0, column=1)
lbl_sure = Label(ustframe, text=0,
                 font=f, width=12, height=2, bg="yellow")
lbl_sure.grid(row=0, column=3)
lbl_sure.after(1000, sure_ilerle)
ustframe.grid(row=0, column=0)
# -------------------------------
altframe = Frame(root)
sira = 0
for satir in range(20):
    for sutun in range(20):
        lbl = Label(altframe, width=3, text=sira, relief=GROOVE)
        lbl.grid(row=satir, column=sutun, sticky="NEWS")
        lbl.sira = sira
        sira += 1
        lbl.bind("<Enter>", uzerinde)
        lbl.bind("<Leave>", gitti)
        lbl.bind("<Button-1>", tiklandi)

altframe.grid(row=1, column=0)
# ----------------------------------
root.mainloop()
