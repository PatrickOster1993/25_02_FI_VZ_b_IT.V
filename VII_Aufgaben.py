#Aufgabe VII 1
print("Bitte registrieren Sie sich zunächst.")
name = input("Wie heißen Sie? ")
passwort = input(f"Hey {name}, bitte leg jetzt ein Passwort fest: ")

print("Registrierung erfolgreich! Jetzt nur noch einloggen. ")

login_name = input("Benutzername: ")
login_passwort = input("Passwort: ")

if login_name == name and login_passwort == passwort:
    print(f"Herzlich Willkommen, {name}!")
else:
    print("Falscher Benutzername oder Passwort!")

#Aufgabe VII 2
zimmerpreis=70
anzahl_personen=int(input("Mit wievielen Personen werden sie anreisen ? "))
dauer=int(input("Wie viele Tage werden sie bleiben (Dauer in Tagen) ? "))
Mwst=1.19
nettopreis=zimmerpreis*anzahl_personen*dauer
gesammtpreis=nettopreis*Mwst
aufschlag=20

if dauer == 1:
    print(f"Sie zahlen {gesammtpreis+aufschlag:.2f} € ")
else:
    print(f"Sie zahlen {gesammtpreis:.2f} € ")


