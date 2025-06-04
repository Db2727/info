days = ["Montag","Dienstag","Mittwoch","Donnerstag","Freitag","Samstag","Sonntag"]

print("Geben sie einen Wochentag als Zahl ein!")
day_number = int(input("Tag (1-7): "))

if 1 <= day_number <= 7:
    print(days[day_number - 1])
else:
    print("Fehler: Ungültige Eingabe.")