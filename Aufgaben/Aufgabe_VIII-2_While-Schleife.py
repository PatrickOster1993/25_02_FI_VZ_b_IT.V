# Summiere die ersten 5 positiven ganzen Zahlen 

z = []
zahl = 1

while zahl <= 5:
    z.append(zahl)
    zahl+=1
summe = sum(z)
print(summe)
