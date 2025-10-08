nettopreis=120

wartesteuer=7

gesamtpreis=nettopreis*(1+wartesteuer/100)

print(f"Gesamtpreis für den übertreuerten Druker beträgt mit Wartesteuer gnau {gesamtpreis: .2f} €")
