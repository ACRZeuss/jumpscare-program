import os
import random
import pygame
import tkinter as tk
from threading import Thread
import time

def play_random_sound(folder_path):
    sound_files = os.listdir(folder_path)
    sound_file = random.choice(sound_files)
    sound_path = os.path.join(folder_path, sound_file)

    pygame.mixer.init()
    pygame.mixer.music.load(sound_path)
    pygame.mixer.music.play()

    pygame.time.wait(random.randint(10000, 60000))

    pygame.mixer.music.stop()

def start_playing():
    folder_path = folder_path_entry.get()
    status_label.config(text="Program Çalışıyor")
    play_thread = Thread(target=continuous_play, args=(folder_path,))
    play_thread.start()

def continuous_play(folder_path):
    while True:
        play_random_sound(folder_path)
        time.sleep(random.randint(10, 60))

def stop_playing():
    status_label.config(text="Program Çalışmıyor")
    pygame.mixer.music.stop()

# Tkinter arayüzünü oluşturma
window = tk.Tk()
window.title("Ses Oynatıcı")
window.geometry("300x300")

# Klasör yolu metin kutusu
folder_path_label = tk.Label(window, text="Klasör Yolu:")
folder_path_label.pack(pady=10)
folder_path_entry = tk.Entry(window)
folder_path_entry.pack(pady=5)

# Başlat düğmesini oluşturma
start_button = tk.Button(window, text="Başlat", command=start_playing)
start_button.pack(pady=10)

# Durdur düğmesini oluşturma
stop_button = tk.Button(window, text="Durdur", command=stop_playing)
stop_button.pack(pady=10)

# Durum çubuğunu oluşturma
status_label = tk.Label(window, text="Program Çalışmıyor", bd=1, relief=tk.SUNKEN, anchor=tk.W)
status_label.pack(side=tk.BOTTOM, fill=tk.X)

# Tkinter arayüzünü çalıştırma
window.mainloop()