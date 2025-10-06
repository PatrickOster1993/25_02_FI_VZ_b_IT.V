# Preis pro kWh
preis_kwh = 0.30  # Euro

# Fernseher
fernseher_leistung = 1    # kWh
fernseher_anzahl = 3
fernseher_stunden = 3
fernseher_tage = 365

verbrauch_fernseher = fernseher_leistung * fernseher_stunden * fernseher_tage * fernseher_anzahl

# Herd
herd_leistung = 2  # kWh
herd_stunden = 2
herd_tage = 4 * 52  # 4 mal die Woche * 52 Wochen
verbrauch_herd = herd_leistung * herd_stunden * herd_tage

# Telefon + Router + Rechner
geraete_leistung = 2
geraete_stunden = 4
geraete_tage = 365
verbrauch_geraete = geraete_leistung * geraete_stunden * geraete_tage

# Elektrische Heizung
heizung_leistung = 8
heizung_stunden = 20
heizung_tage = 170
verbrauch_heizung = heizung_leistung * heizung_stunden * heizung_tage

# Gesamtverbrauch
gesamtverbrauch = verbrauch_fernseher + verbrauch_herd + verbrauch_geraete + verbrauch_heizung
kosten = gesamtverbrauch * preis_kwh

print(f"Gesamtverbrauch im Jahr: {gesamtverbrauch} kWh")
print(f"Jahreskosten bei {preis_kwh} €/kWh: {kosten:.2f} Euro")