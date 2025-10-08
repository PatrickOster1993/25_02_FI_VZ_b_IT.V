#Währungsrechner
wechselkurs_eur_usd=1.17
betrag_in_eur=150
betrag_in_usd=betrag_in_eur*wechselkurs_eur_usd

print("========Währungsrechner========")
print(f"Betrag:                 {betrag_in_eur}€")
print(f"Wechselkurs EUR/USD:    {wechselkurs_eur_usd}")
print(f"{betrag_in_eur}€ in USD sind        {betrag_in_usd}$")
print("===============================")
