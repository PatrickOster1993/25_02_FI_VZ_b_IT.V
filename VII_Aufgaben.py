#Aufgabe VII 1
print("Bitte registrieren Sie sich zunächst.")
name = input("Wie heißen Sie? ")
passwort = input(f"Hey {name}, bitte leg jetzt ein Passwort fest: ")

print("Registrierung erfolgreich! Jetzt nur noch einloggen. ")

while True:
    login_name = input("Benutzername: ")
    login_passwort = input("Passwort: ")

    if login_name == name and login_passwort == passwort:
        print(f"Herzlich Willkommen, {name}!")
        break
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

#Aufgabe VII 3
print("Familienangebot ")

zimmerpreis = 70  # Preis pro Person und Nacht
aufenthalt = int(input("Wie viele Nächte möchten Sie bleiben? "))
alter_kind = int(input("Wie alt ist das Kind? "))

if alter_kind < 7:
    rabatt = 100
elif alter_kind >=18:
    rabatt = 0
else:
    rabatt = 70

kinderpreis = zimmerpreis * aufenthalt * (1 - rabatt / 100)
erwachsene_preis = 2 * zimmerpreis * aufenthalt
gesamtpreis = erwachsene_preis + kinderpreis

print("Angebot ")
print(f"Rabatt für das Kind: {rabatt}%")
print(f"Gesamtpreis für die Familie: {gesamtpreis:.2f} €")



