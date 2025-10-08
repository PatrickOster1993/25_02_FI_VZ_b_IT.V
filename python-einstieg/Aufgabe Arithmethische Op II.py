# anzahl_personen=int(input("Wie viele Personen: "))
# aufenthalsdauer=int(input("Aufenthaltsdauer (in Tagen): "))
# zimmerpreis=70

# nettopreis=zimmerpreis*aufenthalsdauer*anzahl_personen
# gesamtpreis=nettopreis*1,19

# print(f"Der Gesamtpreis beträgt: {gesamtpreis}€")

#netto=120
#steuer=7
#brutto=netto+steuer

#print(f"Bruttobetrag: {brutto}")

anzahl_apfel=int(input("Anzahl der Äpfel: "))
preis_apfel=float(input("Preis eines Apfels: "))

anzahl_banane=int(input("Anzahl der Bananen: "))
preis_banane=float(input("Preis einer Banane: "))

anzahl_orange=int(input("Anzahl der Orangen: "))
preis_orange=float(input("Preis einer Orange: "))

gesamtpreis_apfel=anzahl_apfel*preis_apfel
gesamtpreis_banane=anzahl_banane*preis_banane
gesamtpreis_orange=anzahl_orange*preis_orange

gesamtpreis=gesamtpreis_apfel+gesamtpreis_banane+gesamtpreis_orange
print("")
print(f"Der Gesamtpreis der Äpfel: {gesamtpreis_apfel:.2f}€")
print("")
print(f"Der Gesamtpreis der Bananen: {gesamtpreis_banane:.2f}€")
print("")
print(f"Der Gesamtpreis der Orangen: {gesamtpreis_orange:.2f}€")
print("-----------------------------------------------------")
print(f"Der Gesamtpreis des Obstes beträgt: {gesamtpreis:.2f}€")
print("")
