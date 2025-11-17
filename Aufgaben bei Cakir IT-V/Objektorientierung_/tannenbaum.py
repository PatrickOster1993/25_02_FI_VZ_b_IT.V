import time
import random
import os
from colorama import colorama_text, Fore, Back, Style, init

# Colorama initialisieren (für Windows-Kompatibilität)
init(autoreset=True)



class Weihnachtsbaum:
    def __init__(self):
        self.lichter_an = True
        self.aktuelle_farbe = Fore.RED
        self.lichtmodus = "regenbogen"
        self.geschwindigkeit = 0.5
        self.laeuft = False
        
        # Verfügbare Farben
        self.farben = {
            '1': (Fore.RED, "Rot 🔴"),
            '2': (Fore.GREEN, "Grün 🟢"),
            '3': (Fore.BLUE, "Blau 🔵"),
            '4': (Fore.YELLOW, "Gelb 🟡"),
            '5': (Fore.MAGENTA, "Lila 🟣"),
            '6': (Fore.WHITE, "Weiß ⚪"),
            '7': (Fore.CYAN, "Cyan 🔷")
        }
        
        self.farben_liste = [Fore.RED, Fore.GREEN, Fore.BLUE, 
                             Fore.YELLOW, Fore.MAGENTA, Fore.WHITE, Fore.CYAN]
        
        self.baum_struktur = [
            "        ⭐",
            "        /\\",
            "       /  \\",
            "      / ●  \\",
            "     /  ●  ●\\",
            "    /●  ●  ● \\",
            "   /  ●  ●  ● \\",
            "  / ●  ●  ●  ● \\",
            " /  ●  ●  ●  ●  \\",
            "/  ●  ●  ●  ●  ● \\",
            "      ||||",
            "      ||||"
        ]
    
    def clear_screen(self):
        """Bildschirm leeren"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def zeichne_baum(self, licht_farben=None):
        """Zeichnet den Weihnachtsbaum mit Beleuchtung"""
        self.clear_screen()
        
        print("\n" + "="*50)
        print("🎄 WEIHNACHTSBAUM BELEUCHTUNG 🎄".center(50))
        print("="*50 + "\n")
        
        for i, zeile in enumerate(self.baum_struktur):
            if i == 0:  # Stern
                print(Fore.YELLOW + Style.BRIGHT + zeile)
            elif i >= len(self.baum_struktur) - 2:  # Stamm
                print(Fore.YELLOW + zeile)
            else:
                # Lichter einfärben
                neue_zeile = zeile
                if self.lichter_an and '●' in zeile:
                    if licht_farben:
                        # Verwende spezifische Farben für jedes Licht
                        teile = zeile.split('●')
                        neue_zeile = teile[0]
                        for j, teil in enumerate(teile[1:]):
                            farbe = licht_farben[i % len(licht_farben)]
                            neue_zeile += farbe + Style.BRIGHT + '●' + Style.RESET_ALL + teil
                    else:
                        # Einzelfarbe
                        neue_zeile = zeile.replace('●', 
                            self.aktuelle_farbe + Style.BRIGHT + '●' + Style.RESET_ALL)
                else:
                    # Lichter aus (grau)
                    neue_zeile = zeile.replace('●', Fore.BLACK + '●' + Style.RESET_ALL)
                
                # Baum grün färben
                neue_zeile = neue_zeile.replace('/', Fore.GREEN + '/')
                neue_zeile = neue_zeile.replace('\\', '\\' + Style.RESET_ALL)
                print(neue_zeile)
        
        print()
    
    def zeige_status(self):
        """Zeigt den aktuellen Status an"""
        status = "AN" if self.lichter_an else "AUS"
        farbe = Fore.GREEN if self.lichter_an else Fore.RED
        
        print(f"\n📊 Status: {farbe}{status}{Style.RESET_ALL}")
        print(f"🎨 Modus: {self.lichtmodus.upper()}")
        print(f"⚡ Geschwindigkeit: {self.geschwindigkeit}s")
        print()
    
    def modus_blinken(self, dauer=10):
        """Blinkmodus"""
        self.lichtmodus = "blinken"
        self.laeuft = True
        start = time.time()
        
        while time.time() - start < dauer and self.laeuft:
            self.lichter_an = not self.lichter_an
            self.zeichne_baum()
            self.zeige_status()
            print("⏸️  Drücke Ctrl+C zum Stoppen...")
            time.sleep(self.geschwindigkeit)
    
    def modus_regenbogen(self, dauer=10):
        """Regenbogen-Modus"""
        self.lichtmodus = "regenbogen"
        self.laeuft = True
        self.lichter_an = True
        start = time.time()
        farb_index = 0
        
        while time.time() - start < dauer and self.laeuft:
            # Rotiere durch alle Farben
            aktuelle_farben = []
            for i in range(10):
                aktuelle_farben.append(
                    self.farben_liste[(farb_index + i) % len(self.farben_liste)]
                )
            
            self.zeichne_baum(aktuelle_farben)
            self.zeige_status()
            print("⏸️  Drücke Ctrl+C zum Stoppen...")
            
            farb_index = (farb_index + 1) % len(self.farben_liste)
            time.sleep(self.geschwindigkeit)
    
    def modus_welle(self, dauer=10):
        """Wellen-Modus"""
        self.lichtmodus = "welle"
        self.laeuft = True
        self.lichter_an = True
        start = time.time()
        position = 0
        
        while time.time() - start < dauer and self.laeuft:
            aktuelle_farben = []
            for i in range(10):
                # Nur an bestimmten Positionen leuchten
                if abs(i - position % 10) < 2:
                    aktuelle_farben.append(self.farben_liste[i % len(self.farben_liste)])
                else:
                    aktuelle_farben.append(Fore.BLACK)
            
            self.zeichne_baum(aktuelle_farben)
            self.zeige_status()
            print("⏸️  Drücke Ctrl+C zum Stoppen...")
            
            position += 1
            time.sleep(self.geschwindigkeit / 2)
    
    def modus_zufall(self, dauer=10):
        """Zufalls-Modus"""
        self.lichtmodus = "zufällig"
        self.laeuft = True
        self.lichter_an = True
        start = time.time()
        
        while time.time() - start < dauer and self.laeuft:
            # Zufällige Farben für jedes Licht
            aktuelle_farben = [random.choice(self.farben_liste) for _ in range(10)]
            
            self.zeichne_baum(aktuelle_farben)
            self.zeige_status()
            print("⏸️  Drücke Ctrl+C zum Stoppen...")
            
            time.sleep(self.geschwindigkeit)
    
    def zeige_menu(self):
        """Hauptmenü"""
        while True:
            self.zeichne_baum()
            self.zeige_status()
            
            print("=" * 50)
            print("STEUERUNG:")
            print("=" * 50)
            print()
            print("💡 Hauptsteuerung:")
            print("  1 - Alle Lichter AN")
            print("  2 - Alle Lichter AUS")
            print()
            print("🎨 Lichtmodus (mit Dauer):")
            print("  3 - Blinken")
            print("  4 - Regenbogen")
            print("  5 - Welle")
            print("  6 - Zufällig")
            print()
            print("🌈 Farbe wählen:")
            print("  7 - Rot 🔴")
            print("  8 - Grün 🟢")
            print("  9 - Blau 🔵")
            print("  A - Gelb 🟡")
            print("  B - Lila 🟣")
            print("  C - Weiß ⚪")
            print()
            print("⚙️  Einstellungen:")
            print("  S - Geschwindigkeit ändern")
            print()
            print("  0 - Beenden")
            print()
            
            wahl = input("Deine Wahl: ").strip().upper()
            
            try:
                if wahl == '0':
                    self.clear_screen()
                    print("\n🎅 Frohe Weihnachten! 🎄\n")
                    break
                
                elif wahl == '1':
                    self.lichter_an = True
                    self.lichtmodus = "statisch"
                
                elif wahl == '2':
                    self.lichter_an = False
                    self.lichtmodus = "aus"
                
                elif wahl in ['3', '4', '5', '6']:
                    dauer = int(input("Wie lange soll der Modus laufen? (Sekunden): "))
                    if dauer > 0:
                        try:
                            if wahl == '3':
                                self.modus_blinken(dauer)
                            elif wahl == '4':
                                self.modus_regenbogen(dauer)
                            elif wahl == '5':
                                self.modus_welle(dauer)
                            elif wahl == '6':
                                self.modus_zufall(dauer)
                        except KeyboardInterrupt:
                            print("\n\n⏹️  Modus gestoppt!")
                            time.sleep(1)
                
                elif wahl == '7':
                    self.aktuelle_farbe = Fore.RED
                    self.lichter_an = True
                    self.lichtmodus = "rot"
                
                elif wahl == '8':
                    self.aktuelle_farbe = Fore.GREEN
                    self.lichter_an = True
                    self.lichtmodus = "grün"
                
                elif wahl == '9':
                    self.aktuelle_farbe = Fore.BLUE
                    self.lichter_an = True
                    self.lichtmodus = "blau"
                
                elif wahl == 'A':
                    self.aktuelle_farbe = Fore.YELLOW
                    self.lichter_an = True
                    self.lichtmodus = "gelb"
                
                elif wahl == 'B':
                    self.aktuelle_farbe = Fore.MAGENTA
                    self.lichter_an = True
                    self.lichtmodus = "lila"
                
                elif wahl == 'C':
                    self.aktuelle_farbe = Fore.WHITE
                    self.lichter_an = True
                    self.lichtmodus = "weiß"
                
                elif wahl == 'S':
                    neue_speed = float(input("Neue Geschwindigkeit (0.1 - 2.0 Sekunden): "))
                    if 0.1 <= neue_speed <= 2.0:
                        self.geschwindigkeit = neue_speed
                        print(f"✅ Geschwindigkeit auf {neue_speed}s gesetzt!")
                        time.sleep(1)
                    else:
                        print("⚠️  Bitte Wert zwischen 0.1 und 2.0 eingeben!")
                        time.sleep(2)
                
                else:
                    print("⚠️  Ungültige Auswahl!")
                    time.sleep(1)
            
            except ValueError:
                print("⚠️  Ungültige Eingabe!")
                time.sleep(2)
            except KeyboardInterrupt:
                continue


def main():
    """Hauptprogramm"""
    print("\n" + "="*50)
    print("🎄 WEIHNACHTSBAUM BELEUCHTUNG 🎄".center(50))
    print("="*50)
    print()
    print("WICHTIG: Installiere zuerst colorama für bunte Farben:")
    print("  pip install colorama")
    print()
    input("Drücke ENTER zum Starten...")
    
    baum = Weihnachtsbaum()
    baum.zeige_menu()


if __name__ == "__main__":
    main()