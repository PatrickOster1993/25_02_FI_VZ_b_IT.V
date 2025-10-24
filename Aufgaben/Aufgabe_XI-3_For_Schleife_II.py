# Aufgabe 3: Rabattberechnung

umsatz_kunden = [950, 1200, 800, 1500]

rabatt = 0

for i in range(len(umsatz_kunden)):
    if umsatz_kunden[i] > 1000:
        rabatt = umsatz_kunden[i]-umsatz_kunden[i]*0.1
        print(f"\nKunde Nr.{i} erhält 10% Rabatt und zahlt jetzt nur noch {rabatt} €")
print()
