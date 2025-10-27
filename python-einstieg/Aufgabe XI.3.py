umsatz_kunden = [950, 1200, 800, 1500]
rabatt_satz = 0.10

print("\n--- Rabattberechnung (10% über 1000 €) ---")

for umsatz in umsatz_kunden:
    endbetrag = umsatz
    
    if umsatz > 1000:
        rabatt_betrag = umsatz * rabatt_satz
        endbetrag = umsatz - rabatt_betrag
        print(f"Umsatz: {umsatz} € -> Rabatt: {rabatt_betrag:.2f} € -> Endbetrag: {endbetrag:.2f} €")
    else:
        print(f"Umsatz: {umsatz} € -> Kein Rabatt -> Endbetrag: {endbetrag:.2f} €")