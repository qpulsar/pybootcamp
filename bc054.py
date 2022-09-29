from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Resim göster")
window.geometry("500x500-50+50")

resim = PhotoImage(file="logo.png")
lbl = Label(window, image=resim)
lbl.pack()

window.mainloop()