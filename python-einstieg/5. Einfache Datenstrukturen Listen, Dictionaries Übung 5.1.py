# Erstellen der Liste
einkaufsliste = ["Milch", "Brot", "Eier"]
print(f"Ursprüngliche Liste: {einkaufsliste}")

# Zweites Element ausgeben
print("\na) Zweites Element:")
print(einkaufsliste[1]) # Zugriff über Index

# "Butter" am Ende hinzufügen
einkaufsliste.append("Butter")
print("\nb) Nach Hinzufügen von 'Butter':")
print(einkaufsliste)

# Erstes Element ändern
einkaufsliste[0] = "Hafermilch"
print("\nc) Nach Ändern des ersten Elements:")
print(einkaufsliste)

# Liste ausgeben
print("\nd) Finale, geänderte Liste:")
print(einkaufsliste)