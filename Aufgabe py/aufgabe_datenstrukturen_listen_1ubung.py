#5. Einfache Datenstrukturen: Listen, Dictionaries
einkaufsliste=["Milch","Brot","Eier"]
zweite_Element=einkaufsliste[1]
print (zweite_Element) #Geben Sie das zweite Element der Liste aus

#Fügen Sie "Butter" am Ende der Liste hinzu
einkaufsliste.append("Butter")
print (einkaufsliste)

#Ändern Sie das erste Element von "Milch" zu "Hafermilch
einkaufsliste[0]="Hafermilch"
print (einkaufsliste)
#d) Geben Sie die finale, geänderte Liste aus
print (einkaufsliste)


#Dictionary
benutzerprofil={"vorname":"Ehssan",
                "nachname":"Aldaoode",
                "Alter":50, 
                "stad": "xanten",
                }
benutzerprofil_nachname=benutzerprofil["nachname"]
print (benutzerprofil_nachname)

#b) Ändern Sie das Alter des Benutzers.
benutzerprofil["Alter"]=60
benutzerprofil_Alter=benutzerprofil["Alter"]
print (benutzerprofil_Alter)

#c) Fügen Sie ein neues Schlüssel-Wert-Paar hinzu: email mit einer fiktiven E-Mail-Adresse
benutzerprofil["email"]="ehssanaldaoode@gmail.com"
print (benutzerprofil)
