from tkinter import *
import sqlite3


def temizle():
    isim.set("")
    yas.set(0)


def kaydet():
    global conn
    sql = f"insert into deneme(isim, yas) values ('{isim.get()}',{yas.get()})"
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

def baglanti():
    global conn
    conn = sqlite3.connect("veritabni.db")
    if conn:
        print("Bağlandık gülüm")
    else:
        print("Olmadı be hacı")


root = Tk()
root.title("Veri Ekle")
root.geometry("500x500-0+50")
isim = StringVar()
yas = IntVar()
Label(root, text="İsim", width=20).grid(row=0, column=0)
Entry(root, textvariable=isim, width=30).grid(row=0, column=1)
Label(root, text="Yaş", width=20).grid(row=1, column=0)
Entry(root, textvariable=yas, width=30).grid(row=1, column=1)
Button(root, text="Temizle", command=temizle).grid(row=2, column=0)
Button(root, text="Kaydet", command=kaydet).grid(row=2, column=1)
baglanti()

root.mainloop()
conn.close()
