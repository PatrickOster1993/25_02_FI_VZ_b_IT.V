print("------------Währungsumrechnung------------")
betrag_in_eur= float(input("Betrag in EUR: "))
wechselkurs_eur_usd= float(input("Was ist der aktuelle Wechselkurs (EUR/USD) ? "))
betrag_in_usd= betrag_in_eur*wechselkurs_eur_usd

print(f"Ergibt in USD: {betrag_in_usd} $")
