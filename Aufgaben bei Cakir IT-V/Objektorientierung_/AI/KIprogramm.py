"""
KI-ASSISTENT MIT VERSCHIEDENEN FUNKTIONEN
==========================================
Ein intelligenter Assistent mit:
- Textanalyse & Sentiment-Analyse
- Frage-Antwort System
- Textzusammenfassung
- Spracherkennung (optional)
- Lernfähigkeit
- GUI-Interface

INSTALLATION:
pip install tkinter nltk textblob scikit-learn numpy
python -m textblob.download_corpora
python -m nltk.downloader punkt vader_lexicon stopwords

OPTIONAL (für Sprache):
pip install speechrecognition pyttsx3 pyaudio
"""

import tkinter as tk
from tkinter import scrolledtext, messagebox, ttk
import json
import os
import datetime
import random
from collections import Counter
import re

try:
    from textblob import TextBlob
    from textblob_de import TextBlobDE
    TEXTBLOB_VERFUEGBAR = True
except ImportError:
    TEXTBLOB_VERFUEGBAR = False
    print("⚠️  TextBlob nicht installiert. Installiere mit: pip install textblob textblob-de")

try:
    import nltk
    from nltk.tokenize import word_tokenize, sent_tokenize
    from nltk.corpus import stopwords
    NLTK_VERFUEGBAR = True
except ImportError:
    NLTK_VERFUEGBAR = False
    print("⚠️  NLTK nicht installiert. Installiere mit: pip install nltk")

try:
    import pyttsx3
    SPRACHE_VERFUEGBAR = True
except ImportError:
    SPRACHE_VERFUEGBAR = False


