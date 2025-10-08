# Benutzerprofil

benutzerprofil = {
    "vorname":"Tom",
    "nachname":"Schmidt",
    "alter":"30",
    "stadt":"Berlin"
}

print(benutzerprofil)

nachname = benutzerprofil["nachname"]
print(nachname)

benutzerprofil["alter"] = 35
print(benutzerprofil) 

benutzerprofil["email"] = "Tom_Schmidt@gmx.de"
print(benutzerprofil)