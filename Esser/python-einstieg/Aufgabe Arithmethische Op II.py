#       Aufgabe Arithmethische Op II        #       Aufgabe_1       #
print("     ==========           ==========           ==========           ==========           ==========      ")
print("Programm zur Angebotserstellung von Hotelübernachtungen")
print("")

Mwst = 0.19
Preis_pP= 70
while True:
    Anzahl_der_Naechte= input("Geben Sie die Anzahl der Nächte an ")
    try:
        int_value = int(Anzahl_der_Naechte)
        print(f"Sie haben {int_value} Übernachtungen angegeben")
        break
    except ValueError:
        print("Sie müssen für die Anzahl der Nächte eine Ganzzahl eingeben")
while True:
    Anzahl_der_Personen = input("Geben Sie die Anzahl der Personen an ")
    try:
        int_value_2 = int(Anzahl_der_Personen)
        print(f"Sie haben {int_value_2} Personen angegeben")
        break
    except ValueError:
        print("Sie müssen für die Anzahl der Personen eine Ganzzahl eingeben")
Nettopreis = (Preis_pP*int_value*int_value_2)
Gesamtpreis = (Nettopreis*Mwst+Nettopreis)
print(f"Sie möchten für {Anzahl_der_Naechte} Übernachtungen mit {Anzahl_der_Personen} Personen im Hotel Monty einchecken.")
print(f"Der zu zahlede Gesamtbetrag für Ihren Aufenthalt beträgt: {Gesamtpreis:.2f} €")
print("")
Buchungsbestaetigung = input("Möchten Sie den Aufenthalt im Hotel Monty verbindlich buchen? (ja/nein) : ")
if Buchungsbestaetigung == 'Ja':
    print("Sie werden nun zur Zahlung weitergeleitet")
elif Buchungsbestaetigung == 'ja':
        print("Sie werden nun zur Zahlung weitergeleitet")
elif Buchungsbestaetigung == 'JA':
        print("Sie werden nun zur Zahlung weitergeleitet")
elif Buchungsbestaetigung == 'jA':
        print("Sie werden nun zur Zahlung weitergeleitet")
else : 
    print("Schade, wir hoffen Sie dennoch bald als unseren Gast begrüßen zu dürfen! :) ")


 

 
 
