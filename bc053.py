from tkinter import *
from tkinter.ttk import *


def bak():
    print(f"gündüz müymüş{kontrol.get()}")


window = Tk()
window.geometry("400x400-50+100")
window.title("Günaydın")

kontrol = BooleanVar()
kontrol.set(True)

chk = Checkbutton(window, text="Gündümüz mü?", var=kontrol)
chk.pack()

btn=Button(window,text="Kontrol Et", command=bak)
btn.pack()
window.mainloop()