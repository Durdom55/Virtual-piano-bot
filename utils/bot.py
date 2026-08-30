#---Import---
import keyboard #*
import threading, time
from tkinter.messagebox import showwarning
from . import config

#---Var---
cache = ''
cacheOn = False

#---Func---
def BotPlay(app):
    global cacheOn, Sleep, cache
    text = app.musicfield.get('0.0', 'end')
    numofsteps = len(text)
    progVal = 1/numofsteps
    stepVal = 0
    Sleeptime=config.Sleep
    if config.IsRun==True:
        for i in text:
            if not config.IsRun:
                break
            stepVal+=progVal
            app.progbar.set(stepVal)
            if i in [' ', '[', ']', '{', '}', '-', '—', '–', '|']:
                match i:
                    case '|':
                        pass
                    case ' ':
                        time.sleep(Sleeptime/config.Speed)
                    case '[':
                        cacheOn=True
                    case ']':
                        cacheOn=False
                        cash_press(cache)
                        cache=''
                        time.sleep(Sleeptime/config.Speed)
                    case '{':
                        Sleeptime+=config.parenthesis
                    case '}':
                        Sleeptime=Sleep
                    case '-':
                        time.sleep((Sleeptime+config.dash)/config.Speed)
                    case '—':
                        time.sleep((Sleeptime+config.bigdash)/config.Speed)
                    case '–':
                        time.sleep((Sleeptime+config.middash)/config.Speed)
            else:
                if cacheOn==True:
                    cache+=i
                else:
                    if i.isupper():
                        keyboard.send(f'shift+{i.lower()}')
                    else:      
                        keyboard.send(i)
                    time.sleep(Sleeptime/config.Speed)
    config.IsRun = False
    app.progbar.set(0)
    StopBut(app)
    
def cash_press(cache):
    for i in cache:
        if i.isupper():
            keyboard.send(f'shift+{i.lower()}')
        else:      
            keyboard.send(i)

def Wait(app):
    if config.HotBut!='':
        if config.Iswait:        
            if keyboard.is_pressed(config.HotBut) and config.NotRecord:
                if config.IsRun == False:
                    StartBut(app)
                else:
                    StopBut(app)
        else:
            return
    else:
        showwarning(title='Warning', message='Set HotKey for proper operation')
        Stop(app)
        return
    app.after(30, lambda: Wait(app))
    
def Start(app): #, buts, butp, text, pb
    if config.HotBut != '':    
        app.butStart.configure(state='disabled')
        app.butStart.configure(text=f'Press {config.HotBut} to playing')
        app.butStop.configure(state='normal')
        app.update()
        keyboard.unhook_all()
        if hasattr(keyboard, '_pressed_events'):
            keyboard._pressed_events.clear()
        config.Iswait = True
        Wait(app)
    else:
        showwarning(title='Warning', message='Set HotKey for proper operation')
        Stop(app)
        return
    
def Stop(app):
    app.butStart.configure(state='normal')
    app.butStart.configure(text='▶ START')
    app.butStop.configure(state='disabled')
    app.update()
    config.Iswait = False
                
def StopBut(app):
    global cacheOn, cache, Sleep
    cache = ''
    cacheOn = False
    Sleep=0.417
    app.butStart.configure(text=f'Press {config.HotBut} to playing')
    config.IsRun=False
    while keyboard.is_pressed(config.HotBut):
        time.sleep(0.01)
    
def StartBut(app):
    app.progbar.set(0)
    config.IsRun=True
    app.butStart.configure(text=f'Press {config.HotBut} to stop')
    while keyboard.is_pressed(config.HotBut):
        time.sleep(0.01)
    threading.Thread(target=BotPlay, args=(app, ), daemon=True).start()