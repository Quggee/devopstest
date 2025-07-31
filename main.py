import calendar
from datetime import datetime

print("Herzlich willkommen im Kalender\n")

now = datetime.now()
year = now.year
month = now.month

print(f"Heutiger Monat: {month}/{year}\n")
print(calendar.month(year, month))
print("Alles Gute!")

