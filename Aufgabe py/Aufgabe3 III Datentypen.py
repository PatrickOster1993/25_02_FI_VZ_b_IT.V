netto=float(input(" price der geräte per netto : "))
wartesteuer =float(input("gGib den waeresteuer  : %  "))

Gesamtpreis=netto * (1+wartesteuer/100)

print(f" Der Gesamt preis inklusive wartesteuer : {Gesamtpreis:.2f} Euro")