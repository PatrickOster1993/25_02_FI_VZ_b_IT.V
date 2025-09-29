# 3. Aufgabe: Berechnung des Gesamtwerts mit "Wartesteuer"

"""
Berechnet den Gesamtwert eines Produkts, indem eine "Wartesteuer" 
von 7% auf den Nettopreis aufgeschlagen wird.
"""

# --- 1. Variablen definieren ---
    
# Der Netto-Preis (Originalpreis des Druckers)
netto_preis_euro = 120.00
    
# Der Steuersatz (7% "Wartesteuer" als Dezimalzahl)
wartesteuer_satz = 0.07  # 7 / 100
    
# --- 2. Wartesteuer und Gesamtwert berechnen ---
    
# Betrag der Wartesteuer in Euro
wartesteuer_betrag = netto_preis_euro * wartesteuer_satz
    
# Gesamtwert (Netto-Preis + Wartesteuer)
gesamt_wert_euro = netto_preis_euro + wartesteuer_betrag
    
# --- 3. Ergebnisse ausgeben ---
print("--- GESAMTWERT BERECHNUNG ---")
print(f"Netto-Preis:       {netto_preis_euro:.2f} €")
print(f"Wartesteuer-Satz:  {wartesteuer_satz * 100:.0f} %")
print("-" * 30)
print(f"Betrag Wartesteuer:  {wartesteuer_betrag:.2f} €")
print(f"Gesamtwert:        {gesamt_wert_euro:.2f} €")
print("------------------------------")
