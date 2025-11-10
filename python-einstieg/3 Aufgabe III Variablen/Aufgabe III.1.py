# Erstellen Sie eine neue Anwendung namens "Zinsberechnung".

# Definiere die Variablen, um die Zinsen für ein Jahr auszurechnen.
    
# Kapital 
kapital = 1000.00  # Beispielwert: 1000 Euro

# Zinssatz 
zinssatz = 0.05    # Beispielwert: 5%

# Zeit 
zeit_in_jahren = 1

# Formel für einfache Zinsen= Kapital * Zinssatz * Zeit
zinsen = kapital * zinssatz * zeit_in_jahren

print("--- Zinsberechnung ---")
print(f"Kapital:         {kapital:,.2f} €")
print(f"Zinssatz:        {zinssatz * 100:.2f} %")
print(f"Zeit:            {zeit_in_jahren} Jahr(e)")
print("-" * 20)
print(f"Berechnete Zinsen:   {zinsen:,.2f} €")
print("----------------------")
