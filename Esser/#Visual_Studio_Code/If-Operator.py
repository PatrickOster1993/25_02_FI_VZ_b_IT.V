#####################################   IF
alter = 13

if alter >= 13 and alter <=18:
    print("Ich stehe am Anfang meiner Pubertät")

alter = 26

if alter <30 or alter >35:
    print("Ich bekomme immer einen Kater nach einigen Flaschen Bier")

print("")
#####################################   ELIF
if alter < 12:
    print(" Du bist ein Kind.")
elif alter < 8:
    print(" Du bist ein Jugendlicher.")
elif alter < 5:
    print(" Du bist ein Erwachsener.")
else:
    print(" Uff.")
print("")
#####################################  If Or
land = "Deutschland"
alter = 26

if(land=="Deutschland" and alter>=26) or (land!="Deutschland" and alter <=10):
    print("Jetz können wir alle Alohol trinken")
