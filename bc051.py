import calendar

takvim = calendar.TextCalendar(calendar.MONDAY)
metin = takvim.formatmonth(2022, 8)
print(metin)

web_takvim = calendar.HTMLCalendar()
cetin = web_takvim.formatmonth(2022, 8)
print(cetin)