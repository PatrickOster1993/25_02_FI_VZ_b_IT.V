# Aufgabe 5: Gewinnberechnung

einnahmen = [5000, 7000, 3000, 8000]

ausgaben = [4000, 6000, 2500, 6500]

gewinnzaeler = 0

for i,j,z in zip((einnahmen), (ausgaben), range(len(einnahmen))):
    print(f"\nDer Gewinn für den {z+1}. Monat beträgt: {i-j} €")
    if i-j > 1000:
        gewinnzaeler+=1
print(f"\nEs wurde {gewinnzaeler}. mal ein Gewinn über 1000 € erwirtschaftet.")
print()
