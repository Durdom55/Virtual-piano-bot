from . import config
import keyboard, string, threading, time, json
from tkinter.messagebox import showerror

is_listening = False
lock = threading.Lock()

def load():
    try:
        with open ('Settings.json', 'r') as f:
            config.saves = json.load(f)
        config.HotBut = config.saves.get('HotBut', config.HotBut)
        config.Speed = config.saves.get('Speed', config.Speed)
    except:
        pass

def Save():
    config.saves['HotBut'] = config.HotBut
    config.saves['Speed'] = config.Speed
    with open ('Settings.json', 'w') as f:
        json.dump(config.saves, f, indent=4)

def Listening(app, InpBut, win):
    global is_listening
    try:
        InpBut.configure(text='Waiting for Input...')
        app.update()
        keyboard.unhook_all()
        if hasattr(keyboard, '_pressed_events'):
            keyboard._pressed_events.clear()
        hotkey = keyboard.read_hotkey()
        if win.winfo_exists():
            if langcheck(hotkey):
                config.HotBut = hotkey
                InpBut.configure(text=f'{config.HotBut}')
                app.update()
                return
                
            else:
                showerror(title='error', message='Switch to English keyboard layout')
                return
        else:
            print('zakrito')
            return
    finally:
        if win.winfo_exists():    
            InpBut.configure(state='normal')
            app.update()
            is_listening=False
    
def PreListening(app, InpBut, win):
    global is_listening
    if config.IsRun:
        return
    with lock:
        if is_listening:
            return
        is_listening = True
        config.HotBut = ''
        InpBut.configure(state='disabled')
        app.update()
    threading.Thread(target=Listening, args=(app, InpBut, win, ), daemon=True).start()
    
def langcheck(key):
    keys = key.split('+')
    for i in keys:
        if len(i) == 1 and i.isalpha():
            if i not in string.ascii_letters:
                return False
    return True

def clear(app, InpBut):
    if config.IsRun:
        return
    if not is_listening:
        config.HotBut = ''
        InpBut.configure(text='Click to Set Hotkey')
        app.update()