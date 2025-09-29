name_produkt=input("Name des Produktes: ")
nettopreis_produkt=float(input("Nettopreis des Produktes: "))
stückzahl=int(input("Gewünschte Stückzahl: "))
mwst_faktor=0.19

gesamt_netto=nettopreis_produkt*stückzahl
mwst=gesamt_netto*mwst_faktor
gesamt_brutto=gesamt_netto+mwst

gesamt_netto=str(gesamt_netto)
mwst=str(mwst)
gesamt_brutto=str(gesamt_brutto)

print("---------Bestellzusammenfassung---------")
print(f"Produkt: {name_produkt}")
print(f"Gesamt-Nettopreis: {gesamt_netto} EUR")
print(f"+19% MwSt.: {mwst} EUR")
print(f"Gesamt-Bruttopreis: {gesamt_brutto} EUR")