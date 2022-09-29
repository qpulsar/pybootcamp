from tkinter import *
import sqlite3

def baglanti():
    conn= sqlite3.connect("veritabni.db")
    if conn:
        print("bağlantı kuruldu")
    else:
        print("bağlantı kurulamadı")
        # exit(0)
    return conn

def sorgulaveyaz():
    sql = "select * from deneme"
    cursor = baglanti().cursor()
    cursor.execute(sql)
    sayac = 1
    while True:
        satir = cursor.fetchone()
        if satir is None:
            break
        Label(root, text=satir[0], width=10, relief=SOLID).grid(row=sayac, column=0)
        Label(root, text=satir[1], width=10, relief=SOLID).grid(row=sayac, column=1, sticky="EW")
        Label(root, text=satir[2], width=10, relief=SOLID).grid(row=sayac, column=2)
        sayac += 1

db = baglanti()
root = Tk()
root.title("sqlite browser")
root.geometry("500x500-0+100")

Label(root, text="ID", width=10, relief=RAISED).grid(row=0, column=0)
Label(root, text="İsim", width=30, relief=RAISED).grid(row=0, column=1)
Label(root, text="Yaş", width=10, relief=RAISED).grid(row=0, column=2)
sorgulaveyaz()
root.mainloop()
db.close()