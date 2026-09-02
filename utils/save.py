from . import config
import keyboard, string, threading, json
from tkinter.messagebox import showerror

is_listening = False
lock = threading.Lock()

def load():
    try:
        with open ('Settings.json', 'r') as f:
            config.saves = json.load(f)
        config.HotBut = config.saves.get('HotBut', config.HotBut)
        config.Sleep = config.saves.get('Sleep', config.Sleep)
        config.dash = config.saves.get('dash', config.dash)
        config.bigdash = config.saves.get('bigdash', config.bigdash)
        config.middash = config.saves.get('middash', config.middash)
        config.parenthesis = config.saves.get('parenthesis', config.parenthesis)
        config.songs = config.saves.get('songs', config.songs)
        config.current_song = config.saves.get('current_song', config.current_song)
    except:
        pass

def Save():
    config.saves['HotBut'] = config.HotBut
    config.saves['Sleep'] = config.Sleep
    config.saves['dash'] = config.dash
    config.saves['bigdash'] = config.bigdash
    config.saves['middash'] = config.middash
    config.saves['parenthesis'] = config.parenthesis
    config.saves['songs'] = config.songs
    config.saves['current_song'] = config.current_song
    with open ('Settings.json', 'w') as f:
        json.dump(config.saves, f, indent=4)
    print('save')

def Listening(app, win):
    global is_listening
    try:
        config.NotRecord = False
        app.inputButton.configure(text='Waiting for Input...')
        app.update()
        keyboard.unhook_all()
        if hasattr(keyboard, '_pressed_events'):
            keyboard._pressed_events.clear()
        hotkey = keyboard.read_hotkey()
        if win.winfo_exists():
            if langcheck(hotkey):
                config.HotBut = hotkey
                app.inputButton.configure(text=f'{config.HotBut}')
                app.update()
                return
            else:
                showerror(title='error', message='Switch to English keyboard layout')
                return
        else:
            return
    finally:
        if win.winfo_exists():    
            app.inputButton.configure(state='normal')
            app.cancelbut.configure(state='normal')
            app.clearbut.configure(state='normal')
            app.savebut.configure(state='normal')  
            app.update()
            is_listening=False
        config.NotRecord = True
    
def PreListening(app, win):
    global is_listening
    if config.IsRun:
        return
    with lock:
        if is_listening:
            return
        is_listening = True
        config.HotBut = ''
        app.inputButton.configure(state='disabled')
        app.cancelbut.configure(state='disabled')
        app.clearbut.configure(state='disabled')
        app.savebut.configure(state='disabled')        
        app.update()
    threading.Thread(target=Listening, args=(app, win, ), daemon=True).start()
    
def langcheck(key):
    keys = key.split('+')
    for i in keys:
        if len(i) == 1 and i.isalpha():
            if i not in string.ascii_letters:
                return False
    return True

def clear(app):
    global is_listening
    if config.IsRun:
        return
    if not is_listening:
        config.HotBut = ''
        app.inputButton.configure(text='Click to Set Hotkey')
        app.update()
        
def ToDefault(app):
    config.Sleep = config.default_Sleep
    config.dash = config.default_dash
    config.bigdash = config.default_bigdash
    config.middash = config.default_middash
    config.parenthesis = config.default_parenthesis
    app.middEn.set(config.middash)
    app.par.configure(validate='none')
    app.par.set(config.parenthesis)
    app.par.configure(validate='key')
    app.bigdEn.set(config.bigdash)
    app.dEn.set(config.dash)
    app.sleepen.set(config.Sleep)