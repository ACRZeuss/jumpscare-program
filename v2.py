import os
import random
import pygame
import tkinter as tk
from threading import Thread

def play_random_sound(folder_path):
    sound_files = os.listdir(folder_path)
    sound_file = random.choice(sound_files)
    sound_path = os.path.join(folder_path, sound_file)

    pygame.mixer.init()
    pygame.mixer.music.load(sound_path)
    pygame.mixer.music.play()

    pygame.time.wait(30000)  # 30 saniye bekleme

    pygame.mixer.music.stop()

def start_playing():
    folder_path = "E:\Erhan\Music"  # Klasör yolunu burada belirtin
    Thread(target=play_random_sound, args=(folder_path,)).start()

def stop_playing():
    pygame.mixer.music.stop()

# Tkinter arayüzünü oluşturma
window = tk.Tk()
window.title("Ses Oynatıcı")
window.geometry("300x150")

# Başlat düğmesini oluşturma
start_button = tk.Button(window, text="Başlat", command=start_playing)
start_button.pack(pady=20)

# Durdur düğmesini oluşturma
stop_button = tk.Button(window, text="Durdur", command=stop_playing)
stop_button.pack(pady=10)

# Tkinter arayüzünü çalıştırma
window.mainloop()
