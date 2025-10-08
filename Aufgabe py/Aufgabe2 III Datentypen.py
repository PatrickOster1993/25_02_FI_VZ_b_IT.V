#Energieverbrauch
anzahl_gerate=int(input("Wie viele Gerete gibt es :  "))
leistung_kw= int (1)
price_kw=float(0.30)
leistung_pro_stundem=float(input("wissen Sie Wie viele der Geräte pro stunden  benutzen :  "))
leistung_pro_tag=float(input("wissen Sie Wie viele der Geräte pro Tag benutzen :  "))

verbrauch=leistung_kw*leistung_pro_stundem*leistung_pro_tag
storm_kosten =price_kw*verbrauch

print(f"verbrauch storm : {verbrauch} KWH")
print(f"storm kosten pro Jahr : {storm_kosten} Euro")

