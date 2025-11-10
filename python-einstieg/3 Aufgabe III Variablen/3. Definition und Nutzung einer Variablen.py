# Aufgabe: Währungsumrechnung von Euro in US-Dollar

# 1. Recherchieren Sie den aktuellen Wechselkurs (angenommener fester Kurs: 1 Euro = 1.08 US-Dollar).

# 2. Erstellen Sie eine Variable wechselkurs_eur_usd und weisen Sie ihr diesen Wert zu.
wechselkurs_eur_usd = 1.08

# 3. Erstellen Sie eine Variable betrag_in_eur und weisen Sie ihr einen beliebigen Euro-Betrag zu.
betrag_in_eur = 150.00 

# 4. Erstellen Sie eine dritte Variable betrag_in_usd, die das Ergebnis der Umrechnung enthält.
# Formel: betrag_in_usd = betrag_in_eur * wechselkurs_eur_usd
betrag_in_usd = betrag_in_eur * wechselkurs_eur_usd

# 5. Geben Sie eine saubere Ausgabe, die alle drei Informationen enthält.
print("--- Währungsumrechnung ---")
print(f"Betrag in EUR: {betrag_in_eur:.2f}")
print(f"Aktueller Kurs (EUR/USD): {wechselkurs_eur_usd:.2f}")
print("-" * 30)
# Das Ergebnis der Umrechnung wird ausgegeben.
print(f"Ergibt in USD: {betrag_in_usd:.2f}")
print("--------------------------")