class KIAssistent:
    def __init__(self):
        self.wissensbasis = self.lade_wissensbasis()
        self.gespraechsverlauf = []
        self.benutzername = "Benutzer"
        
        # Vortrainierte Antworten
        self.antworten = {
            "hallo": ["Hallo! Wie kann ich dir helfen?", "Hi! Schön dich zu sehen!", "Grüß dich! Was kann ich für dich tun?"],
            "wie geht es": ["Mir geht es gut, danke! Und dir?", "Prima! Wie kann ich dir helfen?", "Sehr gut! Was brauchst du?"],
            "danke": ["Gerne! 😊", "Kein Problem!", "Immer wieder gern!"],
            "tschüss": ["Auf Wiedersehen! 👋", "Bis bald!", "Tschüss! War schön mit dir zu plaudern!"],
            "wetter": ["Für Wetterinformationen benötige ich eine API-Anbindung. Schau mal bei wetter.com!", 
                      "Das Wetter kann ich leider nicht abrufen, aber ich kann dir andere Dinge erklären!"],
            "hilfe": ["Ich kann:\n- Fragen beantworten\n- Texte analysieren\n- Stimmungen erkennen\n- Informationen speichern\n- Mit dir plaudern!",
                     "Probier mal: 'Analysiere: [dein Text]' oder 'Was ist [Begriff]?'"],
        }
        
        # Sprachausgabe initialisieren
        if SPRACHE_VERFUEGBAR:
            try:
                self.tts_engine = pyttsx3.init()
                self.tts_engine.setProperty('rate', 150)
                self.tts_verfuegbar = True
            except:
                self.tts_verfuegbar = False
        else:
            self.tts_verfuegbar = False
    
    def lade_wissensbasis(self):
        """Lädt gespeicherte Wissensbasis"""
        datei = "ki_wissen.json"
        if os.path.exists(datei):
            try:
                with open(datei, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return {}
        return {}
    
    def speichere_wissensbasis(self):
        """Speichert Wissensbasis"""
        datei = "ki_wissen.json"
        try:
            with open(datei, 'w', encoding='utf-8') as f:
                json.dump(self.wissensbasis, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Fehler beim Speichern: {e}")
    
    def lerne(self, schluessel, wert):
        """Lernt neue Information"""
        schluessel = schluessel.lower().strip()
        self.wissensbasis[schluessel] = {
            "wert": wert,
            "gelernt_am": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.speichere_wissensbasis()
        return f"✅ Verstanden! Ich habe gelernt: {schluessel} = {wert}"
    
    def erinnere(self, schluessel):
        """Ruft Information ab"""
        schluessel = schluessel.lower().strip()
        if schluessel in self.wissensbasis:
            info = self.wissensbasis[schluessel]
            return f"💡 {schluessel}: {info['wert']}\n(Gelernt am: {info['gelernt_am']})"
        return f"❌ Ich habe keine Information über '{schluessel}'"
    
    def sentiment_analyse(self, text):
        """Analysiert die Stimmung eines Textes"""
        if not TEXTBLOB_VERFUEGBAR:
            return "⚠️ TextBlob nicht installiert. Sentiment-Analyse nicht verfügbar."
        
        try:
            # Versuche deutsche Analyse
            blob = TextBlobDE(text)
            polaritaet = blob.sentiment.polarity
            
            if polaritaet > 0.3:
                stimmung = "😊 POSITIV"
                emoji = "👍"
            elif polaritaet < -0.3:
                stimmung = "😟 NEGATIV"
                emoji = "👎"
            else:
                stimmung = "😐 NEUTRAL"
                emoji = "🤷"
            
            return f"""
📊 SENTIMENT-ANALYSE:

Stimmung: {stimmung} {emoji}
Polarität: {polaritaet:.2f} (-1 bis +1)

Interpretation:
{self.interpretiere_sentiment(polaritaet)}
"""
        except Exception as e:
            return f"Fehler bei der Analyse: {e}"
    
    def interpretiere_sentiment(self, polaritaet):
        """Interpretiert Polaritätswert"""
        if polaritaet > 0.5:
            return "Sehr positive Stimmung! Der Text drückt Freude oder Begeisterung aus."
        elif polaritaet > 0.1:
            return "Leicht positive Stimmung. Der Text ist überwiegend positiv."
        elif polaritaet > -0.1:
            return "Neutrale Stimmung. Der Text ist sachlich oder neutral formuliert."
        elif polaritaet > -0.5:
            return "Leicht negative Stimmung. Der Text enthält Kritik oder Unzufriedenheit."
        else:
            return "Sehr negative Stimmung. Der Text drückt Ärger oder Enttäuschung aus."
    
    def text_statistik(self, text):
        """Erstellt Textstatistik"""
        woerter = text.split()
        saetze = text.split('.')
        zeichen = len(text)
        
        # Wortlängen
        wortlaengen = [len(wort) for wort in woerter]
        durchschnitt = sum(wortlaengen) / len(wortlaengen) if wortlaengen else 0
        
        # Häufigste Wörter
        wort_counter = Counter([w.lower() for w in woerter if len(w) > 3])
        haeufigste = wort_counter.most_common(5)
        
        statistik = f"""
📈 TEXT-STATISTIK:

Zeichen: {zeichen}
Wörter: {len(woerter)}
Sätze: {len(saetze)}
Durchschn. Wortlänge: {durchschnitt:.1f} Zeichen

Top 5 häufigste Wörter:
"""
        for wort, anzahl in haeufigste:
            statistik += f"  • {wort}: {anzahl}x\n"
        
        return statistik
    
    def verarbeite_anfrage(self, eingabe):
        """Hauptlogik zur Verarbeitung der Anfrage"""
        eingabe_lower = eingabe.lower().strip()
        
        # Leer-Check
        if not eingabe_lower:
            return "Bitte gib etwas ein! 🤔"
        
        # Gesprächsverlauf speichern
        self.gespraechsverlauf.append({
            "zeit": datetime.datetime.now().strftime("%H:%M:%S"),
            "eingabe": eingabe
        })
        
        # Kommando-Verarbeitung
        # 1. Lernen
        if eingabe_lower.startswith("lerne:") or eingabe_lower.startswith("merke:"):
            teile = eingabe.split(":", 1)[1].strip().split("=", 1)
            if len(teile) == 2:
                return self.lerne(teile[0].strip(), teile[1].strip())
            return "❌ Format: lerne: Begriff = Erklärung"
        
        # 2. Erinnern
        if eingabe_lower.startswith("was ist") or eingabe_lower.startswith("was sind"):
            begriff = re.sub(r'^was ist |^was sind ', '', eingabe_lower).strip('?').strip()
            return self.erinnere(begriff)
        
        # 3. Sentiment-Analyse
        if eingabe_lower.startswith("analysiere:") or eingabe_lower.startswith("sentiment:"):
            text = eingabe.split(":", 1)[1].strip()
            return self.sentiment_analyse(text)
        
        # 4. Text-Statistik
        if eingabe_lower.startswith("statistik:"):
            text = eingabe.split(":", 1)[1].strip()
            return self.text_statistik(text)
        
        # 5. Wissensbasis anzeigen
        if eingabe_lower in ["was weißt du", "was kannst du", "wissen"]:
            if self.wissensbasis:
                antwort = "🧠 MEINE WISSENSBASIS:\n\n"
                for begriff, info in list(self.wissensbasis.items())[:10]:
                    antwort += f"• {begriff}: {info['wert']}\n"
                if len(self.wissensbasis) > 10:
                    antwort += f"\n... und {len(self.wissensbasis) - 10} weitere Einträge"
                return antwort
            return "Ich habe noch nichts gelernt. Bringe mir etwas bei mit: lerne: Begriff = Erklärung"
        
        # 6. Vorprogrammierte Antworten
        for schluessel, antworten in self.antworten.items():
            if schluessel in eingabe_lower:
                return random.choice(antworten)
        
        # 7. Mathematik
        if any(op in eingabe for op in ['+', '-', '*', '/', '=']):
            try:
                # Extrahiere mathematischen Ausdruck
                ausdruck = re.search(r'[\d\s+\-*/().]+', eingabe)
                if ausdruck:
                    ergebnis = eval(ausdruck.group())
                    return f"🔢 Das Ergebnis ist: {ergebnis}"
            except:
                pass
        
        # 8. Standard-Antwort mit KI-Logik
        return self.intelligente_antwort(eingabe)
    
    def intelligente_antwort(self, eingabe):
        """Generiert intelligente Antwort basierend auf Mustern"""
        eingabe_lower = eingabe.lower()
        
        # Frage-Muster
        if "?" in eingabe:
            antworten = [
                "Das ist eine interessante Frage! Ich arbeite noch daran, das zu verstehen.",
                "Hmm, lass mich darüber nachdenken... Kannst du mehr Details geben?",
                "Gute Frage! Leider habe ich dazu noch keine Information. Möchtest du es mir beibringen?",
                "Ich bin mir nicht ganz sicher. Probier mal: 'lerne: [Begriff] = [Erklärung]'"
            ]
            return random.choice(antworten)
        
        # Emotionale Aussagen
        if any(wort in eingabe_lower for wort in ["toll", "super", "großartig", "gut"]):
            return random.choice(["Das freut mich! 😊", "Fantastisch! 🎉", "Das ist großartig! ⭐"])
        
        if any(wort in eingabe_lower for wort in ["schlecht", "traurig", "mist", "ärger"]):
            return random.choice(["Das tut mir leid zu hören. 😟", "Ich verstehe... Kann ich helfen?", "Kopf hoch! 💪"])
        
        # Standard
        return random.choice([
            "Interessant! Erzähl mir mehr darüber.",
            "Verstehe. Was möchtest du noch wissen?",
            "Okay, ich habe das notiert. Wie kann ich dir weiter helfen?",
            "Das ist spannend! Möchtest du, dass ich etwas dazu lerne?",
            "Probiere: 'analysiere: [Text]', 'lerne: [Begriff] = [Info]' oder 'statistik: [Text]'"
        ])
    
    def spreche(self, text):
        """Sprachausgabe"""
        if self.tts_verfuegbar:
            try:
                self.tts_engine.say(text)
                self.tts_engine.runAndWait()
            except:
                pass


class KIAssistentGUI:
    def __init__(self):
        self.ki = KIAssistent()
        
        # Hauptfenster
        self.window = tk.Tk()
        self.window.title("🤖 KI-Assistent")
        self.window.geometry("900x700")
        self.window.configure(bg='#1e1e1e')
        
        self.erstelle_gui()
    
    def erstelle_gui(self):
        """Erstellt die Benutzeroberfläche"""
        # Header
        header = tk.Frame(self.window, bg='#2d2d30', height=80)
        header.pack(fill=tk.X)
        
        titel = tk.Label(header, text="🤖 KI-ASSISTENT", 
                        bg='#2d2d30', fg='#00ff00',
                        font=('Arial', 24, 'bold'))
        titel.pack(pady=20)
        
        # Chat-Bereich
        chat_frame = tk.Frame(self.window, bg='#1e1e1e')
        chat_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        self.chat_display = scrolledtext.ScrolledText(
            chat_frame, wrap=tk.WORD, state='disabled',
            bg='#252526', fg='#ffffff', font=('Consolas', 11),
            insertbackground='white', relief=tk.FLAT
        )
        self.chat_display.pack(fill=tk.BOTH, expand=True)
        
        # Eingabe-Bereich
        eingabe_frame = tk.Frame(self.window, bg='#2d2d30', height=100)
        eingabe_frame.pack(fill=tk.X, padx=20, pady=10)
        
        self.eingabe_text = tk.Text(
            eingabe_frame, height=3, font=('Arial', 11),
            bg='#3e3e42', fg='#ffffff', insertbackground='white',
            relief=tk.FLAT, wrap=tk.WORD
        )
        self.eingabe_text.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        self.eingabe_text.bind('<Return>', lambda e: self.sende_nachricht() if not e.state & 1 else None)
        
        # Buttons
        button_frame = tk.Frame(eingabe_frame, bg='#2d2d30')
        button_frame.pack(fill=tk.X)
        
        self.send_btn = tk.Button(
            button_frame, text="📤 Senden",
            command=self.sende_nachricht,
            bg='#0e639c', fg='white', font=('Arial', 10, 'bold'),
            cursor='hand2', relief=tk.FLAT, padx=20, pady=8
        )
        self.send_btn.pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            button_frame, text="🧹 Löschen",
            command=self.chat_loeschen,
            bg='#c5392b', fg='white', font=('Arial', 10, 'bold'),
            cursor='hand2', relief=tk.FLAT, padx=20, pady=8
        ).pack(side=tk.LEFT, padx=5)
        
        if self.ki.tts_verfuegbar:
            tk.Button(
                button_frame, text="🔊 Sprechen",
                command=self.letztes_sprechen,
                bg='#107c10', fg='white', font=('Arial', 10, 'bold'),
                cursor='hand2', relief=tk.FLAT, padx=20, pady=8
            ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            button_frame, text="💡 Hilfe",
            command=self.zeige_hilfe,
            bg='#6d6d6d', fg='white', font=('Arial', 10, 'bold'),
            cursor='hand2', relief=tk.FLAT, padx=20, pady=8
        ).pack(side=tk.RIGHT, padx=5)
        
        # Begrüßung
        self.zeige_nachricht("KI", "Hallo! Ich bin dein KI-Assistent. Wie kann ich dir helfen?\n\n"
                            "💡 Tipp: Schreibe 'hilfe' für eine Übersicht meiner Funktionen!", "#00ff00")
    
    def zeige_nachricht(self, absender, nachricht, farbe='#ffffff'):
        """Zeigt Nachricht im Chat"""
        self.chat_display.config(state='normal')
        
        # Zeitstempel
        zeit = datetime.datetime.now().strftime("%H:%M:%S")
        
        # Absender
        if absender == "KI":
            self.chat_display.insert(tk.END, f"\n🤖 KI ({zeit}):\n", 'ki')
            self.chat_display.tag_config('ki', foreground='#00ff00', font=('Arial', 10, 'bold'))
        else:
            self.chat_display.insert(tk.END, f"\n👤 Du ({zeit}):\n", 'user')
            self.chat_display.tag_config('user', foreground='#00bfff', font=('Arial', 10, 'bold'))
        
        # Nachricht
        self.chat_display.insert(tk.END, nachricht + "\n", 'nachricht')
        self.chat_display.tag_config('nachricht', foreground=farbe)
        
        self.chat_display.see(tk.END)
        self.chat_display.config(state='disabled')
    
    def sende_nachricht(self):
        """Sendet Nachricht an KI"""
        eingabe = self.eingabe_text.get("1.0", tk.END).strip()
        
        if eingabe:
            # Zeige Benutzer-Nachricht
            self.zeige_nachricht("Du", eingabe, "#00bfff")
            
            # KI-Antwort
            antwort = self.ki.verarbeite_anfrage(eingabe)
            self.zeige_nachricht("KI", antwort, "#ffffff")
            
            # Eingabe löschen
            self.eingabe_text.delete("1.0", tk.END)
            
            # Letzte Antwort speichern
            self.letzte_antwort = antwort
    
    def chat_loeschen(self):
        """Löscht Chat-Verlauf"""
        self.chat_display.config(state='normal')
        self.chat_display.delete("1.0", tk.END)
        self.chat_display.config(state='disabled')
        self.zeige_nachricht("KI", "Chat wurde geleert! Wie kann ich dir helfen?", "#00ff00")
    
    def letztes_sprechen(self):
        """Spricht letzte Antwort aus"""
        if hasattr(self, 'letzte_antwort'):
            self.ki.spreche(self.letzte_antwort)
    
    def zeige_hilfe(self):
        """Zeigt Hilfe-Dialog"""
        hilfe_text = """
🤖 KI-ASSISTENT HILFE

📚 BEFEHLE:

1. LERNEN:
   lerne: Python = Eine Programmiersprache
   merke: Geburtstag = 15. Mai

2. WISSEN ABRUFEN:
   Was ist Python?
   Was sind Algorithmen?

3. SENTIMENT-ANALYSE:
   analysiere: Ich bin sehr glücklich heute!
   sentiment: Das Wetter ist schrecklich

4. TEXT-STATISTIK:
   statistik: [Dein langer Text hier]

5. MATHEMATIK:
   5 + 3 * 2
   Was ist 100 / 5?

6. WISSENSBASIS:
   Was weißt du?
   Was kannst du?

💬 ALLTAGS-GESPRÄCH:
   Einfach normal mit mir reden!
   Fragen stellen, Meinungen teilen, etc.
"""
        messagebox.showinfo("Hilfe", hilfe_text)
    
    def run(self):
        """Startet die GUI"""
        self.window.mainloop()


def main():
    """Hauptprogramm"""
    print("=" * 50)
    print("🤖 KI-ASSISTENT PROGRAMM")
    print("=" * 50)
    print()
    print("Starte GUI...")
    print()
    
    if not TEXTBLOB_VERFUEGBAR:
        print("⚠️  Für volle Funktionalität installiere:")
        print("   pip install textblob textblob-de nltk")
        print()
    
    app = KIAssistentGUI()
    app.run()


if __name__ == "__main__":
    main()