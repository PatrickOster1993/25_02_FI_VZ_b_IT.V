# --- Testfall 1: Rabatt greift (Wert > 50.00) ---
warenkorb_wert = 65.50

print("--- Testfall 1 (Rabatt greift) ---")
print(f"Der Warenkorbwert beträgt: {warenkorb_wert:.2f} €")

if warenkorb_wert > 50.00:
    rabatt_faktor = 0.90  # 10% Rabatt
    neuer_preis = warenkorb_wert * rabatt_faktor
    print("Rabattaktion: 10% Rabatt!")
    print(f"Der neue Preis beträgt: {neuer_preis:.2f} €")
else:
    print("Leider kein Rabatt")

# --- Testfall 2: Kein Rabatt (Wert <= 50.00) ---
warenkorb_wert = 45.00

print("--- Testfall 2 (Kein Rabatt) ---")
print(f"Der Warenkorbwert beträgt: {warenkorb_wert:.2f} €")

if warenkorb_wert > 50.00:
    rabatt_faktor = 0.90
    neuer_preis = warenkorb_wert * rabatt_faktor
    print("Rabattaktion: 10% Rabatt!")
    print(f"Der neue Preis beträgt: {neuer_preis:.2f} €")
else:
    print("Leider kein Rabatt")