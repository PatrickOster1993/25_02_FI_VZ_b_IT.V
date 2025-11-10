produkte = [("Bleistift", 30), ("Heft", 60), ("Radiergummi", 20), ("Marker", 80)]

print("\n--- Lagerbestandsprüfung ---")
print("Bestand unter 50 (Nachbestellung):")

for produkt_info in produkte:
    name = produkt_info[0]
    bestand = produkt_info[1]
    
    if bestand < 50:
        print(f"  * {name}: {bestand} Stück - **NACHBESTELLEN**")