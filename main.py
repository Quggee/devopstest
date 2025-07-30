import calendar

print("Herzlich willkommen im Kalender\n")

year = int(input("Gib bitte das Jahr ein: "))
month = int(input("Gib bitte die Monatsnummer ein: "))

print(calendar.month(year, month))
print("Alles Gute!")
