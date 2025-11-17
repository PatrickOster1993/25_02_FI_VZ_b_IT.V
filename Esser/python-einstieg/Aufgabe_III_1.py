#Zinsberechnung
print("         ---Zinsberechnung---            ")
eine_kwh = 0.30
wochen_jahr = 52
print("")
tv_tage = 365
tv_anzahl = 3
tv_verbrauch = 1
tv_std = 3
tv_gesamt = (tv_tage*tv_anzahl*tv_std*tv_verbrauch*eine_kwh)
print(f"Der Fernseher kostet pro Jahr {tv_gesamt:.2f} € an Strom")
print("")
herd_tage = 4
herd_Verbrauch = 2
herd_std = 2
herd_woche =(herd_tage*herd_std*herd_Verbrauch)
herd_gesamt =(herd_woche*wochen_jahr*eine_kwh)
print(f"Der Herd kostet pro Jahr {herd_gesamt:.2f} € an Strom")
print("")
routel_verbrauch = 2
routel_std = 4
routel_tage = 7
routel_woche = (routel_verbrauch*routel_std*routel_tage)
routel_gesamt = (routel_woche*wochen_jahr*eine_kwh)
print(f"Router und Telefon verbrauchen pro Jahr {routel_gesamt:.2f} € an  Strom")
print("")
heiz_verbrauch = 8
heiz_std = 20
heiz_tage = 170
heiz_gesamt = ((heiz_tage*heiz_verbrauch*heiz_std)*eine_kwh)
print(f"Die Heizung verbraucht pro Jahr {heiz_gesamt:.2f} € an  Strom")
print("")
Kosten_gesamt = (tv_gesamt+herd_gesamt+routel_gesamt+heiz_gesamt)
print(f"Die Gesamtstromkosten im Jahr belaufen sich auf {Kosten_gesamt:.2f} € im Jahr")
print("")
