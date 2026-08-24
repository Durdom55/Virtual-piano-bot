#---Import---
import keyboard #*
import threading
import time
from tkinter.messagebox import showwarning
import config

#---Var---
cache = ''
cacheOn = False

#---Func---
def BotPlay(text, pb):
    global cacheOn, Sleep, cache
    text = text.get('0.0', 'end')
    numofsteps = len(text)
    progVal = 1/numofsteps
    stepVal = 0
    Sleeptime=config.Sleep
    print('text get')
    if config.IsRun==True:
        for i in text:
            if not config.IsRun:
                break
            print(i)
            stepVal+=progVal
            pb.set(stepVal)
            if i in [' ', '[', ']', '{', '}', '-', '—', '–']:
                match i:
                    case ' ':
                        time.sleep(Sleeptime/config.Speed)
                    case '[':
                        cacheOn=True
                    case ']':
                        cacheOn=False
                        print(cache)
                        cash_press(cache)
                        cache=''
                        time.sleep(Sleeptime/config.Speed)
                    case '{':
                        Sleeptime-=0.15
                    case '}':
                        Sleeptime=Sleep
                    case '-':
                        time.sleep((Sleeptime+0.04)/config.Speed)
                    case '—':
                        time.sleep((Sleeptime+0.05)/config.Speed)
                    case '–':
                        time.sleep((Sleeptime+0.043)/config.Speed)
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
    
def cash_press(cache):
    for i in cache:
        if i.isupper():
            keyboard.send(f'shift+{i.lower()}')
        else:      
            keyboard.send(i)

def Wait(app, buts, butp, text, pb):
    if config.HotBut!='':
        if keyboard.is_pressed(config.HotBut) and config.NotRecord:
            print("nazhata")
            if config.IsRun == False:
                print("Startw")
                StartBut(buts, text, pb)
            else:
                print('StopW')
                StopBut(buts, butp)
    else:
        showwarning(title='Warning', message='Set HotKey for proper operation')
        return
    app.after(30, lambda: Wait(app, buts, butp, text, pb))
    
def Start(app, buts, butp, text, pb):
    buts.configure(state='disabled')
    buts.configure(text=f'Press {config.HotBut} to playing')
    butp.configure(state='normal')
    Wait(app, buts, butp, text, pb)
    
def Stop(buts, butp):
    buts.configure(state='normal')
    buts.configure(text='▶ START')
    butp.configure(state='disabled')
                
def StopBut(buts, butp):
    global cacheOn, cache, Sleep
    cache = ''
    cacheOn = False
    Sleep=0.417
    print("Stop")
    buts.configure(text=f'Press {config.HotBut} to playing')
    config.IsRun=False
    while keyboard.is_pressed(config.HotBut):
        time.sleep(0.01)
    
def StartBut(buts, text, pb):
    print("Start")
    pb.set(0)
    config.IsRun=True
    buts.configure(text=f'Press {config.HotBut} to stop')
    while keyboard.is_pressed(config.HotBut):
        time.sleep(0.01)
    threading.Thread(target=BotPlay, args=(text,pb, ), daemon=True).start()