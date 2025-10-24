# Aufgabe 1: Umsatzberechnung

umsatz = [1200, 1500, 900, 2000, 1700, 1300]

gesamtumsatz = sum(umsatz)

durchschnitt = gesamtumsatz/len(umsatz)

for i in umsatz:
    if i > durchschnitt:
        print(f"\n - {i} €")
print()
