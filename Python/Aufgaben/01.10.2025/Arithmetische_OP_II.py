#Aufgabe 1 Angebot=======
#Feste Variablen=========
zimmer_preis = 70
mwst = 0.19
#Begüßung================
print("Willkommen bei Hotel Kunterbund")
print(f"Unser Zimmerpreis beträgt {zimmer_preis} pro Nacht und Person")
#Eingabe von Personen anzahl und Dauer des Aufenthalts 
anzahl = int(input("Anzahl der Personen eingeben"))
dauer = int(input("Dauer Ihres aufenthalts in Ganzen Tagen angeben"))
#Berechnung==============
netto_preis = zimmer_preis*anzahl*dauer
gesamt_preis = netto_preis*(1+mwst)
#Ausgabe=================
print(f"Ihr Gesamtpreis beträgt {gesamt_preis}€")
print(f"Wir freuen uns auf Ihren Besuch")


#Aufgabe 2 Bruttobetrag==
#Feste Variablen=========
netto = 120
steuer = 7
#Berechnung==============
brutto = netto+steuer
#Ausgabe=================
print(brutto,"€")


#Aufgabe 3 Lebensmittel==
#Listen================== 
anzahl_obst = {"Äpfel":5,"Bananen":20,"Orangen":12}
preise_obst = {"Äpfel":0.40,"Bananen":0.90,"Orangen":0.60}
#Berechnung==============
gesamt_apfel = anzahl_obst.get("Äpfel")*preise_obst.get("Äpfel")
gesamt_banane = anzahl_obst.get("Bananen")*preise_obst.get("Bananen")
gesamt_orange = anzahl_obst.get("Orangen")*preise_obst.get("Orangen")
gesamt_obst = gesamt_apfel+gesamt_banane+gesamt_orange
#Ausgabe=================
print(f"Der Einkauf kostet {gesamt_obst:.2f}€")
