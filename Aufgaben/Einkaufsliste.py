Einkaufsliste=["Milch", "Brot", "Eier"]
print(Einkaufsliste[1])


Einkaufsliste.append("Butter")

Einkaufsliste[0]="Hafermilch"

print(Einkaufsliste)

#Extra mit if

if "Hafermilch" in Einkaufsliste: # Falls Hafermilch in Liste
    index = Einkaufsliste.index("Hafermilch") # index (Zahl) an welcher Hafermilch in Liste erkannt wird
    Einkaufsliste[index] = "Doch Milch" # Einkaufsliste an Indexzahl mit "Doch Milch" ersetzen
    
print(Einkaufsliste)