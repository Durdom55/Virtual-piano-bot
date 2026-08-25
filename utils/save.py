from . import config
import keyboard, string, threading, time
from tkinter.messagebox import showerror

is_listening = False
lock = threading.Lock()

def Listening(app, InpBut, win):
    global is_listening
    try:
        InpBut.configure(text='Waiting for Input...')
        app.update()
        print('izmenil')
        keyboard.unhook_all()
        if hasattr(keyboard, '_pressed_events'):
            keyboard._pressed_events.clear()
            print('sbrosil1')
        print('sbrosil2')
        hotkey = keyboard.read_hotkey()
        print('zapisal')
        if win.winfo_exists():
            print('otkrito')
            if langcheck(hotkey):
                print('en')
                config.HotBut = hotkey
                print(config.HotBut)
                InpBut.configure(text=f'{config.HotBut}')
                app.update()
                return
                
            else:
                print('ru')
                showerror(title='error', message='Switch to English keyboard layout')
                return
        else:
            print('ne')
            return
    finally:
        InpBut.configure(state='normal')
        app.update()
        print('vse')
        is_listening=False
    
def PreListening(app, InpBut, win):
    global is_listening
    print(config.HotBut)
    print('PreListening called, is_listening =', is_listening)
    with lock:
        if is_listening:
            print('Already listening, ignoring')
            return
        is_listening = True
        config.HotBut = ''          # очищаем только теперь
        InpBut.configure(state='disabled')
        app.update()
    threading.Thread(target=Listening, args=(app, InpBut, win, ), daemon=True).start()
    
def langcheck(key):
    print('checkay')
    keys = key.split('+')
    for i in keys:
        if len(i) == 1 and i.isalpha():
            if i not in string.ascii_letters:
                return False
    return True