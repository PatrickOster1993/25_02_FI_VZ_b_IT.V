Kwh= float(0.30)

# Fernseher

anzahl_TV =(3)
lestung_TV_Kwh = (1)
zeit_TV_perstunden =(3)
zeit_TV_perTage = (3)

# Herd 
lestung_Herd_Kwh = (1)
zeit_Herd_perWoche =(4)
zeit_Herd_perstunden =(2)

#Telfon und Router sowie Rechner
lestung_Telfon_Kwh = (2)
zeit_Telfon_perstunden = (4)
zeit_Telfon_perTage = (365)

#Heizung 
lestung_Heizung_Kwh = (8)
zeit_Heizung_perstunden = (20)
zeit_Heizung_perTage = (170)


verbrauch_TV = (anzahl_TV*lestung_TV_Kwh*zeit_TV_perstunden*zeit_TV_perTage)
verbrauch_Herd =(lestung_Herd_Kwh*zeit_Herd_perstunden*zeit_Herd_perWoche)
verbrauch_Telfon =(lestung_Telfon_Kwh *zeit_Telfon_perstunden*zeit_Telfon_perTage)
verbrauch_Heizung=(lestung_Heizung_Kwh*zeit_Heizung_perstunden*zeit_Heizung_perTage)
Gesamtverbrauch=(verbrauch_TV+verbrauch_Herd+verbrauch_Telfon+verbrauch_Heizung)

gesamtkosten =(Gesamtverbrauch*Kwh)

print ( "=== Energieverbrauch im Jahr ===")
print (F"Fernseher : {verbrauch_TV} kWh")
print (F"Herd : {verbrauch_Herd} kWh")
print (F"Telfon: {verbrauch_Telfon} kWh")
print (F"Heizung : {verbrauch_Heizung} kWh")
print("------------------------------")
print (F"Gesamtverbrauch : {Gesamtverbrauch} kWh im jahr")
print (F"gesamtkosten : {gesamtkosten} Euro im jahr")


