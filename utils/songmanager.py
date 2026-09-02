from tkinter.messagebox import showerror
import json
from . import config

def SaveSong(app):
    val = app.allsongs.cget()
    
def NewSong(app):
    if not config.IsRun:
        app.deleteSong.configure(state="disabled")
        song_index = len(config.songs) + 1
        new_song = f'New song №{song_index}'
        while new_song in config.songs:
            new_song = f'New song №{song_index+1}'
        config.songs.append(new_song)
        app.allsongs.configure(values=config.songs)
        app.allsongs.set(config.songs[song_index-1])
        app.deleteSong.configure(state="normal")
        print(config.songs)
    
def DeleteSong(app):
    if not config.IsRun:
        app.plussong.configure(state='disabled')
        quan = len(config.songs)
        if quan > 1:    
            current_song = app.allsongs.get()
            print(current_song)
            config.songs.remove(current_song)
            song_index = len(config.songs)
            app.allsongs.configure(values=config.songs)
            app.allsongs.set(config.songs[song_index-1])
            print(config.songs)
        app.plussong.configure(state='normal')