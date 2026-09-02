from tkinter.messagebox import showerror
import json
from . import config

def SaveSong(app):
    val = app.allsongs.cget()
    
def NewSong(app):
    song_index = len(config.songs) + 1
    config.songs.append(f'New song №{song_index}')
    app.allsongs.configure(values=config.songs)
    app.allsongs.set(config.songs[song_index-1])
    print(config.songs)