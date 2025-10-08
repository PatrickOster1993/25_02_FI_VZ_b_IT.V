# Übung 4.1: Rabattaktion 

print("")
warenkorb_wert = float(input("Bitte geben sie den Wert in ihrem Warenkorb in Euro an: "))

if warenkorb_wert > 50.00:
    print(f"Sie erhalten einen Rabatt von 10% und bezahlen jetzt nur noch: {warenkorb_wert-warenkorb_wert*0.1:.2f} Euro")
else:
    print(f"Sie erhalten leider keinen Rabatt und zahlen somit: {warenkorb_wert} Euro")

print("")
