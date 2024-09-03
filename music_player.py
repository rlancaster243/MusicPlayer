# music_player_gui.py
# Ensure pygame is installed: pip install pygame
import pygame
import os
import tkinter as tk
from tkinter import filedialog, messagebox

class MusicPlayer:
    def __init__(self, music_directory):
        self.music_directory = music_directory
        self.playlist = self.load_playlist()
        pygame.mixer.init()

    def load_playlist(self):
        return [os.path.join(self.music_directory, file) for file in os.listdir(self.music_directory) if file.endswith('.mp3')]

    def play(self, track_number=0):
        if 0 <= track_number < len(self.playlist):
            pygame.mixer.music.load(self.playlist[track_number])
            pygame.mixer.music.play()
            print(f"Playing: {self.playlist[track_number]}")
        else:
            print("Track number out of range")

    def stop(self):
        pygame.mixer.music.stop()
        print("Music stopped")

    def pause(self):
        pygame.mixer.music.pause()
        print("Music paused")

    def unpause(self):
        pygame.mixer.music.unpause()
        print("Music unpaused")

    def next_track(self, current_track):
        next_track = (current_track + 1) % len(self.playlist)
        self.play(next_track)

    def previous_track(self, current_track):
        previous_track = (current_track - 1) % len(self.playlist)
        self.play(previous_track)

class MusicPlayerUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("400x300")
        self.root.configure(bg="#282c34")
        
        self.player = None
        self.current_track = 0

        self.create_widgets()

    def create_widgets(self):
        # Title Label
        self.title_label = tk.Label(self.root, text="Music Player", font=("Helvetica", 16, "bold"), bg="#282c34", fg="#61dafb")
        self.title_label.pack(pady=10)

        # Control Frame
        self.control_frame = tk.Frame(self.root, bg="#282c34")
        self.control_frame.pack(pady=10)

        # Load Button
        self.load_button = tk.Button(self.control_frame, text="Load Music Directory", command=self.load_music_directory, bg="#61dafb", fg="#282c34", font=("Helvetica", 10, "bold"))
        self.load_button.grid(row=0, column=0, padx=5, pady=5)

        # Play Button
        self.play_button = tk.Button(self.control_frame, text="Play", command=self.play, bg="#61dafb", fg="#282c34", font=("Helvetica", 10, "bold"))
        self.play_button.grid(row=0, column=1, padx=5, pady=5)

        # Pause Button
        self.pause_button = tk.Button(self.control_frame, text="Pause", command=self.pause, bg="#61dafb", fg="#282c34", font=("Helvetica", 10, "bold"))
        self.pause_button.grid(row=0, column=2, padx=5, pady=5)

        # Unpause Button
        self.unpause_button = tk.Button(self.control_frame, text="Unpause", command=self.unpause, bg="#61dafb", fg="#282c34", font=("Helvetica", 10, "bold"))
        self.unpause_button.grid(row=1, column=0, padx=5, pady=5)

        # Stop Button
        self.stop_button = tk.Button(self.control_frame, text="Stop", command=self.stop, bg="#61dafb", fg="#282c34", font=("Helvetica", 10, "bold"))
        self.stop_button.grid(row=1, column=1, padx=5, pady=5)

        # Next Button
        self.next_button = tk.Button(self.control_frame, text="Next", command=self.next_track, bg="#61dafb", fg="#282c34", font=("Helvetica", 10, "bold"))
        self.next_button.grid(row=1, column=2, padx=5, pady=5)

        # Previous Button
        self.previous_button = tk.Button(self.control_frame, text="Previous", command=self.previous_track, bg="#61dafb", fg="#282c34", font=("Helvetica", 10, "bold"))
        self.previous_button.grid(row=2, column=0, padx=5, pady=5)

        # Track Label
        self.track_label = tk.Label(self.root, text="No track loaded", font=("Helvetica", 12), bg="#282c34", fg="#61dafb")
        self.track_label.pack(pady=10)

    def load_music_directory(self):
        music_directory = filedialog.askdirectory()
        if music_directory:
            self.player = MusicPlayer(music_directory)
            self.current_track = 0  # Reset to the first track
            self.update_track_label()
            print(f"Loaded music directory: {music_directory}")

    def play(self):
        if self.player:
            self.player.play(self.current_track)
            self.update_track_label()

    def pause(self):
        if self.player:
            self.player.pause()

    def unpause(self):
        if self.player:
            self.player.unpause()

    def stop(self):
        if self.player:
            self.player.stop()

    def next_track(self):
        if self.player:
            self.current_track = (self.current_track + 1) % len(self.player.playlist)
            self.player.play(self.current_track)
            self.update_track_label()

    def previous_track(self):
        if self.player:
            self.current_track = (self.current_track - 1) % len(self.player.playlist)
            self.player.play(self.current_track)
            self.update_track_label()

    def update_track_label(self):
        if self.player and self.player.playlist:
            current_track_name = os.path.basename(self.player.playlist[self.current_track])
            self.track_label.config(text=f"Playing: {current_track_name}")
        else:
            self.track_label.config(text="No track loaded")

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayerUI(root)
    root.mainloop()