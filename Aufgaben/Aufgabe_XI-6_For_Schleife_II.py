# Rabattstufen

umsatz = [950, 1200, 800, 1600, 1800]

for i,j in zip(umsatz, range(len(umsatz))):
    print(f"\nKunde #{j}:")
    if i > 1500:
        print(f"Bekommt einen Rabatt von 20% und bezahlt jetzt noch: {i-i*0.2} €")
    elif i > 1000:
        print(f"Bekommt einen Rabatt von 10% und bezahlt jetzt noch: {i-i*0.1} €") 
    else:
        print(f"Bekommt keinen Rabatt und bezahlt deshalb: {i} €")
print()
