# Erstellen des Dictionarys
benutzerprofil = {
    "vorname": "Max",
    "nachname": "Mustermann",
    "alter": 28,
    "stadt": "Musterstadt"
}
print(f"Ursprüngliches Profil: {benutzerprofil}")

# Nachnamen ausgeben
print("Nachname:")
print(benutzerprofil["nachname"])

# Das Alter ändern
benutzerprofil["alter"] = 29
print("Nach Änderung des Alters:")
print(benutzerprofil["alter"])

# Neu hinzufügen: email
benutzerprofil["email"] = "max.mustermann@mail.de"
print("Nach Hinzufügen der E-Mail:")
print(benutzerprofil)

# geänderte Liste ausgeben
print("Finale, geänderte Liste:")
print(benutzerprofil)