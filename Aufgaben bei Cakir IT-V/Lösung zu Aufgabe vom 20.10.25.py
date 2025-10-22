#summe= 0
#anzahl = 0

#while True:
#    zahl = float(input("Gib eine positive Zahl ein (oder eine negative zum Beenden): "))

#    if zahl < 0:
#        break

#    summe += zahl
#    anzahl += 1

#if anzahl > 0:
#    durchschnitt = summe / anzahl
#    print("Der Durchschnitt der eingegebenen Zahlen ist:", durchschnitt)
#else:
#    print("Es wurden keine positiven Zahlen eingegeben.")



#richtiges_passwort = "Passwort"
#versuche = 0

#while versuche < 3:
#    eingabe = input("Bitte gib dein Passwort ein: ")

#    if eingabe == richtiges_passwort:
#        print("Login erfolgreich!")
#        break
#    else:
#        print("Falsches Passwort.")
#        versuche += 1

#if versuche == 3:
#    print("Zu viele Fehlversuche!")

zahl=int(input("Gibt eine Positive ganze Zahl ein: "))
anzahl = 0

if zahl == 0:
    anzahl = 1
else:
    while zahl > 0:
        zahl //= 10
        anzahl += 1

print("Die Zahl hat", anzahl, "Ziffern.")