import time
import random
import os
import threading
from playsound3 import playsound


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_random_color():
    colors = [
        '\033[91m',  # Rot
        '\033[92m',  # Grün
        '\033[94m',  # Blau
        '\033[93m',  # Gelb
        '\033[95m',  # Magenta
        '\033[96m',  # Cyan
    ]
    return random.choice(colors)

def play_sound_once(sound_file):
    try:
        playsound(sound_file)
    except:
        pass

def draw_tree():
    reset = '\033[0m'
    
    tree = [
        "        *        ",
        "       ***       ",
        "      *****      ",
        "     *******     ",
        "    *********    ",
        "   ***********   ",
        "  *************  ",
        " *************** ",
        "*****************",
        "       |||       ",
        "       |||       "
    ]
    
    colored_tree = []
    for line in tree[:-2]: 
        colored_line = ""
        for char in line:
            if char == '*':
                colored_line += get_random_color() + char + reset
            else:
                colored_line += char
        colored_tree.append(colored_line)
    
    brown = '\033[33m'
    colored_tree.append(brown + tree[-2] + reset)
    colored_tree.append(brown + tree[-1] + reset)
    
    return '\n'.join(colored_tree)

try:
    sound_file = "indian_xmas.mp3"  
    if os.path.exists(sound_file):
        sound_thread = threading.Thread(target=play_sound_once, args=(sound_file,), daemon=True)
        sound_thread.start()
    
    while True:
        clear_screen()
        print(draw_tree())
        print("Frohe Weihnachten! 🎄")
        time.sleep(0.5)
except KeyboardInterrupt:
    clear_screen()