# Aufgabe: Schreibe ein Program , das einen Betrag in Euro eingibt und diesen in US-Dollar umrechnet.
# Der Umrechnungskurs ist 1 Euro = 175,5 Yen
   #Eingabe: Betrag in Euro.
   #Ausgabe: Betrag in Yen.
   
betragineuro=float(input("Betrag in Euro,sofern Sie Geld haben: "))
aktuellerWechselkurs=float(input("Wieviel ist der aktuelle Wechselkurs Euro in Yen: "))
betraginYen= betragineuro*aktuellerWechselkurs
print(f"Sofern Sie Geld haben oder wollen bekommen sie genau {betraginYen:.2f2400}. Möchten Sie denn abheben?")

