from tkinter import *


def fare_geldi(w):
    kutu = w.widget
    kutu["text"] = "O"
    kutu["bg"] = "SteelBlue2"


def fare_gitti(w):
    kutu = w.widget
    kutu["text"] = "*"
    kutu["bg"] = "sandybrown"


def fare_tik(w):
    kutu = w.widget
    kutu["text"] = "Z"
    kutu["bg"] = "tomato"

def zaman_ilerle():
    suretut.set(suretut.get()+1)
    sure.after(1000, zaman_ilerle)

root = Tk()
root.title("Mayın Tarlası 0.1")
root.geometry("520x500-0+0")

suretut = IntVar()
suretut.set(0)

baslikframe = Frame(root, bg="red")
kalanmayin = Label(baslikframe, width=11, text="20", bg="ivory2", font=("Arial", 25))
kalanmayin.grid(row=0, column=0)
gulenyuz = Label(baslikframe, width=5, text="\U0001F600", bg="IndianRed3", font=("Arial", 25))
gulenyuz.grid(row=0, column=1)
sure = Label(baslikframe, textvariable=suretut, width=11, text="0", bg="springgreen2", font=("Arial", 25))
sure.grid(row=0, column=2, sticky="EW")
sure.after(1000, zaman_ilerle())
baslikframe.grid(row=0, column=0, sticky="NEWS")

tarlaframe = Frame(root)
for satir in range(0, 10):
    for sutun in range(0, 10):
        lbl = Label(tarlaframe, text=f"{satir}x{sutun}", relief=SUNKEN,
                    width=6, height=2)
        lbl.grid(row=satir, column=sutun)
        lbl.bind("<Enter>", fare_geldi)
        lbl.bind("<Leave>", fare_gitti)
        lbl.bind("<Button-1>", fare_tik)

tarlaframe.grid(row=1, column=0, sticky="NEWS")

root.mainloop()
