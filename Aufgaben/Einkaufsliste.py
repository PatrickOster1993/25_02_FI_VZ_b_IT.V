Einkaufsliste=["Milch", "Brot", "Eier"]
print(Einkaufsliste[1])


Einkaufsliste.append("Butter")

Einkaufsliste[0]="Hafermilch"

print(Einkaufsliste)

if "Hafermilch" in Einkaufsliste:
    index = Einkaufsliste.index("Hafermilch")
    Einkaufsliste[index] = "Doch Milch"
    
print(Einkaufsliste)