import sys
import calendar

print("Herzlich willkommen im Kalender\n")

try:
    year = int(sys.argv[1])
    month = int(sys.argv[2])
except (IndexError, ValueError):
    print("❗ Fehler: Bitte Jahr und Monat als Argumente übergeben (z. B. 2025 7)")
    sys.exit(1)

print(calendar.month(year, month))
print("Alles Gute!")
