#Aufgabe 3 Angebot Zimmerpreis
kind_alter = 17
erwachsene = 2
zimmer_preis = 230
kostenlos_unter = 6
rabatt_unter = 16
rabatt = 0.7
if kind_alter <= kostenlos_unter:
    gesamt = erwachsene*zimmer_preis
elif kind_alter < rabatt_unter:
    gesamt = erwachsene*zimmer_preis+zimmer_preis*(1-rabatt)
else:
    gesamt = erwachsene*zimmer_preis+zimmer_preis

print(f"Sie müssen {gesamt}€ Bezahlen")
