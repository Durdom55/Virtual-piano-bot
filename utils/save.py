from . import config
import keyboard, string

def Listening(app, InpBut, winop):
    InpBut.configure(text='Waiting for Input...')
    app.update()
    print('izmenil')
    hotkey = keyboard.read_hotkey()
    print('zapisal')
    if winop ==True:
        print('otkrito')
        if langcheck(hotkey):
            print('en')
            
        else:
            print('ru')
            return
    else:
        print('ne')
        return
    
def langcheck(key):
    print('checkay')
    keys = key.split('+')
    for i in keys:
        if len(i) == 1 and i.isalpha():
            if i not in string.ascii_letters:
                return False
    return True