import sqlite3

print(sqlite3.version)
baglanti = sqlite3.connect("veritabni.db")

if baglanti:
    print("bağlantı kuruldu")
else:
    print("bağlantı kurulamadı")
cursor = baglanti.cursor()
cursor.execute("""
create table if not exists deneme(
id integer primary key autoincrement,
isim text,
yas int
)
""")
baglanti.commit()

cursor.execute("""
insert into deneme (isim, yas) values('Süheyla', 27) 
""")
baglanti.commit()

kayitlar = baglanti.execute("select * from deneme")
print(kayitlar.fetchall())
baglanti.close()
