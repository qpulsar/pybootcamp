from tkinter import *
from tkinter.ttk import *
from tkinter import Label as Lab


def gorev():
    metin["text"] = txt.get()


pencere = Tk()
pencere.title("Altıkod Bootcamp")
pencere.geometry("400x300-50+100")
pencere.resizable(width=False, height=True)

metin = Lab(pencere, text="PythonU seviyorum")
metin["font"] = ("Comic Sans MS", 30)
metin["fg"] = "SteelBlue3"
metin["bg"] = "LemonChiffon"
metin.pack()

txt = Entry(pencere, width=20, font=("Arial", 20))
txt.pack()

btn = Button(pencere, text="Tıkla", command=gorev)
btn.pack()

combo = Combobox(pencere, values=("Can", "Cem"))
combo.current(0)
combo.pack()

pencere.mainloop()
