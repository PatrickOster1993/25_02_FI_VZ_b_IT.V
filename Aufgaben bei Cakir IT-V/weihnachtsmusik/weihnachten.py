import time
import random
import os
from pathlib import Path

try:
    import pygame
    PYGAME_VERFUEGBAR = True
except ImportError:
    PYGAME_VERFUEGBAR = False
    print("⚠️  pygame nicht gefunden. Installiere es mit: pip install pygame")
    print("⚠️  Programm läuft ohne Musik weiter...\n")


class WeihnachtsShow:
    def __init__(self):
        self.farben = ['🔴', '🟢', '🟡', '🔵', '⚪', '🟠']
        self.laeuft = False
        self.lichtmuster = 0
        
        # Musik-Setup
        self.musik_ordner = Path("weihnachtsmusik")
        self.musik_dateien = {
            '1': 'jingle_bells.mp3',
            '2': 'last_christmas.mp3',
            '3': 'all_i_want.mp3',
            '4': 'white_christmas.mp3',
            '5': 'silent_night.mp3'
        }
        self.musik_namen = {
            '1': 'Jingle Bells',
            '2': 'Last Christmas',
            '3': 'All I Want for Christmas',
            '4': 'White Christmas',
            '5': 'Silent Night'
        }
        
        if PYGAME_VERFUEGBAR:
            pygame.mixer.init()
            self.pruefe_musik_dateien()
    
    def pruefe_musik_dateien(self):
        """Prüft welche Musik-Dateien vorhanden sind"""
        if not self.musik_ordner.exists():
            print(f"📁 Erstelle Ordner: {self.musik_ordner}")
            self.musik_ordner.mkdir(exist_ok=True)
            print("ℹ️  Lege deine MP3-Dateien in diesen Ordner!\n")
        
        print("🎵 Verfügbare Musik-Dateien:")
        for key, datei in self.musik_dateien.items():
            pfad = self.musik_ordner / datei
            if pfad.exists():
                print(f"   ✅ {self.musik_namen[key]}")
            else:
                print(f"   ❌ {self.musik_namen[key]} (fehlt: {datei})")
        print()
    
    def clear_screen(self):
        """Bildschirm leeren"""
        print("\n" * 50)
    
    def zeige_banner(self):
        """Weihnachtsbanner anzeigen"""
        print("=" * 60)
        print("🎄" * 15)
        print("     WEIHNACHTSBELEUCHTUNG & MUSIK STEUERUNG")
        print("🎄" * 15)
        print("=" * 60)
        print()
    
    def lichteffekt_funkeln(self):
        """Funkelnder Lichteffekt"""
        lichter = [random.choice(self.farben) for _ in range(20)]
        print("✨ FUNKELN: " + " ".join(lichter))
    
    def lichteffekt_welle(self):
        """Wellenförmiger Lichteffekt"""
        print("🌊 WELLE:   ", end="")
        for i in range(20):
            farbe = self.farben[i % len(self.farben)]
            print(farbe, end=" ")
        print()
    
    def lichteffekt_blinken(self):
        """Blinkendes Lichtmuster"""
        if self.lichtmuster % 2 == 0:
            print("💡 BLINKEN: " + "🔴 " * 10)
        else:
            print("💡 BLINKEN: " + "🟢 " * 10)
        self.lichtmuster += 1
    
    def lichteffekt_regenbogen(self):
        """Regenbogen-Effekt"""
        print("🌈 RAINBOW: ", end="")
        for farbe in self.farben * 3:
            print(farbe, end=" ")
        print()
    
    def musik_abspielen(self, song_wahl):
        """Spielt die ausgewählte Musik ab"""
        if not PYGAME_VERFUEGBAR:
            print(f"🎵 [Simuliert]: {self.musik_namen[song_wahl]}")
            return False
        
        datei = self.musik_dateien[song_wahl]
        pfad = self.musik_ordner / datei
        
        if not pfad.exists():
            print(f"⚠️  Datei nicht gefunden: {datei}")
            print(f"🎵 [Simuliert]: {self.musik_namen[song_wahl]}")
            return False
        
        try:
            pygame.mixer.music.load(str(pfad))
            pygame.mixer.music.play(-1)  # -1 = Endlos-Schleife
            print(f"🎵 ♪♫ Spielt jetzt: {self.musik_namen[song_wahl]} ♫♪")
            return True
        except Exception as e:
            print(f"⚠️  Fehler beim Abspielen: {e}")
            return False
    
    def musik_stoppen(self):
        """Stoppt die Musik"""
        if PYGAME_VERFUEGBAR:
            pygame.mixer.music.stop()
    
    def lautstaerke_anpassen(self, lautstaerke):
        """Passt die Lautstärke an (0.0 - 1.0)"""
        if PYGAME_VERFUEGBAR:
            pygame.mixer.music.set_volume(lautstaerke)
            print(f"🔊 Lautstärke: {int(lautstaerke * 100)}%")
    
    def haupt_show(self, musik_wahl, dauer=10, lautstaerke=0.7):
        """Hauptshow mit Lichtern und Musik"""
        self.laeuft = True
        self.clear_screen()
        self.zeige_banner()
        
        # Lautstärke einstellen
        self.lautstaerke_anpassen(lautstaerke)
        
        # Musik starten
        musik_laeuft = self.musik_abspielen(musik_wahl)
        print(f"⏱️  Show läuft für {dauer} Sekunden...")
        print("⏸️  Drücke Ctrl+C zum vorzeitigen Stoppen\n")
        
        start_zeit = time.time()
        effekt_nummer = 0
        
        try:
            while time.time() - start_zeit < dauer and self.laeuft:
                # Wechsle zwischen verschiedenen Lichteffekten
                if effekt_nummer % 4 == 0:
                    self.lichteffekt_funkeln()
                elif effekt_nummer % 4 == 1:
                    self.lichteffekt_welle()
                elif effekt_nummer % 4 == 2:
                    self.lichteffekt_blinken()
                else:
                    self.lichteffekt_regenbogen()
                
                effekt_nummer += 1
                time.sleep(0.5)
        
        except KeyboardInterrupt:
            print("\n\n⏹️  Show manuell gestoppt!")
        
        finally:
            self.musik_stoppen()
            print("\n🎄 Show beendet! Frohe Weihnachten! 🎄\n")
    
    def zeige_menu(self):
        """Interaktives Menü"""
        lautstaerke = 0.7  # Standard-Lautstärke
        
        while True:
            self.clear_screen()
            self.zeige_banner()
            print("MENÜ:")
            print("1️⃣  Jingle Bells 🔔")
            print("2️⃣  Last Christmas 🎁")
            print("3️⃣  All I Want for Christmas ⭐")
            print("4️⃣  White Christmas ❄️")
            print("5️⃣  Silent Night 🕯️")
            print()
            print("⚙️  Einstellungen:")
            print(f"L - Lautstärke ändern (aktuell: {int(lautstaerke * 100)}%)")
            print("0️⃣  Beenden")
            print()
            
            wahl = input("Deine Wahl: ").strip().lower()
            
            if wahl == '0':
                print("\n🎅 Auf Wiedersehen und frohe Weihnachten! 🎅\n")
                break
            
            elif wahl == 'l':
                try:
                    neue_lautstaerke = int(input("Lautstärke (0-100): "))
                    if 0 <= neue_lautstaerke <= 100:
                        lautstaerke = neue_lautstaerke / 100
                        print(f"✅ Lautstärke auf {neue_lautstaerke}% gesetzt")
                    else:
                        print("⚠️  Bitte Wert zwischen 0 und 100 eingeben!")
                    time.sleep(1.5)
                except ValueError:
                    print("⚠️  Ungültige Eingabe!")
                    time.sleep(1.5)
            
            elif wahl in ['1', '2', '3', '4', '5']:
                try:
                    dauer = int(input("Wie lange soll die Show laufen? (Sekunden): "))
                    if dauer > 0:
                        self.haupt_show(wahl, dauer, lautstaerke)
                        input("\n🎄 Drücke ENTER um zurück zum Menü zu kommen...")
                    else:
                        print("⚠️  Bitte eine positive Zahl eingeben!")
                        time.sleep(2)
                except ValueError:
                    print("⚠️  Bitte eine gültige Zahl eingeben!")
                    time.sleep(2)
            else:
                print("⚠️  Ungültige Auswahl!")
                time.sleep(2)


def main():
    """Hauptprogramm starten"""
    show = WeihnachtsShow()
    
    print("\n🎄 Willkommen zur Weihnachtsshow! 🎄\n")
    
    if not PYGAME_VERFUEGBAR:
        print("💡 Tipp: Installiere pygame für echte Musik:")
        print("   pip install pygame\n")
    
    # Frage ob Schnellstart oder Menü
    schnellstart = input("Schnellstart mit Jingle Bells für 20 Sek? (j/n): ").lower()
    
    if schnellstart == 'j':
        show.haupt_show('1', 20)
        input("\nDrücke ENTER für das Hauptmenü...")
    
    # Zeige Hauptmenü
    show.zeige_menu()


if __name__ == "__main__":
    main()