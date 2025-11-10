# 2. Aufgabe: Erstellen Sie eine neue Anwendung namens "Energieverbrauch".

"""
Berechnet den jährlichen Energieverbrauch und die Kosten basierend auf den Szenarien.
"""

# Allgemeine Konstanten
TAGE_IM_JAHR = 365
TAGE_PRO_WOCHE = 7
KOSTEN_PRO_KWH_CENT = 30  # 1 kWh = 30 Cent
KOSTEN_PRO_KWH_EURO = KOSTEN_PRO_KWH_CENT / 100.0  # 0.30 Euro/kWh

# Variable zur Speicherung des Gesamtverbrauchs
gesamtverbrauch_kwh = 0.0

# --- 2. Variablen für jedes Szenario definieren und den Verbrauch berechnen ---

# a) Fernseher (Game of Thrones)
# Info: 3 Fernseher, je 1 kWh, 3 Stunden täglich
ANZ_FERNSEHER = 3
LEISTUNG_TV_KW = 1.0
STUNDEN_TV_PRO_TAG = 3
    
verbrauch_tv_kwh = ANZ_FERNSEHER * LEISTUNG_TV_KW * STUNDEN_TV_PRO_TAG * TAGE_IM_JAHR
gesamtverbrauch_kwh += verbrauch_tv_kwh

# b) Herd
LEISTUNG_HERD_KW = 2.0
STUNDEN_HERD_PRO_KOCHVORGANG = 2
ANZ_KOCHVORGAENGE_PRO_WOCHE = 4
    
# Berechne die Tage pro Jahr, an denen gekocht wird: (4 Tage/Woche) * (365/7 Wochen/Jahr)
TAGE_HERD_PRO_JAHR = (ANZ_KOCHVORGAENGE_PRO_WOCHE / TAGE_PRO_WOCHE) * TAGE_IM_JAHR
    
# Vereinfachte Berechnung: KW * Stunden * Kochvorgänge pro Jahr
verbrauch_herd_kwh = LEISTUNG_HERD_KW * STUNDEN_HERD_PRO_KOCHVORGANG * TAGE_HERD_PRO_JAHR
gesamtverbrauch_kwh += verbrauch_herd_kwh

# c) Telefon, Router, Rechner
LEISTUNG_IT_KW = 2.0
STUNDEN_IT_PRO_TAG = 4
    
verbrauch_it_kwh = LEISTUNG_IT_KW * STUNDEN_IT_PRO_TAG * TAGE_IM_JAHR
gesamtverbrauch_kwh += verbrauch_it_kwh

# d) Elektrische Heizung (supersparsam)
LEISTUNG_HEIZUNG_KW = 8.0
STUNDEN_HEIZUNG_PRO_TAG = 20
TAGE_HEIZUNG_PRO_JAHR = 170
    
verbrauch_heizung_kwh = LEISTUNG_HEIZUNG_KW * STUNDEN_HEIZUNG_PRO_TAG * TAGE_HEIZUNG_PRO_JAHR
gesamtverbrauch_kwh += verbrauch_heizung_kwh

# --- 3. Gesamtkosten berechnen ---

kosten_gesamt_euro = gesamtverbrauch_kwh * KOSTEN_PRO_KWH_EURO

# --- 4. Ergebnisse ausgeben ---
print("--- ENERGIEVERBRAUCH BERECHNUNG ---")
print(f"Preis pro kWh: {KOSTEN_PRO_KWH_EURO:.2f} €")
print("-" * 35)

print("Jährlicher Verbrauch pro Gerät:")
print(f"  Fernseher (TV):     {verbrauch_tv_kwh:9,.2f} kWh")
print(f"  Herd:               {verbrauch_herd_kwh:9,.2f} kWh")
print(f"  IT (Tel/Router/PC): {verbrauch_it_kwh:9,.2f} kWh")
print(f"  Elektrische Heizung:{verbrauch_heizung_kwh:9,.2f} kWh")
print("-" * 35)

print(f"GESAMTVERBRAUCH:    {gesamtverbrauch_kwh:9,.2f} kWh")
print(f"GESAMTKOSTEN (ohne MwSt.): {kosten_gesamt_euro:8,.2f} €")
print("---------------------------------")
