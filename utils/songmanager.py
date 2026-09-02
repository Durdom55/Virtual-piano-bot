from tkinter.messagebox import showerror
import json, os
from . import config
from .save import Save

def SaveSong(app):
    config.current_song_data['Speed'] = config.Speed
    try:     
        config.current_song_data['Sheets'] = app.musicfield.get('0.0', 'end-1c')
    except:
        pass
    with open(f'Saves/{config.current_song}', 'w') as f:
        json.dump(config.current_song_data, f, indent=4)
    print('save song')
    
def LoadSong(app):
    try:
        with open(f'Saves/{config.current_song}', 'r') as f:
            config.current_song_data = json.load(f)
        config.Speed = config.current_song_data.get('Speed', config.Speed)
        config.sheets = config.current_song_data.get('Sheets', config.sheets)
        print(config.sheets)
    except:
        SaveSong(app)
    
def NewSong(app):
    if not config.IsRun:
        app.deleteSong.configure(state="disabled")
        song_index = len(config.songs) + 1
        new_song = f'New song №{song_index}'
        while new_song in config.songs:
            new_song = f'New song №{song_index+1}'
        config.songs.append(new_song)
        config.current_song = new_song
        app.allsongs.configure(values=config.songs)
        app.allsongs.set(config.songs[song_index-1])
        app.deleteSong.configure(state="normal")
        Save()
        SaveSong(app)
        print(config.songs)
    
def DeleteSong(app):
    if not config.IsRun:
        app.plussong.configure(state='disabled')
        quan = len(config.songs)
        if quan > 1:    
            current_song = app.allsongs.get()
            print(current_song)
            config.songs.remove(current_song)
            os.remove(f'Saves/{config.current_song}')
            song_index = len(config.songs)
            app.allsongs.configure(values=config.songs)
            cur_song = config.songs[song_index-1]
            config.current_song = cur_song
            app.allsongs.set(cur_song)
            Save()
            print(config.songs)
        app.plussong.configure(state='normal')