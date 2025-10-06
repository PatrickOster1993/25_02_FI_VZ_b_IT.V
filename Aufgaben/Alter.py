alter = int(input(""))

if alter < 12:
    print(" Du bist ein Kind.") 
elif alter < 18:
    print(" Du bist ein Jugendlicher.") 
elif alter < 65:
    print(" Du bist ein Erwachsener.") 
else:
    print(" Uff.")