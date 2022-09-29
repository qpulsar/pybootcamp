from tkinter import *
import tkinter.ttk as ttk
import sqlite3
from tkinter import messagebox

root = Tk()
root.title("CRUD")
root.geometry("1000x500-0+100")


def baglanti():
    global baglan, cursor
    baglan = sqlite3.connect("obs.db")
    cursor = baglan.cursor()
    sql = """
    create table if not exists `ogrenci` (
    id integer primary key autoincrement,
    isim text,
    numara text,
    vize int,
    fin int,
    but int)
    """
    cursor.execute(sql)
    # durumu yazdır

    baglan.commit()


def kaydet():
    global baglan, cursor
    sql = f"insert into ogrenci (isim, numara,vize,fin,but) values ('{isim.get()}'," \
          f"'{numara.get()}',{vize.get()},{fin.get()},{but.get()})"
    cursor.execute(sql)
    baglan.commit()
    l_mesaj["text"] = "Kayıt yapıldı."
    l_mesaj["bg"] = "pale violet red"
    isim.set("")
    numara.set("")
    vize.set(0)
    fin.set(0)
    but.set(0)


def listele():
    global baglan, cursor
    tree.delete(*tree.get_children())
    sql = "select * from ogrenci order by id"
    cursor.execute(sql)
    veriler = cursor.fetchall()
    for satir in veriler:
        if satir[5] != 0:
            ortalama = satir[3] * 0.4 + satir[5] * 0.60
        else:
            ortalama = satir[3] * 0.4 + satir[4] * 0.60
        if (satir[4] >= 50 or satir[5] >= 50) and ortalama >= 45:
            sonuc = "Başarılı"
        else:
            sonuc = "Başarısız"
        tree.insert("", 'end', values=
        (satir[0], satir[1], satir[2], satir[3], satir[4], satir[5], ortalama, sonuc))
        l_mesaj["text"]="Tüm kayıtlar listelendi."
        l_mesaj["bg"]="lime green"

# ---------- MAIN ------------
isim = StringVar()
numara = StringVar()
vize = IntVar()
fin = IntVar()
but = IntVar()
f_baslik = ("Times New Roman", 22)
f_hepsi = ("Tahome", 16)
baglanti()

ust = Frame(root, width=1000, height=50, relief=GROOVE, bd=5)
Label(ust, text="CRUD İŞLEMLERİ", bg="turquoise4", fg="blue4", font=f_baslik). \
    pack(expand=True, fill=BOTH)
ust.pack(side=TOP, expand=True, fill=X)

alt = Frame(root, width=1000, height=50, relief=GROOVE, bd=2)
l_mesaj=Label(alt, text="Hoşgeldiniz..", bg="turquoise4", fg="blue4", font=f_hepsi)
l_mesaj.pack(expand=True, fill=BOTH)
alt.pack(side=BOTTOM, expand=True, fill=X)

sol = Frame(root, width=400, height=400, relief=RAISED, bg="lightblue")
l_isim = Label(sol, text="İsim", font=f_hepsi, relief=FLAT)
l_isim.grid(row=0, column=0, sticky=E)
l_numara = Label(sol, text="Numara", font=f_hepsi, relief=FLAT)
l_numara.grid(row=1, column=0, sticky=E)
l_vize = Label(sol, text="Vize", font=f_hepsi, relief=FLAT)
l_vize.grid(row=2, column=0, sticky=E)
l_final = Label(sol, text="Final", font=f_hepsi, relief=FLAT)
l_final.grid(row=3, column=0, sticky=E)
l_butunleme = Label(sol, text="Bütünleme", font=f_hepsi, relief=FLAT)
l_butunleme.grid(row=4, column=0, sticky=E)
e_isim = Entry(sol, textvariable=isim, font=f_hepsi, relief=SUNKEN)
e_isim.grid(row=0, column=1, sticky=W)
e_numara = Entry(sol, textvariable=numara, font=f_hepsi, relief=SUNKEN, width=14)
e_numara.grid(row=1, column=1, sticky=W)
e_vize = Entry(sol, textvariable=vize, font=f_hepsi, relief=SUNKEN, width=3)
e_vize.grid(row=2, column=1, sticky=W)
e_final = Entry(sol, textvariable=fin, font=f_hepsi, relief=SUNKEN, width=3)
e_final.grid(row=3, column=1, sticky=W)
e_butunleme = Entry(sol, textvariable=but, font=f_hepsi, relief=SUNKEN, width=3)
e_butunleme.grid(row=4, column=1, sticky=W)

dugmeler = Frame(sol, width=400, height=80, bg="lightblue")
dugmeler.grid(row=5, column=0, columnspan=2, sticky=S)
btn_kaydet = Button(dugmeler, command=kaydet, width=10, text="Kaydet")
btn_kaydet.grid(row=0, column=0, pady=230)
btn_oku = Button(dugmeler, width=10, text="Oku", command=listele)
btn_oku.grid(row=0, column=1, pady=150)
btn_guncelle = Button(dugmeler, width=10, text="Güncelle")
btn_guncelle.grid(row=0, column=2, pady=150)
btn_sil = Button(dugmeler, width=10, text="Sil")
btn_sil.grid(row=0, column=3, pady=150)
btn_cik = Button(dugmeler, width=10, text="Çık")
btn_cik.grid(row=0, column=4, pady=150)

sol.pack(side=LEFT, expand=True, fill=BOTH)

sag = Frame(root, width=600, height=400, relief=RAISED, bg="lightgreen")
sag.pack(side=RIGHT, expand=True, fill=BOTH)

# Listeleme Tablosu
dikey = Scrollbar(sag, orient=VERTICAL)
yatay = Scrollbar(sag, orient=HORIZONTAL)
tree = ttk.Treeview(sag,
                    columns=["SN", "İsim", "Numara", "Vize", "Final", "Büt", "Ort", "Sonuç"],
                    selectmode="extended", height=400,
                    yscrollcommand=dikey.set,
                    xscrollcommand=yatay.set)
dikey["command"] = tree.yview
dikey.pack(side=RIGHT, fill=Y)
yatay["command"] = tree.xview
yatay.pack(side=BOTTOM, fill=X)
tree.heading("SN", text="SN", anchor=W)
tree.heading("İsim", text="İsim", anchor=W)
tree.heading("Numara", text="Numara", anchor=W)
tree.heading("Vize", text="Vize", anchor=W)
tree.heading("Final", text="Final", anchor=W)
tree.heading("Büt", text="Bütünleme", anchor=W)
tree.heading("Ort", text="Ortalama", anchor=W)
tree.heading("Sonuç", text="Sonuç", anchor=W)
tree.column("#0", stretch=NO, minwidth=0, width=0)
tree.column("#1", stretch=NO, minwidth=0, width=30)
tree.column("#2", stretch=NO, minwidth=0, width=130)
tree.column("#3", stretch=NO, minwidth=0, width=60)
tree.column("#4", stretch=NO, minwidth=0, width=50)
tree.column("#5", stretch=NO, minwidth=0, width=50)
tree.column("#6", stretch=NO, minwidth=0, width=50)
tree.column("#7", stretch=NO, minwidth=0, width=50)
tree.column("#8", stretch=NO, minwidth=0, width=50)
tree.pack()
root.mainloop()
