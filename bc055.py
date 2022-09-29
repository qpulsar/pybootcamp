from tkinter import *


def topla():
    try:
        s3.set(int(s1.get())+int(s2.get()))
    except:
        s3.set("Geçersiz veri")

def cikar():
    try:
        s3.set(int(s1.get())-int(s2.get()))
    except:
        s3.set("Geçersiz veri")
def bol():
    try:
        s3.set(int(s1.get())/int(s2.get()))
    except:
        s3.set("Geçersiz veri")
def carp():
    try:
        s3.set(int(s1.get())*int(s2.get()))
    except:
        s3.set("Geçersiz veri")

root = Tk()
root.title("Hesap Makinesi V0.1")
root.geometry("300x300-50+50")

s1 = StringVar()
s2 = StringVar()
s3 = StringVar()
s3.set("İşlem Seç")

Entry(textvariable=s1, font=("Arial", 30)).pack()
Entry(textvariable=s2, font=("Arial", 30)).pack()
Label(textvariable=s3, font=("Verdana", 25)).pack()
bf = ("Comic Sans Ms", 30)
Button(text="+", command=topla, font=bf).pack(side=LEFT)
Button(text="-", command=cikar, font=bf).pack(side=LEFT)
Button(text="/", command=bol, font=bf).pack(side=LEFT)
Button(text="*", command=carp, font=bf).pack(side=LEFT)

root.mainloop()
