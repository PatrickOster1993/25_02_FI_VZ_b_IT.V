#VIII.1
zahl = 1

while zahl <= 10:
    print(zahl)
    zahl += 1


#VIII.2
zahl = 1
summe = 0

while zahl <= 5:
    summe += zahl
    zahl += 1

print("Die Summe der ersten 5 positiven Zahlen ist:", summe)


#VIII.3
zahl = 1

while 2 * zahl <= 50:
    ergebnis = 2 * zahl
    print(f"2 x {zahl} = {ergebnis}")
    zahl += 1

#IX.1
summe = 0
anzahl = 0

while True:
    zahl = float(input("Gib eine positive Zahl ein (oder eine negative zum Beenden): "))

    if zahl < 0:
        break

    summe += zahl
    anzahl += 1

if anzahl > 0:
    durchschnitt = summe / anzahl
    print("Der Durchschnitt der eingegebenen Zahlen ist:", durchschnitt)
else:
    print("Es wurden keine positiven Zahlen eingegeben.")


#IX.2
richtiges_passwort = "passwort"
versuche = 0

while versuche < 3:
    eingabe = input("Bitte gib dein Passwort ein: ")

    if eingabe == richtiges_passwort:
        print("Login erfolgreich!")
        break
    else:
        print("Falsches Passwort.")
        versuche += 1

if versuche == 3:
    print("Zu viele Fehlversuche!")
